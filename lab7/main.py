
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox
)

from paket import Room, Apartment, Building

class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Многоэтажный дом")

        self.building = Building()
        self.current_apartment = Apartment()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # ввод
        input_layout = QHBoxLayout()

        self.length = QLineEdit()
        self.width = QLineEdit()
        self.height = QLineEdit()

        self.length.setPlaceholderText("Длина")
        self.width.setPlaceholderText("Ширина")
        self.height.setPlaceholderText("Высота")

        input_layout.addWidget(self.length)
        input_layout.addWidget(self.width)
        input_layout.addWidget(self.height)

        layout.addLayout(input_layout)

        # кнопки
        btn_layout = QHBoxLayout()

        add_btn = QPushButton("Добавить комнату")
        add_btn.clicked.connect(self.add_room)

        new_apt_btn = QPushButton("Новая квартира")
        new_apt_btn.clicked.connect(self.new_apartment)

        calc_btn = QPushButton("Рассчитать дом")
        calc_btn.clicked.connect(self.calculate)

        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(new_apt_btn)
        btn_layout.addWidget(calc_btn)

        layout.addLayout(btn_layout)

        # списки
        lists_layout = QHBoxLayout()

        self.room_list = QListWidget()
        self.apartment_list = QListWidget()

        lists_layout.addWidget(self.room_list)
        lists_layout.addWidget(self.apartment_list)

        layout.addLayout(lists_layout)

        # результат
        self.result = QLabel("")

        layout.addWidget(self.result)

        self.setLayout(layout)

    def add_room(self):
        try:
            l = float(self.length.text())
            w = float(self.width.text())
            h = float(self.height.text())

            if l <= 0 or w <= 0 or h <= 0:
                raise ValueError

            room = Room(l, w, h)
            self.current_apartment.add_room(room)

            self.room_list.addItem(str(room))

        except ValueError:
            QMessageBox.critical(self, "Ошибка", "Введите корректные числа")

    def new_apartment(self):
        if len(self.current_apartment) == 0:
            QMessageBox.warning(self, "Ошибка", "Нет комнат")
            return

        self.building.add_apartment(self.current_apartment)

        self.apartment_list.addItem(
            f"Квартира {len(self.building)}: {self.current_apartment.total_area():.1f} м²"
        )

        self.current_apartment = Apartment()
        self.room_list.clear()

    def calculate(self):
        area = self.building.total_area()
        heat = self.building.total_heat()

        self.result.setText(f"Дом: {area:.1f} м² | {heat:.1f} Вт")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())




