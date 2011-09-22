#@{}[]|\&<>

import re

def comb(cad,pr=list()):
	if len(cad)>1:
		for i in range(len(cad)):
			c=pr+[cad[i]]
			comb(cad[0:i]+cad[i+1:len(cad)] , c)
	else:
		pr+=cad
		print pr

if __name__=="__main__":
	x=['jo','ma','lu','ce']
	comb(x)
