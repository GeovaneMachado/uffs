#Definindo funções 
class cadastro:
    nome =None
    cpf = None
    email = None
    senha = None
    saldo = None

def bem_vindo():
    from time import sleep
    cabe = '*=' *20
    comeco = 'Bem vindo a loja virtual'
    for i in cabe:
        print(i, end='')
        sleep(0.1)
    print()
    print('|       ', end='')
    for i in comeco:
        print(i, end='')
        sleep(0.1)
    print(f'{"|":>8}')
    for i in cabe:
        print(i, end='')
        sleep(0.1)
    print()

def titulo(palavra):
    print(f'{"-"*40}')
    print(f'{palavra.upper()}'.center(40))
    print(f'{"-"*40}')

def menu1():
    Menu=int(input("[1]-Cadastro\n[2]-Login\nOpcao: "))
    while Menu > 2 or Menu < 1:
        print("Opção invalida")
        Menu=int(input("[1]-Cadastro\n[2]-Login\nOpcao: "))
    return Menu

def menu2():
    titulo('menu principal')
    Menu=int(input("[1]-consultar cliente\n[2]-Fazer compras\n[3]-Ver carrinho\n[4]-pagamento\n[5]-Voltar\nOpcao: "))
    while Menu > 5 or Menu < 1:
        print("Opção invalida")
        Menu=int(input("[1]-consultar cliente\n[2]-Fazer compras\n[3]-Ver carrinho\n[4]-pagamento\n[5]-Voltar\nOpcao: "))
    return Menu

def valida_cpf(cpf):
    soma = j = 0
    verificar =  True
    count = 10
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
        
def cad_cpf(): #essa função serve para cadastrar o cpf
    cpf=str(input("Digite seu cpf: ")).replace('.','').replace('-','')  #Apaga os pontos e tracos se forem digitados
    ver_cpf=valida_cpf(cpf)
    while ver_cpf == False:
        print("CPF invalido")
        cpf=str(input("Por favor digite novamente: "))
        ver_cpf=valida_cpf(cpf)
    return cpf


def cad_senha(): #Essa função serve para cadastrar a senha do usuario
    from getpass import getpass #Esconde a senha digitada
    print('Cadastre sua senha com 6 digitos!')
    while True:
        senha = getpass('Digite sua senha: ')
        conf_senha= getpass('Confirme sua senha: ')
        if senha != conf_senha:
            print("As senhas divergem")
        elif len(senha) != 6:
            print('A senha precisa ter 6 digitos')
        else:
            print("senha cadastrada com sucesso")
            break
    return senha


def cad_email(): #Essa função serve para cadastrar o email do usuario
    email=str(input("Digite seu indereço de email: "))
    return email

def main(): #Essa função serve para o usuario cadastrar seus dados
    pessoas = cadastro()
    pessoa_cad = [] 
    pessoas.nome = input('Nome: ')
    pessoas.cpf = cad_cpf()
    pessoas.email = str(input("Digite seu indereço de email: "))
    pessoas.senha = cad_senha()
    pessoas.saldo = 1000
    pessoa_cad.append(pessoas.nome)
    pessoa_cad.append(pessoas.cpf)
    pessoa_cad.append(pessoas.email)
    pessoa_cad.append(pessoas.senha)
    pessoa_cad.append(pessoas.saldo) #adiciona os dados no vetor para cadastro
    return pessoa_cad



def log(x):
    from getpass import getpass
    while True:
        logui=[]
        cpf=input("Digite o seu CPF: ")
        if valida_cpf(cpf):
            senha=getpass("Digite sua senha: ")
            for i in range(len(x)):
                if x[i][1] == cpf and x[i][3] == senha:
                    logui.append(x[i][0])
                    logui.append(x[i][2])
                    logui.append(x[i][4])
                    print()
                    print("=-=-=-=-=-=-Login efetuado com sucesso=-=-=-=-=-=-=")
                    print()
                    return logui
        else:
            print("CPF invalido")
                      
def cons(x):
    while True:
        logui=[]
        cpf=input("Digite o seu CPF: ")
        if valida_cpf(cpf):
            for i in range(len(x)):
                if x[i][1] == cpf:
                    logui.append(x[i][0])
                    logui.append(x[i][2])
                    return logui
        else:
            print("CPF não encontrado!")

