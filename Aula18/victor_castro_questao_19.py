#!/usr/bin/python
# -*- coding: utf-8 -*-

while True:
	user = input('Digite o seu nome: ')
	password = input('Digite a sua senha: ')

	if user != password:
		print('Usuário cadastrado')
		break
	else:
		print('O usuário e senha são iguais. Digite novamente!\n')