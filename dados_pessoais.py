#cadastro de dados
def ver_nome(lista,nome_usuario):
    verificacao=bool
    if nome_usuario in lista:
        return True
    else:
        return False
       

def pessoa(lista):
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=Iniciando cadastro-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    nome_usuario=str(input("digite seu nome completo: "))
    ver=ver_nome(lista,nome_usuario)
    while ver == True:
        print("nome ja cadastrado")
        nome_usuario=str(input("digite seu nome completo: "))
        ver=ver_nome(lista,nome_usuario)
    return nome_usuario
    

def cad_cpf():
    cpf=str("Digite seu cpf: ")
    ver_cpf=valida_cpf(cpf)
    while ver_cpf == False:
        print("CPF invalido")
        cpf=str("Por favor digite novamente: ")
        ver_cpf=valida_cpf(cpf)
    print("Ok")
    return cpf

def cad_senha():
    senha=str(input("Digite sua nova senha: "))
    conf_senha=(input("Confireme seu senha: "))
    while senha != conf_senha:
        print("As senhas divergem")
        senha=str(input("Digite novamente sua nova senha: "))
        conf_senha=(input("Confireme seu nova senha: "))
        print("senha cadastrada com sucesso")
    return senha

def cad_email():
    email=str(input("Digite seu indereço de email: "))
    return email

#lista=['maluko','judite']
#while True:
#    teste=pessoa(lista)
#    lista.append(teste)
#    print(lista)
