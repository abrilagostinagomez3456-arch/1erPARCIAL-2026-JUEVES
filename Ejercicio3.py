def calcular_interrupciones(a, b):
    if b == 0:
        return 0 
    elif b == 1:
        return a
    else:
        return a + calcular_interrupciones(a, b - 1) 

print(calcular_interrupciones(3, 4))
