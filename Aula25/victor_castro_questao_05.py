#!/usr/bin/python
# -*- coding: utf-8 -*-

numbers = []
counter = 1

while True:
    number = float(input(f'Digite o {counter}º número: '))
    
    if number == 0:
        break

    numbers.append(number)

    counter += 1

for number in numbers:
    print(number)
