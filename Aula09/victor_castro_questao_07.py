#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    Leia a idade de uma pessoa em dias e informe-a em anos, meses e dias. Considerar que 1 ano tem 365 dias e 1 mês tem 30 dias.
"""

age_day = int(input('Digite sua idade em dias: '))

years = age_day // 365
days = age_day % 365

months = age_day // 30
days %= 30

print(f"""
A idade informada é equivalente a
{years} {"ano" if years == 1 else "anos"}
{months} {"mês" if months == 1 else "meses"}
{days} {"dia" if days == 1 else "dias"}
""")
