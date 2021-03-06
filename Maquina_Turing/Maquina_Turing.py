def Maquina_Turing (estado = None, #estados de la maquina de turing
                   blanco = None, # simbolo blanco de el alfabeto de la cinta
                   reglas = [], #reglas de transicion
                   cinta = [], 
                   final = None, #estado valido y/o final 
                   posicion = 0): #posicion siguiente de la maquina

    st = estado
    #seguridad prevenir errores
    if not cinta: cinta = [blanco]
    if posicion < 0 : posicion += len(cinta)
    if posicion >= len(cinta) or posicion < 0 : raise Error ("Se inicializo mal la posicion")
    
    reglas = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in reglas)
    """
Estado	 Símbolo leído	  Símbolo escrito	    Mov. 	  Estado sig.
p(s0)	      1(v0)	          x(v1)            R(dr)	     p(s1)
"""
    while True:
        print (st, '\t', end = " ")
        for i, v in enumerate(cinta):
            if i == posicion: print ("[%s]"%(v,),end=" ")
            else: print (v,end=" ")
        print()

        if st == final : break
        if (st, cinta[posicion]) not in reglas : break

        (v1,dr,s1) = reglas [(st, cinta[posicion])]
        cinta[posicion] = v1 # rescribe el simbolo de la cinta
    
    #movimeinto del cabezal
        if dr == 'left': #izquierda
            if posicion > 0 : posicion -= 1#pocision del numero dentro de la regla
            else: cinta.insert(0, blanco) #el numero va primero despues del recorrido se pone un numero en blanco o nulo
        if dr == 'right': #derecha
            posicion += 1 
            if posicion >= len(cinta): cinta.append(blanco)
        st = s1



print()
print("Maquina de turing")
print("suma 1 al valor binario ejemplo: entrada 111=7 salida 1000=8")
caracter = input("Ingrese el numero en binario: ")#ingreso de numeros
print("Resultado:")
Maquina_Turing (estado = 's1',#estado inicial 
                blanco = 'b',#bariable que deja en blanco la cinta 
                cinta = list(caracter),#entrada del caracter
                final = 's3',#estado de aceptacion 
                reglas = map(tuple,#reglas de la transcicion del resultado
                            [
                            "s1 1 1 right s1".split(),#derecha
                            "s1 0 0 right s1".split(),#derecha
                            "s1 b b left s2".split(),#izquierda
                            "s2 1 0 left s2".split(),#izquierda
                            "s2 0 1 right s3".split(),#derecha
                            "s2 0 1 left s3".split(),#izquierda
                            "s2 b 1 left  s3".split(),#izquierda
                            ]   
                            )
                )             



               