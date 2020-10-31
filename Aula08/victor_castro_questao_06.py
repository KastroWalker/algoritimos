#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime

date = datetime.now()

age = int(input('Digite sua idade: '))
future_year = int(input('Digite o ano que deseja saber a idade: '))

future_age = age + (future_year - date.year)

print(f'Em {future_year} você vai ter {future_age} anos')