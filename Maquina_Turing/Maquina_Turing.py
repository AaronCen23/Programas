def Maquina_Turing (
    estado = None, 
    blanco = None,
    reglas = [], 
    cinta = [], 
    final = None,
    asignacion = 0):

    st = estado
  
    if not cinta: cinta = [blanco]
    if asignacion < 0 : asignacion += len(cinta)
    if asignacion >= len(cinta) or asignacion < 0 : raise print ("Error de posición")

    reglas = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in reglas)
    
    while True:
        print (st, '\t', end = " ")
        for i, v in enumerate(cinta):
            if i == asignacion: print ("[%s]"%(v,),end=" ")
            else: print (v,end=" ")
        print()

        if st == final : break
        if (st, cinta[asignacion]) not in reglas : break

        (v1,dr,s1) = reglas [(st, cinta[asignacion])]
        cinta[asignacion] = v1
    
 
        if dr == 'L': #LEFT(Izquierda)
            if asignacion > 0 : asignacion -= 1
            else: cinta.insert(0, blanco)
        if dr == 'R': #Right(derecha)
            asignacion += 1
            if asignacion >= len(cinta): cinta.append(blanco)
        st = s1

print()
print()
print("Ejercicio de Turing") 
print()
print("Resultados:")
Maquina_Turing (estado = 'q0', 
              blanco= 'x',
              cinta = list("111"),
              final = 'q2',
              reglas = map(tuple,
                          [
                          "q0 x x R q0".split(),
                          "q0 1 1 R q0".split(),
                          "q0 x x L q1".split(),
                          "q1 1 x L q1".split(),
                          "q1 x 1 R q2".split(),
                          "q1 x 1 L q2".split(),
                          "q1 x 1 R q2".split(),
                          ]   
                        )
           ) 
print()
print()