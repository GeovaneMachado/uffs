def palindromo(frase):
    frase = frase.replace(' ', '')
    inverso = frase[::-1]
    if frase == inverso:
        return True
    else:
        return False

frase = str(input('Frase: '))
print(palindromo(frase))