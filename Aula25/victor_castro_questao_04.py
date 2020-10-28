#!/usr/bin/python
# -*- coding: utf-8 -*-

numbers = []

for i in range(10):
    number = float(input(f'Digite o {i+1}º número: '))
    numbers.append(number)

for number in numbers:
    print(number)