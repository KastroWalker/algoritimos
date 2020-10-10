#!/usr/bin/python
# -*- coding: utf-8 -*-

number = int(input('Digite um número: '))

isPrimo = True

if number % 2 == 0 and number != 2:
    isPrimo = False
else:
    for x in range(1, number):
        if number % x == 0 and x != 1:
            isPrimo = False
        
if isPrimo:
    print(f'{number} é primo!')
else:
    print(f'{number} não é primo!')
