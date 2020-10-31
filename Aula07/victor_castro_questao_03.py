#!/usr/bin/python
# -*- coding: utf-8 -*-

seconds = int(input('Digite o tempo em segundos: '))

hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
seconds %= 60

print(f'O evento vai durar {hours} hora(s) {minutes} minuto(s) e {seconds} segundo(s)')
