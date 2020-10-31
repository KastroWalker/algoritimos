#!/usr/bin/python
# -*- coding: utf-8 -*-

voters = int(input('Digite a quantidade de eleitores: '))

candidate1 = 0
candidate2 = 0
candidate3 = 0
blank = 0
null = 0

for i in range(voters):
    vote = int(input('''
\n Escolha um candidato para votar: 
====================================
1 - Candidato 1
2 - Candidato 2
3 - Candidate 3
0 - Branco
===================================
'''))

    if vote == 1:
        candidate1 += 1
    elif vote == 2:
        candidate2 += 1
    elif vote == 3:
        candidate3 += 1
    elif vote == 4:
        blank += 1
    else:
        null += 1

print(f'''\n
  Total de votos
==================
Candidato 1: {candidate1} votos
Candidato 2: {candidate2} votos
Candidato 3: {candidate3} votos
Branco: {null} votos
Nulo: {null} votos
''')

if candidate1 > (voters * 0.5):
    print(f'O candidato 1 foi vencedor com {candidate1} votos!')
elif candidate2 > (voters * 0.5):
    print(f'O candidato 2 foi vencedor com {candidate2} votos!')
elif candidate3 > (voters * 0.5):
    print(f'O candidato 3 foi vencedor com {candidate3} votos!')
else:
    print('A eleição vai ter segundo turno. Nenhum candidato conseguiu a quantidade de votos necessário')
