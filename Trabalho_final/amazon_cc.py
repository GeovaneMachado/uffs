def bem_vindo():
    from time import sleep
    cabe = '*=' *15
    comeco = 'Bem vindo a loja virtual'
    for i in cabe:
        print(i, end='')
       # sleep(0.1)
    print()
    print('|  ', end='')
    for i in comeco:
        print(i, end='')
      #  sleep(0.25)
    print(f'{"|":>3}')
    for i in cabe:
        print(i, end='')
       # sleep(0.1)

def valida_cpf(cpf):
    soma = j = 0 
    verificar =  True
    count = 10
    cpf = str(cpf).replace('.','').replace('-','') #Apaga os pontos e tracos se forem digitados
    fat_cpf = []
    for i in cpf: #transforma cada elemento no cpf em inteiros e coloca eles em uma lista(fat_cpf)
        i = int(i) 
        fat_cpf.append(i)
    while j < 11:
        soma += fat_cpf[j] * count #multiplica o numero do cpf pelo count 
        j += 1
        count -= 1 #decrementa 1 no count 
        if count <= 1:
            if verificar: #verifica se o primeiro digito é valido
                digito1 = 11 - (soma % 11)
                if digito1 < 2 or soma % 11 == 0:
                    digito1 = 0
                count = 11
                j = 0
                soma = 0
                verificar = False
            else: #verifica se o segundo digito é valido
                digito2 = 11 - (soma % 11)
                if digito2 < 2 or soma % 11 == 0:
                    digito2 = 0
                break 
    if digito1 == fat_cpf[-2] and digito2 == fat_cpf[-1]:
        return True
    else:
        return False
        
cpf = str(input())
print(valida_cpf(cpf))
