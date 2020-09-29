#!/usr/bin/python
# -*- coding: utf-8 -*-

number_init = int(input('Digite o primeiro número da sequência: '))
number_end = int(input('Digite o primeiro último da sequência: '))

if number_init == number_end:
    print('Os números são iguais')
elif number_init < number_end:
    for x in range(number_init + 1, number_end):
        print(x)
else:
    for x in range(number_init - 1, number_end, -1):
        print(x)
