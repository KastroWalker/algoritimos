#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime

date = datetime.now()

year_of_birth = int(input('Digite o seu ano de nascimento: '))

age = date.year - year_of_birth

print(f'A idade é: {age} anos')