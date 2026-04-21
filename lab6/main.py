import tkinter as tk
from tkinter import messagebox
from premises.room import Room
from premises.apartment import Apartment

from docx import Document
from openpyxl import Workbook

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Расчёт помещений")

        self.apartment = Apartment()
        self.create_widgets()
        

    def create_widgets(self):
        # ввод
        tk.Label(text="Длина").grid(row=0, column=0)
        tk.Label(text="Ширина").grid(row=1, column=0)
        tk.Label(text="Высота").grid(row=2, column=0)

        self.length = tk.Entry()
        self.width = tk.Entry()
        self.height = tk.Entry()

        self.length.grid(row=0, column=1)
        self.width.grid(row=1, column=1)
        self.height.grid(row=2, column=1)

        # кнопки
        tk.Button(text="Добавить комнату", command=self.add_room).grid(row=3, column=0, columnspan=2)
        tk.Button(text="Рассчитать", command=self.calculate).grid(row=4, column=0, columnspan=2)
        tk.Button(text="Сохранить DOCX", command=self.save_docx).grid(row=5, column=0)
        tk.Button(text="Сохранить XLSX", command=self.save_xlsx).grid(row=5, column=1)

        # список комнат
        tk.Label(text="Список комнат").grid(row=0, column=2)
        self.room_listbox = tk.Listbox(width=40, height=10)
        self.room_listbox.grid(row=1, column=2, rowspan=5)

        # результат
        self.result = tk.Label(text="")
        self.result.grid(row=6, column=0, columnspan=3)

    def add_room(self):
        try:
            l = float(self.length.get())
            w = float(self.width.get())
            h = float(self.height.get())

            if l <= 0 or w <= 0 or h <= 0:
                raise ValueError

            room = Room(l, w, h)
            self.apartment.add_room(room)

            # добавляем в список
            index = len(self.apartment.rooms)
            self.room_listbox.insert(
                tk.END,
                f"Комната {index}: {l}x{w}x{h} | {room.area():.2f} м²"
            )

            messagebox.showinfo("OK", "Комната добавлена")

        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные положительные числа")

    def calculate(self):
        area = self.apartment.total_area()
        heat = self.apartment.total_heat()

        self.result.config(text=f"Площадь: {area:.2f} м²\nТепло: {heat:.2f} Вт")

    def save_docx(self):
        doc = Document()
        doc.add_heading("Отчёт", 0)

        for i, room in enumerate(self.apartment.rooms, 1):
            doc.add_paragraph(f"Комната {i}: {room.area():.2f} м²")

        doc.add_paragraph(f"Общая площадь: {self.apartment.total_area():.2f} м²")
        doc.add_paragraph(f"Тепловая мощность: {self.apartment.total_heat():.2f} Вт")

        doc.save("report.docx")

    def save_xlsx(self):
        wb = Workbook()
        ws = wb.active

        ws["A1"] = "Комната"
        ws["B1"] = "Площадь"

        for i, room in enumerate(self.apartment.rooms, 1):
            ws[f"A{i+1}"] = f"Комната {i}"
            ws[f"B{i+1}"] = room.area()

        ws["A10"] = "Итого"
        ws["B10"] = self.apartment.total_area()

        wb.save("report.xlsx")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()



