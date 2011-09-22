#<>{}[]|\

from raices import *

print "Te voy a calcular las raices de un polinomio de coeficientes complejos"
print "arbitrarios"
print

while True:
	x=input("Quieres un polinomio cuadratico [1] o cubico [2]: ")

	if x==2:
		A=input("Dame el coeficinte cubico: ")
		B=input("Dame el coeficinte cuadratico: ")
		C=input("Dame el coeficinte lineal: ")
		D=input("Dame el termino independiente: ")

		print cubRoot(A,B,C,D)
	else:
		A=input("Dame el coeficinte cuadratico: ")
		B=input("Dame el coeficinte lineal: ")
		C=input("Dame el termino independiente: ")

		print quadRoot(A,B,C)

	x=raw_input("Quieres otro resultado? [Si]/No: ")

	if (x=='Si' or not x) and not (x=='no' or x=='No' or x=='nO' or x=='NO'):
		continue
	else:
		break

print "Bye"
print
