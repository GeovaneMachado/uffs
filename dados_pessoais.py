#cadastro de dados
def pessoa():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=Iniciando cadastro-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    nome_usuario=str(input("digite seu nome completo: "))
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

pes=cad_email()
print(pes)