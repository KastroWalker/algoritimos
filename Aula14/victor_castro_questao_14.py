#!/usr/bin/python
# -*- coding: utf-8 -*-

day = int(input('Digite o dia: '))
month = int(input('Digite o mês: '))
year = int(input('Digite o ano: '))

if day < 0:
    print('Dia invalido. Dia negativo não é válido.')
elif day > 31:
    print('Dia invalido. Dia maior que 31 não é válido.')
elif month < 0:
    print('Mês inválido. Mês negativo não é válido.')
elif month > 12:
    print('Mês inválido. Mês maior que 12 não é válido.')
elif year < 0:
    print('Ano inválido. Ano não pode ser negativo')
else:
    print('Data válida')
