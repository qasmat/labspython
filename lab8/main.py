from __future__ import annotations

from pathlib import Path
from typing import Optional

import wx
from PIL import Image, ImageDraw, ImageFont


class MemeGeneratorError(Exception):
    """Базовое исключение приложения."""


class ImageNotLoadedError(MemeGeneratorError):
    """Изображение не загружено."""


class MemeSaveError(MemeGeneratorError):
    """Ошибка сохранения мема."""


class InvalidTextError(MemeGeneratorError):
    """Некорректный текст мема."""


class Meme:
    """Модель мема."""

    def __init__(self) -> None:
        self.image: Optional[Image.Image] = None
        self.path: Optional[Path] = None

    def load_image(self, file_path: str) -> None:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        self.image = Image.open(path).convert("RGB")
        self.path = path

    def _get_font(self, font_size: int) -> ImageFont.ImageFont:
        """Загружает шрифт, который поддерживает кириллицу."""
        
        possible_fonts = [
            "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
            "/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf",
            str(Path(__file__).parent / "DejaVuSans.ttf"),
            "DejaVuSans.ttf",
        ]
        
        for font_path in possible_fonts:
            try:
                if Path(font_path).exists():
                    return ImageFont.truetype(font_path, font_size)
            except Exception:
                continue
        
        raise MemeGeneratorError(
            "Не найден ни один шрифт, поддерживающий кириллицу. "
            "Установите пакет: sudo apt install fonts-noto-cjk"
        )

    def generate(
        self,
        top_text: str,
        bottom_text: str,
        font_size: int = 40,
    ) -> Image.Image:
        if self.image is None:
            raise ImageNotLoadedError("Сначала загрузите изображение.")

        if not top_text.strip() and not bottom_text.strip():
            raise InvalidTextError(
                "Введите хотя бы один текст для мема."
            )

        image = self.image.copy()
        draw = ImageDraw.Draw(image)

        font = self._get_font(font_size)

        width, height = image.size

        self._draw_text(
            draw=draw,
            text=top_text.upper(),
            font=font,
            image_width=width,
            y_position=20,
        )

        self._draw_text(
            draw=draw,
            text=bottom_text.upper(),
            font=font,
            image_width=width,
            y_position=height - font_size - 40,
        )

        return image

    @staticmethod
    def _draw_text(
        draw: ImageDraw.ImageDraw,
        text: str,
        font: ImageFont.ImageFont,
        image_width: int,
        y_position: int,
    ) -> None:
        if not text:
            return

        bbox = draw.textbbox((0, 0), text=text, font=font)

        text_width = bbox[2] - bbox[0]
        x_position = (image_width - text_width) // 2

        outline_range = 2

        for offset_x in range(-outline_range, outline_range + 1):
            for offset_y in range(-outline_range, outline_range + 1):
                draw.text(
                    (x_position + offset_x, y_position + offset_y),
                    text,
                    font=font,
                    fill="black",
                )

        draw.text(
            (x_position, y_position),
            text,
            font=font,
            fill="white",
        )


