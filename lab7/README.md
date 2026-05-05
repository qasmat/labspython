## Задание 7.py
Перепишите свой вариант ЛР №6 с использованием классов и объектов. Задание то же, вариант GUI фреймворка возьмите следующий по списку. Для успешной сдачи в коде должны присутствовать:

использование абстрактного базового класса и соотвествующих декораторов для методов,
иерархия наследования,
managed - атрибуты,
минимум 2 dunder-метода у каждого класса.

## Программа
## Абстракный класс base
```python
from abc import ABC, abstractmethod

class BasePremise(ABC):
    @abstractmethod
    def total_area(self) -> float:
        pass

    @abstractmethod
    def total_heat(self) -> float:
        pass

    def __str__(self):
        return f"Area: {self.total_area():.2f}, Heat: {self.total_heat():.2f}"

    def __repr__(self):
        return f"<{self.__class__.__name__}>"
  ````
## Класс Room
````python
from .base import BasePremise

class Room(BasePremise):
    def __init__(self, length: float, width: float, height: float):
        self._length = length
        self._width = width
        self._height = height

    # managed attributes
    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def total_area(self) -> float:
        return self.length * self.width

    def volume(self) -> float:
        return self.total_area() * self.height

    def total_heat(self) -> float:
        return self.volume() * 40

    def __str__(self):
        return f"Room {self.length}x{self.width}x{self.height}"

    def __repr__(self):
        return f"Room({self.length}, {self.width}, {self.height})"
  ````

  ## Класс apartment
  ````python
  from .base import BasePremise
from .room import Room

class Apartment(BasePremise):
    def __init__(self):
        self._rooms: list[Room] = []

    @property
    def rooms(self):
        return self._rooms

    def add_room(self, room: Room):
        self._rooms.append(room)

    def total_area(self) -> float:
        return sum(r.total_area() for r in self.rooms)

    def total_heat(self) -> float:
        return sum(r.total_heat() for r in self.rooms)

    def __len__(self):
        return len(self.rooms)

    def __str__(self):
        return f"Apartment with {len(self)} rooms"

    def __repr__(self):
        return f"Apartment({len(self)} rooms)"
  ````
  ## Класс building
  ````python
from .base import BasePremise
from .apartment import Apartment

class Building(BasePremise):
    def __init__(self):
        self._apartments: list[Apartment] = []

    @property
    def apartments(self):
        return self._apartments

    def add_apartment(self, apartment: Apartment):
        self._apartments.append(apartment)

    def total_area(self) -> float:
        return sum(a.total_area() for a in self.apartments)

    def total_heat(self) -> float:
        return sum(a.total_heat() for a in self.apartments)

    def __len__(self):
        return len(self.apartments)

    def __str__(self):
        return f"Building with {len(self)} apartments"

    def __repr__(self):
        return f"Building({len(self)} apartments)"
  ````
  ## __init__
  ```python
  from .room import Room
from .apartment import Apartment
from .building import Building

__all__ = ["Room", "Apartment", "Building"]
````
## Главная программа main
```python

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
````
## Результат программы
<img width="539" height="342" alt="image" src="https://github.com/user-attachments/assets/dc397908-7a33-4043-a0bf-69c61f0d38df" />

## Описание проделанной работы
В работе была реализована программа на Python с графическим интерфейсом с использованием PyQt5.

Был создан пакет paket, включающий модули room, apartment, building, а также base, в котором реализован абстрактный базовый класс BasePremise.

Класс BasePremise задаёт общий интерфейс для всех типов помещений с помощью абстрактных методов total_area() и total_heat(). От него наследуются классы Room, Apartment и Building, что формирует иерархию наследования.

В классах используются managed-атрибуты (@property) для работы с данными, а также реализованы специальные методы (__str__, __repr__, __len__).

Графический интерфейс позволяет вводить параметры помещений, формировать квартиры и дом, а также выполнять расчёты.

[PyQt5](https://progpython.ru/stati/prochee/8185/polnoe-rukovodstvo-po-pyqt5-dokumentatsiya-na-russkom-yazyke/)
