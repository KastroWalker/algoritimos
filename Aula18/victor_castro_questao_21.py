#!/usr/bin/python
# -*- coding: utf-8 -*-

higher = 0

for i in range(5):
    number = float(input('Digite um número: '))

    if number > higher:
        higher = number

print(f'O maior número é {number}')