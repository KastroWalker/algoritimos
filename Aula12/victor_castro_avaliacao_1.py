#!/usr/bin/python
# -*- coding: utf-8 -*-

value = float(input('Digite o valor que deseja sacar: '))

fifty_notes = int(value // 50)
rest = value % 50

twenty_notes = int(rest // 20)
rest = rest % 20

ten_notes = int(rest // 10)

print(f"""Sacando: 
{fifty_notes} notas de 50
{twenty_notes} notas de 20
{ten_notes} notas de 10""")