def prod():#produtos cadastrados
    mercearia = [{'produto':'feijão 1kg','valor':7.99}, {'produto':'arroz 5kg','valor':19.99},{'produto':'sal 1kg','valor':3.99},
    {'produto': 'açucar 5kg','valor':10.99},{'produto':'farinha 5kg','valor':14.99},{'produto':'fermento 200g','valor':4.99}]
    eletronico = [{'produto':'Fone de ouvido','valor':79.99}, {'produto': 'mouse','valor':99.99},{'produto':'teclado','valor':139.99},
    {'produto': 'carregador','valor':29.99}, {'produto': 'webcam','valor':99.99}]
    bebidas = [{'produto': 'cerveja 350ml', 'valor': 2.49},{'produto': 'agua de coco 1l','valor': 5.99},
    {'produto':'Refrigerante 2l','valor':7.99},{'produto':'Suco 1l','valor':4.99}]
    segmento = int(input('Segmento:\n[1] Mercearia\n[2] Bebidas\n[3] Eletronicos\n[4] Voltar\nOpcao: '))
    while segmento > 4 or segmento < 1:
        print()
        print("OPÇÃO INVALIDA")
        print()
        segmento = int(input('Segmento:\n[1] mercearia\n[2] Bebidas\n[3] Eletronicos\n[4]Voltar\nOpcao: '))
    if segmento == 1: # retorna qual segmento a pessoa quer ver para fazer a compra
        return mercearia
    elif segmento == 2:
        return bebidas
    elif segmento == 3:
        return eletronico
    else:
        return 'Voltar'


def carrinho(produtos):
    cesto=[]
    adic_car=None
    cont="s"
    for i, v in enumerate(produtos):
        print(f" {i} {v['produto']} R${v['valor']} ")#mostra os produtos formatado
    print()
    valor_final = 0
    while True:
        try:
            adic_car=int(input("Digite o codigo do produto:  "))
            cesto.append(produtos[adic_car])
            cesto[-1]['quantidade'] = int(input('Quantidade do produto: '))
            valor_final += cesto[-1]['valor'] * cesto[-1]['quantidade'] #soma o valor que vai da do produto e acrescenta no valor total
            cont=input("Quer adicionar mais produtos? [s/n]").lower()
            while cont not in 'sn':
                cont = input('Quer visualizar o valor total?[s/n]: ').lower()
        except:
            print('ERRO!!')
        if cont == "n":
            break
    cesto.append({'VALOR_TOT':valor_final})
    return cesto
    

def ver_carrinho(compras):
    for i, v in enumerate(compras): #mostra os produtos adicionados no carrinho
        try:
            print(f'Item: {i} {v["produto"]}  R${v["valor"]:.2f}    Quantidade:{v["quantidade"]}')
        except:
            pass
    while True:
        vis_tot = input('Quer visualizar o valor total?[s/n]: ').lower()
        if vis_tot in 'sn':
            break
    if vis_tot == 's':
        print(f'Valor total: R${compras[-1]}')

    
  
  

bem_vindo()
tot_cad = []
compras = []
count = soma = 0
while True:
    titulo('amazon cc')
    start = menu1()
    if start == 1: #Cadastro de clientes novos
        titulo('CADASTRO')
        registro = main()
        print(registro)
        count = 1
        for i in range(len(tot_cad)):#percorre a matriz tot_cad para ver se o cpf se repete mais que uma vez
            if tot_cad[i][1] == registro[1]: 
                count += 1
        if count > 1:
            print('Pessoa ja cadastrada!')
            print ('Tente novamente!')
        else:
            tot_cad += [registro]
    if start == 2:  # Login 
        loguin=log(tot_cad)
        while True:
            play=menu2()
            if play == 1: # Consultar cliente
                tituo('consulta') 
                consulta=cons(tot_cad)
                print("Cadastro encontrado")
                print(f"nome: {consulta[0]}\nE-mail: {consulta[1]}")
            elif play == 2: # função destinada a fazer compras
                titulo('compras') 
                itens = prod()
                if itens == 'Voltar':
                    print('Voltando para o menu')
                    continue
                produtos = carrinho(itens)
                compras += produtos
                soma += compras[-1]['VALOR_TOT']
                compras.remove(compras[-1])
                compras.append(soma)
            elif play == 3:
                titulo('seu carrinho') 
                ver_carrinho(compras)
            elif play == 4:
                print("O total da compra foi: {} R$".format(soma))
                saldo=loguin[2]
                checkout=(saldo-soma)
                if checkout < 0:
                    print("Saldo insuficiente")
                else:
                    loguin.remove(saldo) 
                    loguin.append(checkout)
                    print("Pagamento efetuado com sucesso!")      
                    print(f"Novo saldo: {checkout}")
                          