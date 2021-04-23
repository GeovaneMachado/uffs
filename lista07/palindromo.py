
def palindromo(frase):
    frase = frase.split()
    count = 0
    print(frase)
    print(verificar)
    if len(frase) > 1:
        for i in frase:
            for c in i:
                for j in verificar:
                    for v in j:
                        if c == v:
                            count = count + 1
        if count == len(frase):
            return True
        else:
            return False
    else:
        print(verificar)


frase = str(input('Frase: '))
print(palindromo(frase))