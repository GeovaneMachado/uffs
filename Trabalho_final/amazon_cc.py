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
    resultado = []
    for j in range(0, 10):
        soma += fat_cpf[j] * count #multiplica o numero do cpf pelo count 
        print(j, count)
        count -= 1 #decrementa 1 no count 
        resultado.append(soma)
        if count <= 1:
            if verificar:
                print(resultado)
                digito1 = 11 - (soma % 11)
                if digito1 < 2:
                    digito1 = 0
                count = 11
                j = 0
                soma = 0
                verificar = False
                resultado.clear()
            else:
                print(resultado)
                digito2 = 11 - (soma % 11)
                print(digito2)
                if digito2 < 2:
                    digito2 = 0
                break       
    print(fat_cpf)
    return fat_cpf
        
cpf = str(input())
valida_cpf(cpf)
bem_vindo()