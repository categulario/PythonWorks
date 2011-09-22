#<>{}[]|\

class InvalidArgumentException(Exception):
	"""
	Error de argumento invalido para un plinomio
	"""
	def __init__(self,msg):
		self.msg=msg

	def __str__(self):
		return self.msg
