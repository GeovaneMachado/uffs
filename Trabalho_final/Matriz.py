#Definindo funções 
def bem_vindo():
    from time import sleep
    cabe = '*=' *15
    comeco = 'Bem vindo a loja virtual'
    for i in cabe:
        print(i, end='')
        sleep(0.1)
    print()
    print('|  ', end='')
    for i in comeco:
        print(i, end='')
        sleep(0.1)
    print(f'{"|":>3}')
    for i in cabe:
        print(i, end='')
        sleep(0.1)
    print()

def titulo(palavra):
    print(f'{"-"*30}')
    print(f'{palavra.upper()}'.center(30))
    print(f'{"-"*30}')

def menu():
    Menu=int(input("[1]-Cadastro\n[2]-Login\n[3]-consultar cliente\n[4]-Fazer compras\n[5]-Ver carrinho\n[6]-pagamento\n"))
    while Menu > 6 or Menu < 1:
        print("Opção invalida")
        Menu=int(input("[1]-Cadastro\n[2]-Login\n[3]-consultar cliente\n[4]-Fazer compras\n[5]-Ver carrinho\n[6]-pagamento\n"))
    return Menu

def valida_cpf(cpf):
    soma = j = 0 
    verificar =  True
    count = 10
    cpf = cpf.replace('.','').replace('-','') #Apaga os pontos e tracos se forem digitados
    fat_cpf = []
    for i in cpf: #transforma cada elemento no cpf em inteiros e coloca eles em uma lista(fat_cpf)
        i = int(i) 
        fat_cpf.append(i)
    if len(fat_cpf) < 11:
        return False
    else:
        while j < 11:
            soma += fat_cpf[j] * count #multiplica o numero do cpf pelo count 
            j += 1
            count -= 1 #decrementa 1 no count 
            if count <= 1:
                if verificar: #verifica se o primeiro digito é valido
                    resto = soma % 11
                    digito1 = 11 - resto
                    if resto < 2:
                        digito1 = 0
                    count = 11
                    j = 0
                    soma = 0
                    verificar = False #Apos verificar o primeiro digito a variavel fica False e não executa mais esse bloco
                else: #verifica se o segundo digito é valido
                    resto = soma % 11
                    digito2 = 11 - resto
                    if resto < 2:
                        digito2 = 0
                    break 
        if digito1 == fat_cpf[-2] and digito2 == fat_cpf[-1]:
            return True
        else:
            return False
        
def cad_cpf():
    #essa função serve para cadastrar o cpf
    cpf=str(input("Digite seu cpf: "))
    ver_cpf=valida_cpf(cpf)
    while ver_cpf == False:
        print("CPF invalido")
        cpf=str(input("Por favor digite novamente: "))
        ver_cpf=valida_cpf(cpf)
    return cpf


def cad_senha():
    #Essa função serve para cadastrar a senha do usuario
    from getpass import getpass #Esconde a senha digitada
    print('Cadastre sua senha com 6 digitos!')
    while True:
        senha = getpass('Digite sua senha: ')
        conf_senha=getpass('Confirme sua senha: ')
        if senha != conf_senha:
            print("As senhas divergem")
        elif len(senha) != 6:
            print('A senha precisa ter 6 digitos')
        else:
            print("senha cadastrada com sucesso")
            break
    return senha


def cad_email():
    #Essa função serve para cadastrar o email do usuario
    email=str(input("Digite seu indereço de email: "))
    return email

class cadastro:
    nome =None
    cpf = None
    email = None
    senha = None
    saldo = None

def lista():#Essa função serve para o usuario cadastrar seus dados
    titulo("Cadastro")
    tot_cad = []
    pessoas = cadastro()
    count = 0
    sair = ' '
    while True:
        pessoa_cad = []
        pessoas.nome = input('Nome: ')
        pessoas.cpf = cad_cpf()
        pessoas.email = cad_email()
        pessoas.senha = cad_senha()
        pessoas.saldo = 1000
        pessoa_cad.append(pessoas.nome)
        pessoa_cad.append(pessoas.cpf)
        pessoa_cad.append(pessoas.email)
        pessoa_cad.append(pessoas.senha)
        pessoa_cad.append(pessoas.saldo)
        for i in range(len(tot_cad)):
            if tot_cad[i].index(pessoas.cpf) not in tot_cad[i]:
                print('ok')
            else:
                print('Ja existe') 
        tot_cad += [pessoa_cad]
        print(tot_cad)
        sair = input('continuar?[s/n]').upper()
        if sair in 'N':
            break
    return tot_cad

#bem_vindo()
cadastro = lista()
print(cadastro)




