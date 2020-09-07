#!/usr/bin/python
# -*- coding: utf-8 -*-

days = int(input('Digite a quantidade de dias: '))
distance = float(input('Digite a distância percorrida: '))

price = (days * 70) + (distance * 0.5)

print(f'O valor a ser pago é: R${price}')
