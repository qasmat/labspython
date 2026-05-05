#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке
def run():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

    # посадите медведя (bear) между львом и кенгуру
    #  и выведите список на консоль
    zoo.insert(1,'bear')
    print(zoo)

    # добавьте птиц из списка birds в последние клетки зоопарка
    birds = ['rooster', 'ostrich', 'lark', ]
    #  и выведите список на консоль
    zoo.extend(birds)
    print(zoo)

    # уберите слона
    #  и выведите список на консоль
    zoo.remove('elephant')
    print(zoo)

    # выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
    # Номера при выводе должны быть понятны простому человеку, не программисту.
    lion_prizon = zoo.index('lion') + 1
    lark_prizon = zoo.index('lark') + 1
    print('Лев сидит в клетке номер', lion_prizon)
    print('Жаворонок сидит в клетке номер', lark_prizon)
