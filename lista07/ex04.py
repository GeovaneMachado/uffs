def repet(lista):
    cont = 0
    n_repetidos = []
    for i in lista:
        if n_repetidos.count(i) == 0:
            if lista.count(i) > 1:
                n_repetidos.append(i)
    return n_repetidos

numeros = []
for i in range(0, 10):
    numeros.append(int(input('Numero: ')))
print(repet(numeros))
