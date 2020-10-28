#!/usr/bin/python
# -*- coding: utf-8 -*-

amount_notes = int(input('Digite a quantidade de notas: '))
total_notes = 0
media = 0
notes = []

for i in range(amount_notes):
    note = float(input(f'Digite a {i+1}º nota: '))

    total_notes += note
    notes.append(note)

media = total_notes / amount_notes

print(f'\nA média de notas é: {media}')
print('\nAs notas são: ')

for i in range(len(notes)):
    print(f'nota {i + 1}: {notes[i]}')
