#<>{}[]|\

from exception import *

class Pol(tuple):
	def __init__(self,pattern):
		"""
		Crea un nuevo polinomio segun el patron dado, pattern debe ser una lista
		de la forma:

			[4,2,34,0,12]

		donde el elemento en la posicion k es el coeficiente de x con el exponente k
		"""
		if type(pattern)!=list and type(pattern)!=tuple:
			raise InvalidArgumentException("No puedo construir un polinomio con este argumento")

	def __add__(self,y):
		
