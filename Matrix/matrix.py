#@{}[]|\&<>

from numpy.random import random_integers
from exception import *

def producto(A,B):
	"""
	Define el producto entre matrices haciendo la validacion correspondiente
	Dada una matriz A de mxn y una matriz B de nxp devuelve el producto
	AxB

	El producto tambien esta definido para un escalar por la izquierda
	"""
	if not esMatriz(B):
		raise MatrixProductError("El producto escalar solo esta definido por la izquierda")
	if esMatriz(A):
		if A.columnas==B.filas:
			M=list()
			B.trasponer()
			m=0
			for i in A.matriz:
				M.append(list())
				for j in B.matriz:
					r=0  #Almacena el valor del producto de las casillas correspondientes
					for k in range(len(i)):
						r+=i[k]*j[k]
					M[m].append(r)
				m+=1
			return Matriz().crear(M)
		else:
			raise MatrixProductError("Estas matrices no cumplen lo necesario para el producto")
	else:
		M=list()
		m=0
		for i in B.matriz:
			M.append(list())
			for j in i:
				M[m].append(j*A)
			m+=1
		return Matriz().crear(M)

def suma(A,B):
	"""
	Define la suma para dos matrices de cualesquiera tamanios casilla a casilla
	"""
	if esMatriz(A) and esMatriz(B):
		M=list()
		m=0
		# Creamos primero una matriz de ceros del tamanio adecuado
		for i in range(max(A.filas,B.filas)):
			M.append(list())
			for j in range(max(A.columnas,B.columnas)):
				M[m].append(0)
			m+=1
		# Agregamos luego los elementos de cada matriz
		ii=0
		for i in A.matriz:
			jj=0
			for j in i:
				M[ii][jj]+=j
				jj+=1
			ii+=1
		ii=0
		for i in B.matriz:
			jj=0
			for j in i:
				M[ii][jj]+=j
				jj+=1
			ii+=1
		return Matriz().crear(M)
	else:
		raise MatrixAddError("La suma de matrices solo esta definida para matrices!")

def esMatriz(A):
	"""
	Identifica si el objeto A es una matriz u otra cosa
	"""
	try:
		if type(A)==Matriz:
			return True
		else:
			return False
	except AttributeError:
		return False

class Matriz(object):
	"""
	Define la clase Matriz con la informacion sobre filas, columnas y la lista rectangular
	que la define

	El constructor recibe como parametros opcionales el numero de filas
	y el numero de columnas, ademas si el tercer algumento es True, crea una matriz
	identidad con las dimensiones dadas (de ser posible). Si no es posible construir 
	la matriz identidad entonces devuelve un error IdentityError
	"""

	def __init__(self,filas=10,columnas=10,tipo='rand'):
		"""
		Inicializa el objeto Matriz a partir de la informacion dada.

		filas		-> el numeor de filas
		columnas 	-> el numero de columnas
		identidad	-> establece una matriz identidad (Si es False agrega valores aleatorios)
		"""
		if tipo=='rand':
			self.filas=filas
			self.columnas=columnas
			m=list()
			for i in range(filas):
				m.append(list())
				for j in range(columnas):
					m[i].append(random_integers(21)-11)
			self.matriz=m
			self.__type__='matriz'			
		elif tipo=='identidad':
			if filas==columnas:
				self.filas=filas
				self.columnas=columnas
				m=list()
				for i in range(filas):
					m.append(list())
					for j in range(columnas):
						if i==j:
							m[i].append(1)
						else:
							m[i].append(0)
				self.matriz=m
				self.__type__='matriz'
			else:
				raise IdentityError('La matriz identidad debe ser cuadrada')
		else:
			self.filas=filas
			self.columnas=columnas
			m=list()
			for i in range(filas):
				m.append(list())
				for j in range(columnas):
					m[i].append(tipo)
			self.matriz=m
			self.__type__='matriz'

	def __nonzero__(self):
		if self.columnas==0:
			return False
		nonZero=False
		for i in self.matriz:
			for j in i:
				if j!=0:
					nonZero=True
					break
		return nonZero

	def __len__(self):
		"""
		Devuelve la longitud de la matriz, es decir, el producto del numero de filas
		con el numero de columnas
		"""
		return self.filas*self.columnas

	def __mlen__(self):
		"""
		Devuelve una tupla de dos elementos con las dimenciones de la matriz.

		Si A es una matriz mxn devuelve (m,n)
		"""
		return self.filas,self.columnas

	def len(self):
		return self.__mlen__()

	def __add__(self,x):
		"""
		Define la suma de una matriz con otra
		"""
		return suma(x,self)

	def __neg__(self):
		"""
		Define el inverso aditivo de una matriz determinada
		"""
		M=list()
		m=0
		for i in range(self.filas):
			M.append(list())
			for j in range(self.columnas):
				M[m].append(-self.matriz[i][j])
			m+=1
		return Matriz().crear(M)

	def __sub__(self,x):
		return self+(-x)

	def __rmul__(self,x):
		"""
		Define el producto por la izquierda de un escalar con una matriz usando 
		el operador *
		"""
		return producto(x,self)

	def __mul__(x,self):
		"""
		Define el producto por la derecha de una matriz con otra matriz, evaluando siempre
		que se cumplan las condiciones necesarias
		"""
		return producto(x,self)

	def __str__(self):
		"""
		Devuelve la representacion en texto de la matriz de la siguiente forma:
		
		Matriz mxn
		[[a1,...,an], [b1,...,bn],...,[p1,...,pn]]
		"""
		s="["
		k=0
		for i in self.matriz:
			if k==0:
				s+=str(i)
			else:
				s+=" "+str(i)
			if k!=len(self.matriz)-1:
				s+=",\n"
			k+=1
		return "Matriz "+str(self.filas)+"x"+str(self.columnas)+"\n"+s+"]"

	def traspuesta(self):
		"""
		Devuelve la traspuesta de la matriz actual
		"""
		M=list()
		for i in self.matriz[0]:
			M.append(list())
		for i in range(len(self.matriz)):
			for j in range(len(self.matriz[0])):
				M[j].append(self.matriz[i][j])
		ma=Matriz()
		ma.crear(M)
		return ma

	def trasponer(self):
		"""
		Traspone la matriz actual sin devolver ningun resultado
		"""
		M=list()
		for i in self.matriz[0]:
			M.append(list())
		for i in range(len(self.matriz)):
			for j in range(len(self.matriz[0])):
				M[j].append(self.matriz[i][j])
		self.matriz=M

	def crear(self,matriz):
		"""
		Crea un objeto de la clase Matriz dada una lista rectangular de elementos

		recibe como unico argumento una lista bidimencional con objetos de cualquier
		tipo, por ejemplo:

		x=[[a1,...,an],...,[p1,...,pn]]
		M=Matriz.crear(x)

		Se crea una matriz con entradas a1,a2,...,an sucesivamente
		"""
		if type(matriz)==list and type(matriz[0]==list):
			valid=True
			lenght=len(matriz[0])
			for i in matriz:
				if len(i)!=lenght:
					valid=False
					break
			if valid:
				self.matriz=matriz
				self.filas=len(matriz)
				self.columnas=len(matriz[0])
				self.__type__='matriz'
				
				return self
			else:
				raise NotAValidMatrix("No es una matriz valida")
		else:
			raise NotAValidMatrix("No es una matriz valida")




"""
Esta clase y metodos incluidos son parte de las rutinas comunes encontradas al momento de 
utilizar matrices.
Cualquier aportacion es bien recibida
"""
