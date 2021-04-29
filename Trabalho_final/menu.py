def menu():
    Menu=int(input("[1]-Cadastro\n[2]-Login\n[3]-consultar cliente\n[4]-Fazer compras\n[5]-Ver carrinho\n[6]-pagamento\n"))
    while Menu > 6 or Menu < 1:
        print("Opção invalida")
        Menu=int(input("[1]-Cadastro\n[2]-Login\n[3]-consultar cliente\n[4]-Fazer compras\n[5]-Ver carrinho\n[6]-pagamento\n"))
    return Menu 



