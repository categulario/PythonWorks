from numpy.random import random_integers,shuffle

letras=['Q','W','E','R','T','Y','U','I']
victoria=False
nombre=None

def intro():
    print 'Bienvenido a mente maestra'
    print 'Este juego retara tus conocimientos, estas listo?'
    print 'Comencemos, escoje un nivel:'
    print 'A- Sencillo B- Medio C- Mortal'
def instrucciones():
    print 'Instrucciones:'
    print '\tDebes adivinar las letras (en orden) que esconde el programa'
    print '\tSi el nivel es A(Sencillo) solo pueden ser Q,W,E o R'
    print '\tSi el nivel es B(Medio) pueden ser Q,W,E,R,T o Y'
    print '\tSi el nivel es C(Mortal) pueden ser Q,W,E,R,T,Y,U o I'
    print
    print 'Jugar'
    print '\tPara adivinar las letras (insisto, en orden) que la maquina esconde, es necesario escribir una combinacion de estas letras a 4 casillas, por ejemplo: QERT'
    print '\tEl sistema devolvera como respuesta una B por cada letra correcta y una M por cada letra correcta que ademas este en su lugar'
    print '\tNotese que la respuesta no sera devuelta en orden'
def main():
    global victoria
    global nombre
    global letras
    guess=list()
    print 'Tu nombre:'
    nombre=raw_input()
    intro()
    op=raw_input()
    while(op!='A' and op!='B' and op!='C'):
        print 'Opcion invalida, debe ser A,B o C'
        op=raw_input()
    if(op=='A'):
        for i in range(0,4):
            guess.append(letras[random_integers(4)-1])
    elif(op=='B'):
        for i in range(0,4):
            guess.append(letras[random_integers(6)-1])
    else:
        for i in range(0,4):
            guess.append(letras[random_integers(8)-1])
    instrucciones()
    print 'Comencemos'
    print '0,0,0,0'
    while(True):
        aciertos=list()
        entrada=list(raw_input())
        while(len(entrada)<4):
            entrada.append('X')
        matched=[False,False,False,False]
        gmatched=[False,False,False,False]
        if(entrada==guess):
            victoria=True
            break
        else:
            for i in range(0,4):
                if(entrada[i]==guess[i]):
                    aciertos.append('M')
                    matched[i]=True
                    gmatched[i]=True
            for i in range(0,4):
                if(not matched[i]):
                    for j in range(0,4):
                        if(not gmatched[j]):
                            if(entrada[i]==guess[j]):
                                aciertos.append('B')
                                matched[i]=True
                                gmatched[j]=True
                                break
        shuffle(aciertos)
        print aciertos
    if(victoria):
        print nombre+' ha ganado!'
    else:
        print 'Nooooo!!'

if __name__=='__main__':
    main()
