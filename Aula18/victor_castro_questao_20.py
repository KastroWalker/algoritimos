#!/usr/bin/python
# -*- coding: utf-8 -*-

populationA = 80000
populationB = 200000
years = 0

while populationA != populationB:
	populationA *= 0.03
	populationB *= 0.01
	years += 1

print(f'Levou {years} anos para as populações ficarem iguas.')