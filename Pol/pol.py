"""
General routine for working with polinomial expressions.
"""

from PolException import *

class Pol(tuple):
	def __init__(self,pattern):
		"""
		Crea un nuevo polinomio segun el patron dado, pattern debe ser una lista
		de la forma:

			[4,2,34,0,12] o bien (4,2,34,0,12)

		donde el elemento en la posicion k es el coeficiente de x con el exponente k,
		"""
		self.__type__ = 'pol'
		if type(pattern)!=list and type(pattern)!=tuple :
			raise InvalidArgumentException("No puedo construir un polinomio con este argumento")
	def grad(self):
		if self != (0,):
			return len(self)-1
		else:
			return None
	def __add__(self,y):
		if type(y)==int or type(y)==long or type(y)==float or type(y)==complex :
			y = (y,)
		if type(y)==tuple or type(y)==list or type(y)==Pol:
			p=range(max(len(y),len(self)))
			for i in p:
				p[i]=0
				if i<min(len(y), len(self)):
					p[i]+=y[i]+self[i]
				else:
					if len(y) < len(self):
						p[i]+=self[i]
					else:
						p[i]+=y[i]
			if p:
				n=len(self)
				for i in range(len(p)):
					if p[len(p)-i-1]!=0:
						break
					else:
						n-=1
				p=p[0:n]
				if p:
					return Pol(p)
				else:
					return Pol((0,))
			else:
				return Pol((0,))
		else:
			raise UnsupportedOperator("La suma esta definida entre polinomios")
	def __radd__(self,y):
		return self.__add__(y)
	def __mul__(self,y):
		if type(y)==list or type(y)==tuple or type(y)==Pol:
			p = list()
			for i in range(len(y)*len(self)-1):
				p.append(0)
			for i in range(len(self)):
				for j in range(len(y)):
					p[i+j] += self[i]*y[j]
			return Pol(p)
		else:
			if  type(y)==int or type(y)==long or type(y)==float or type(y)==complex :
				p = list()
				for i in self:
					p.append(i*y)
				return Pol(p)
			else:
				raise UnsupportedOperator("El producto esta definida entre polinomios")
	def __rmul__(self,y):
		return self.__mul__(y)
	def __neg__(self):
		return self*-1
	def __sub__(self,y):
		return self+(-y)
	def __rsub__(self,y):
		return y+self.__neg__()
	def __pow__(self,y):
		if type(y)==int or type(y)==long :
			if y>=0:
				if y==0:
					return Pol((1,))
				else:
					s = 1
					for i in range(y):
						s*=self
					return s
			else:
				raise UnsupportedOperator("Usando un exponente invalido")
		else:
			raise UnsupportedOperator("Usando un exponente invalido")
	def __call__(self,x):
		s = 0
		for i in range(len(self)):
			s += self[i]*(x**i)
		return s
