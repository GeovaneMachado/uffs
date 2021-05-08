def prod():#produtos cadastrados
    mercearia = [{'produto':'feijão 1kg','valor':7.99}, {'produto':'arroz 5kg','valor':19.99},{'produto':'sal 1kg','valor':3.99},
    {'produto': 'açucar 5kg','valor':10.99},{'produto':'farinha 5kg','valor':14.99},{'produto':'fermento 200g','valor':4.99}]
    eletronico = [{'produto':'Fone de ouvido','valor':79.99}, {'produto': 'mouse','valor':99.99},{'produto':'teclado','valor':139.99},
    {'produto': 'carregador','valor':29.99}, {'produto': 'webcam','valor':99.99}]
    bebidas = [{'produto': 'cerveja 350ml', 'valor': 2.49},{'produto': 'agua de coco 1l','valor': 5.99},
    {'produto':'Refrigerante 2l','valor':7.99},{'produto':'Suco 1l','valor':4.99}]
    segmento = int(input('Segmento:\n[1] mercearia\n[2] Bebidas\n[3] Eletronicos\nOpcao: '))
    while segmento > 4 or segmento < 1:
        print()
        print("OPÇÃO INVALIDA")
        print()
        segmento = int(input('Segmento:\n[1] mercearia\n[2] Bebidas\n[3] Eletronicos\nOpcao: '))
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
        print(f'Valor total: {compras[-1]}')


tot_cad = []
compras = []
count = soma = 0
while True:
    start = 4
    '''if start == 1:
        titulo('CADASTRO')
        registro = main()
        count = 1
        for i in range(len(tot_cad)):#percorre a matriz tot_cad para ver se o cpf se repete mais que uma vez
            if tot_cad[i][1] == registro[1]: 
                count += 1
        if count > 1:
            print('Pessoa ja cadastrada!')
            print ('Tente novamente!')
        else:
            tot_cad += [registro]'''
    if start == 4:
        #titulo('COMPRAR')
        itens = prod()
        if itens == 'Voltar':
            print('Voltando para o menu')
            break
        produtos = carrinho(itens)
        compras += produtos
        soma += compras[-1]['VALOR_TOT']
        compras.remove(compras[-1])
        compras.append(soma)
    elif start == 5:
        ver_carrinho(compras)
    

