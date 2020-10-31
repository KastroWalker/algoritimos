#!/usr/bin/python
# -*- coding: utf-8 -*-

consumption = float(input('Digite o consumo: '))

rate = 0.15
price = (consumption * 0.25) * rate

print(f'O valor a ser pago é: {price}')
