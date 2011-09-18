#@{}[]|\&<>

class MatrixProductError(Exception):
        """
        Excepcion para el producto indefinido de matrices
        """
	def __init__(self, valor):
		self.valor = valor

	def __str__(self):
		return str(self.valor)


class IdentityError(Exception):
	def __init__(self, valor):
		self.valor = valor

	def __str__(self):
		return str(self.valor)


class NotAValidMatrix(Exception):
	def __init__(self, valor):
		self.valor = valor

	def __str__(self):
		return str(self.valor)

class MatrixAddError(Exception):
	def __init__(self,valor):
		self.valor = valor

	def __str__(self):
		return str(self.valor)


# Errores comunes en la operacion con matrices
