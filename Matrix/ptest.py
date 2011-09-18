#@{}[]|\&<>

from subprocess import Popen,PIPE

out = Popen(["java", "Prueba"], stdout=PIPE,shell=True).communicate()[0]
print out
