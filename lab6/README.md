## Задание6.py
По своему варианту задания создайте пакет, содержащий 3 модуля, и подключите его к основной программе.
Основная программа должна предоставлять:
графический пользовательский интерфейс с возможностями ввода требуемых параметров и отображения результатов расчёта,
возможность сохранить результаты в отчёт формата .doc или .xls (например, пакеты python-docx и openpyxl).
Помещения:

Комната
Квартира
Многоэтажный дом
Расчёт общей площади помещения, тепловой мощности для обогрева помещения.
## Программа
## Модуль Room
```python
class Room:
    def __init__(self, length: float, width: float, height: float):
        self.length = length
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.length * self.width

    def volume(self) -> float:
        return self.area() * self.height

    def heat_power(self, k: float = 40) -> float:
        # k — удельная тепловая характеристика (Вт/м³)
        return self.volume() * k
````
## Модуль apartment
```python
from .room import Room

class Apartment:
    def __init__(self):
        self.rooms: list[Room] = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def total_area(self) -> float:
        return sum(room.area() for room in self.rooms)

    def total_heat(self) -> float:
        return sum(room.heat_power() for room in self.rooms)
```
## Модуль building
```python
from .apartment import Apartment

class Building:
    def __init__(self):
        self.apartments: list[Apartment] = []

    def add_apartment(self, apartment: Apartment):
        self.apartments.append(apartment)

    def total_area(self) -> float:
        return sum(a.total_area() for a in self.apartments)

    def total_heat(self) -> float:
        return sum(a.total_heat() for a in self.apartments)
```
## Главный модуль main
```python
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
```
## Результат программмы

<img width="630" height="249" alt="image" src="https://github.com/user-attachments/assets/9c51af2c-e538-497c-9c2b-b9a8c6b31894" />

## Описание проделанной работы

В работе была создана программа на Python с графическим интерфейсом с использованием Tkinter.

Был разработан пакет `premises`, который состоит из трёх модулей:

* `room.py` — описание комнаты и расчёт её площади и тепловой мощности;
* `apartment.py` — объединение нескольких комнат и расчёт общих значений;
* `building.py` — объединение квартир в дом.

В основной программе реализован интерфейс, позволяющий:

* вводить размеры комнаты;
* добавлять комнаты в список;
* рассчитывать общую площадь и тепловую мощность;
* отображать добавленные помещения.

Также добавлена возможность сохранения результатов:

* в файл `.docx` с помощью python-docx;
* в файл `.xlsx` с помощью openpyxl.

В ходе работы использовался объектно-ориентированный подход, что позволило удобно разделить логику программы.

[tkinter](https://metanit.com/python/tkinter/)