class MemeGeneratorFrame(wx.Frame):
    """Главное окно приложения."""

    PREVIEW_SIZE = (700, 500)

    def __init__(self) -> None:
        super().__init__(
            parent=None,
            title="Генератор мемов",
            size=(900, 800),
        )

        self.meme = Meme()
        self.generated_image: Optional[Image.Image] = None

        self.panel = wx.Panel(self)

        self.image_preview = wx.StaticBitmap(self.panel)

        self.top_text_ctrl = wx.TextCtrl(self.panel)
        self.bottom_text_ctrl = wx.TextCtrl(self.panel)

        self.font_size_ctrl = wx.SpinCtrl(
            self.panel,
            min=20,
            max=100,
            initial=40,
        )

        self.load_button = wx.Button(
            self.panel,
            label="Загрузить изображение",
        )

        self.generate_button = wx.Button(
            self.panel,
            label="Создать мем",
        )

        self.save_button = wx.Button(
            self.panel,
            label="Сохранить мем",
        )

        self._build_layout()
        self._bind_events()

        self.Center()
        self.Show()

    def _build_layout(self) -> None:
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        controls_sizer = wx.FlexGridSizer(
            rows=4,
            cols=2,
            hgap=10,
            vgap=10,
        )

        controls_sizer.Add(
            wx.StaticText(self.panel, label="Текст сверху:"),
            0,
            wx.ALIGN_CENTER_VERTICAL,
        )

        controls_sizer.Add(self.top_text_ctrl, 1, wx.EXPAND)

        controls_sizer.Add(
            wx.StaticText(self.panel, label="Текст снизу:"),
            0,
            wx.ALIGN_CENTER_VERTICAL,
        )

        controls_sizer.Add(self.bottom_text_ctrl, 1, wx.EXPAND)

        controls_sizer.Add(
            wx.StaticText(self.panel, label="Размер шрифта:"),
            0,
            wx.ALIGN_CENTER_VERTICAL,
        )

        controls_sizer.Add(self.font_size_ctrl, 1, wx.EXPAND)

        controls_sizer.Add(self.load_button, 1, wx.EXPAND)
        controls_sizer.Add(self.generate_button, 1, wx.EXPAND)

        controls_sizer.AddGrowableCol(1, 1)

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(self.save_button, 0, wx.RIGHT, 10)

        main_sizer.Add(
            controls_sizer,
            0,
            wx.ALL | wx.EXPAND,
            15,
        )

        main_sizer.Add(
            self.image_preview,
            1,
            wx.ALL | wx.EXPAND,
            15,
        )

        main_sizer.Add(
            button_sizer,
            0,
            wx.ALL | wx.CENTER,
            10,
        )

        self.panel.SetSizer(main_sizer)

    def _bind_events(self) -> None:
        self.load_button.Bind(wx.EVT_BUTTON, self.on_load_image)
        self.generate_button.Bind(wx.EVT_BUTTON, self.on_generate_meme)
        self.save_button.Bind(wx.EVT_BUTTON, self.on_save_meme)

    def on_load_image(self, _: wx.CommandEvent) -> None:
        with wx.FileDialog(
            self,
            message="Выберите изображение",
            wildcard=(
                "Image files (*.png;*.jpg;*.jpeg)|"
                "*.png;*.jpg;*.jpeg"
            ),
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
        ) as dialog:
            if dialog.ShowModal() == wx.ID_CANCEL:
                return

            try:
                path = dialog.GetPath()
                self.meme.load_image(path)

                self._display_image(self.meme.image)

                wx.MessageBox(
                    "Изображение успешно загружено.",
                    "Успех",
                    wx.OK | wx.ICON_INFORMATION,
                )

            except Exception as error:
                self._show_error(str(error))

    def on_generate_meme(self, _: wx.CommandEvent) -> None:
        try:
            self.generated_image = self.meme.generate(
                top_text=self.top_text_ctrl.GetValue(),
                bottom_text=self.bottom_text_ctrl.GetValue(),
                font_size=self.font_size_ctrl.GetValue(),
            )

            self._display_image(self.generated_image)

            wx.MessageBox(
                "Мем успешно создан.",
                "Успех",
                wx.OK | wx.ICON_INFORMATION,
            )

        except MemeGeneratorError as error:
            self._show_error(str(error))

    def on_save_meme(self, _: wx.CommandEvent) -> None:
        if self.generated_image is None:
            self._show_error("Сначала создайте мем.")
            return

        with wx.FileDialog(
            self,
            message="Сохранить мем",
            wildcard="PNG files (*.png)|*.png",
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,
        ) as dialog:
            if dialog.ShowModal() == wx.ID_CANCEL:
                return

            try:
                save_path = dialog.GetPath()

                self.generated_image.save(save_path)

                wx.MessageBox(
                    "Мем успешно сохранён.",
                    "Успех",
                    wx.OK | wx.ICON_INFORMATION,
                )

            except Exception as error:
                raise MemeSaveError(
                    f"Ошибка сохранения: {error}"
                ) from error

def _display_image(self, image: Optional[Image.Image]) -> None:
    if image is None:
        return

    preview = image.copy()
    preview.thumbnail(self.PREVIEW_SIZE)

    width, height = preview.size

    wx_image = wx.Image(width, height)
    wx_image.SetData(preview.convert("RGB").tobytes())

    bitmap = wx_image.ConvertToBitmap()

    self.image_preview.SetBitmap(bitmap)
    self.panel.Layout()


class MemeGeneratorApp(wx.App):
    """Приложение."""

    def OnInit(self) -> bool:
        MemeGeneratorFrame()
        return True


def main() -> None:
    app = MemeGeneratorApp()
    app.MainLoop()


if __name__ == "__main__":
    main()