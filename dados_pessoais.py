#cadastro de dados
def pessoa():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=Iniciando cadastro-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    nome_usuario=str(input("digite seu nome completo: "))
    return nome_usuario
    
def cad_cpf:
    cpf=str("Digite seu cpf: ")
    ver_cpf=valida_cpf(cpf)
    while ver_cpf == False:
        print("CPF invalido")
        cpf=str("Por favor digite novamente: ")
        ver_cpf=valida_cpf(cpf)
    print("Ok")