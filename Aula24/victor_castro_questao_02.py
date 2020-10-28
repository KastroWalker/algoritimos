#!/usr/bin/python
# -*- coding: utf-8 -*-

numbers = []
total_multiplication = 1
total_sum = 0

for i in range(5):
    number = float(input(f'Digite o {i + 1}º número: '))

    total_multiplication *= number
    total_sum += number

    numbers.append(number)

print(f'\nA soma dos número é: {total_sum}')
print(f'\nA multiplicação dos número é: {total_multiplication}')
print('\nOs números são: ')

for i in range(len(numbers)):
    print(f'{i + 1}º número: {numbers[1]}')
