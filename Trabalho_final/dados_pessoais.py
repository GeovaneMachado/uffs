#cadastro de dados

def ver_nome(lista,nome_usuario):
    #Essa função verifica se o nome que o usuario esta cadastrando ja esta no sistema
    verificacao=bool
    if nome_usuario in lista:
        return True
    else:
        return False
       

def pessoa(lista):
    #Essa função serve para o usuario cadastrar seu nome
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=Iniciando cadastro-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    nome_usuario=str(input("digite seu nome completo: "))
    ver=ver_nome(lista,nome_usuario)
    while ver == True:
        print("nome ja cadastrado")
        nome_usuario=str(input("digite seu nome completo: "))
        ver=ver_nome(lista,nome_usuario)
    return nome_usuario
    
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
                    digito1 = 11 - (soma % 11)
                    if digito1 < 2 or soma % 11 == 0:
                        digito1 = 0
                    count = 11
                    j = 0
                    soma = 0
                    verificar = False #Apos verificar o primeiro digito a variavel fica False e não executa mais esse bloco
                else: #verifica se o segundo digito é valido
                    digito2 = 11 - (soma % 11)
                    if digito2 < 2 or soma % 11 == 0:
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
    senha = getpass('Digite sua senha: ')
    conf_senha=getpass('Confirme sua senha: ')
    while senha != conf_senha:
        print("As senhas divergem")
        senha = getpass('Digite sua senha: ')
        conf_senha=getpass('Confirme sua senha: ')
        print("senha cadastrada com sucesso")
    return senha

def cad_email():
    #Essa função serve para cadastrar o email do usuario
    email=str(input("Digite seu indereço de email: "))
    return email

def lista():
    pessoa = pessoa()
    cpf = cad_cpf()
    email = cad_email()
    senha = cad_senha()
    cadastro = [pessoa, email, cpf, senha]
    return cadastro


#lista=['maluko','judite']
#while True:
#    teste=pessoa(lista)
#    lista.append(teste)
#    print(lista)
