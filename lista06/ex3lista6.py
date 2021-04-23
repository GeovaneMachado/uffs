lista = []
count = 0
while True:
    num = int(input('Numero:'))
    if lista.count(num) > 1:
        print('ESSE NUMERO JA EXISTE!')
    else:
        lista.append(num)
        print('Numero não existe na lista, adicionado!')
    sair = str(input('Para sair digite [S/N]:')).upper()
    while sair not in 'SN':
        sair = str(input('Para sair digite [S/N]:')).upper()
    if sair in 'S':
        break
lista.sort()
for j in lista:
    print(j, end=' ')
