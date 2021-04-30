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
        sleep(0.25)
    print(f'{"|":>3}')
    for i in cabe:
        print(i, end='')
        sleep(0.1)
    print()

def menu():
    Menu=int(input("[1]-Cadastro\n[2]-Login\n[3]-consultar cliente\n[4]-Fazer compras\n[5]-Ver carrinho\n[6]-pagamento\n"))
    while Menu > 6 or Menu < 1:
        print("Opção invalida")
        Menu=int(input("[1]-Cadastro\n[2]-Login\n[3]-consultar cliente\n[4]-Fazer compras\n[5]-Ver carrinho\n[6]-pagamento\n"))
    return Menu

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

#programa principal
boas_vindas=bem_vindo()
cad_clientes=[]
while True:
    fun_menu=menu()
    if fun_menu == 1:
        apender = pessoa(cad_clientes)
        cad_clientes.append(apender)


