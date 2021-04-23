def fracao(n):
    soma = 0
    for i in range(2, n+1):
        if i % 2 == 0:
            soma = soma + (1/i)
        else:
            soma = soma - (1/i)
    return soma
num = int(input('Numero: '))
print(fracao(num))


