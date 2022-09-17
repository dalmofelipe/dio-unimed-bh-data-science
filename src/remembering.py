#!/bin/bash python3


class Pokemon:
	"""docstring for Pokemon"""
	def __init__(self, name, type, power):
		self.name = name
		self.type = type
		self.power = power

	def __str__(self):
		name, type, power = vars(self).values()
		return "{0} é um pokemon do tipo {1} e tem o poder de {2}, por isso me chamo {0}.".format(
			'.'.join([*name.upper()]), 
			type.lower(), 
			power.lower()
		)


def run():
	dito = Pokemon('Dito', 'Normal', 'Copiar poderes de outro pokem')
	my_dic = {}
	my_dic['chave_a'] = 'uma string valor a'
	my_dic['chave_b'] = 34

	print(dito)
	print(my_dic, type(my_dic))

	print('Chaves do dicionário: ', my_dic.keys())
	print('Valosres das chaves: ', my_dic.values())

	a = 1000
	b = 1000.00001
	c = 1000

	print('a e b apontam para o mesmo espaço de memoria' if a is b else 'a e b não compartilham memoria')
	if a is c: print('a e c compartilham mesmo espaço de memoria')
	# print(a is not b)

	distancia = 20
	x = 10
	y = 20

	if (distancia <= 0 or distancia >= 10000) or (x <= 0 and x >= 100) or (y <= 0 and y >= 100):
		return

	icm = distancia / (x + y)
	print(f"{icm:.2}")


if __name__ == '__main__':
	run()
