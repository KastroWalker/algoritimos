#!/usr/bin/python
# -*- coding: utf-8 -*-

total_age = 0
teens = 0
adults = 0
seniors = 0

total_peoples = int(input('Digite a quantidade de pessoas da turma: '))

for i in range(total_peoples):
    while True:
        age = int(input(f'Digite a idade da {i + 1}º pessoa: '))
        
        if 0 < age < 100:
            total_age += age

            if age < 26:
                teens += 1
            elif age < 61:
                adults += 1
            else:
                seniors += 1

            break
        else:
            print('A idade dever se maior que 0 e menor que 100. Digite novamente!\n')

media_age = total_age / total_peoples

print('===================================')
print(f'\nA média de idade é {media_age}\n')

if media_age < 26:
    print('A turma é jovem!')
elif media_age < 61:
    print('A turma é adulta!')
else:
    print('A turma é idosa!')

print(f'''
A turma possui:
{teens} jovens
{adults} adultos
{seniors} idosos
''')

