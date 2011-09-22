#@{}[]|\&<>

from numpy import sqrt
from PolException import *
from PolUtils import e1,e2

def quadRoot(A,B,C):
	if A!=0:
		A+=0j
		B+=0j
		C+=0j
		a1=(-B+sqrt(B**2-4*A*C))/2.
		a2=(-B-sqrt(B**2-4*A*C))/2.
		return a1,a2
	else:
		raise InvalidPol("No es un polinomio cuadratico")

def cubRoot(A=1,B=0,C=0,D=1):
	"""
	Rutina para obtener las tres raices complejas de un polinomio arbitrario
	"""
	if A!=0:
		a=(B+0j)/A
		b=(C+0j)/A
		c=(D+0j)/A

		p=(3*b-a**2)/3
		q=(2*a**3-9*a*b+27*c)/27

		aa,bb=quadRoot(1,q,-(p**3)/27)

		a0=(aa)**(1/3.)
		b0=(bb)**(1/3.)

		a1=a0*e1
		a2=a0*e2

		b1=b0*e1
		b2=b0*e2

		return (a0+b0-a/3),(a1+b2-a/3),(a2+b1-a/3)
	else:
		raise InvalidPol("No es un polinomio cubico")

"""
Rutina para obtener las raices de un polinomio cuadratico y cubico
"""
