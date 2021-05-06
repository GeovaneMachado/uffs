def prod():
    mercearia = [{'produto':'feijão 1kg','valor':7.99}, {'produto':'arroz 5kg','valor':19.99},{'produto':'sal 1kg','valor':3.99},
    {'produto': 'açucar 5kg','valor':10.99},{'produto':'farinha 5kg','valor':14.99},{'produto':'fermento 200g','valor':4.99}]
    eletronico = [{'produto':'Fone de ouvido','valor':79.99}, {'produto': 'mouse','valor':99.99},{'produto':'teclado','valor':139.99},
    {'produto': 'carregador','valor':29.99}, {'produto': 'webcam','valor':99.99}]
    bebidas = [{'produto': 'cerveja 350ml', 'valor': 2.49},{'produto': 'agua de coco 1l','valor': 5.99},
    {'produto':'Refrigerante 2l','valor':7.99},{'produto':'Suco 1l','valor':4.99}]
    segmento = int(input('Segmetno:\n[1] mercearia\n[2] Bebidas\n[3] Eletronicos\nOpcao: '))
    while segmento > 3 or segmento < 1:
        print()
        print("OPÇÃO INVALIDA")
        print()
        segmento = int(input('Segmento:\n[1] mercearia\n[2] Bebidas\n[3] Eletronicos\nOpcao: '))
    if segmento == 1:
        return mercearia
    elif segmento == 2:
        return bebidas
    else:
        return eletronico


def carrinho(produtos):
    cesto=[]
    total=[]
    adic_car=None
    cont="s"
    for i, v in enumerate(produtos):
        print(f" {i} {v['produto']} R${v['valor']} ")
    print()
    valor_final = 0
    while True:
        try:
            adic_car=int(input("Digite o codigo do produto:  "))
            cesto.append(produtos[adic_car])
            cesto[-1]['quantidade'] = int(input('Quantidade do produto: '))
            cont=input("Quer adicionar mais produtos? [s/n]").lower()
        except:
            print('ERRO!!')
        if cont == "n":
            break
    cesto.append(valor_final)
    return cesto
    

def ver_carrinho(compras, saldo=0):
    print(compras)
    for i, v in enumerate(compras):
        print(f'Item: {i} {v["produto"]}  R${v["valor"]:.2f}    Quantidade:{v["quantidade"]}')
    vis_tot = input('Quer visualizar o valor total?[s/n]: ').lower()
    if vis_tot == 's':
        print(f'Valor total: {saldo:.2f}')


tot_cad = []
compras = []
count = 0
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
        produtos = carrinho(itens)
        compras += produtos
        for i in compras:
            soma = i['valor'] * i['quantidade']
            count += soma
        print(count)
        ver_carrinho(compras)
