#@{}[]|\&<>

class InvalidPol(Exception):
	"""
	Se arroja cuando el usuario crea un polinomio invalido
	"""
	def __init__(self,msg):
		self.msg=msg
	def __str__(self):
		return self.msg
