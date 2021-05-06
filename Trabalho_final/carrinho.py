def prod():
    mercearia = [{'produto':'feijão 1kg','valor':7.99},
    {'produto':'arroz 5kg','valor':19.99},
    {'produto':'sal 1kg','valor':3.99},
    {'produto': 'açucar 5kg','valor':10.99},
    {'produto':'farinha 5kg','valor':14.99},
    {'produto':'fermento 200g','valor':4.99}]
    eletronico = [{'produto':'Fone de ouvido','valor':79.99},
    {'produto': 'mouse','valor':99.99},
    {'produto':'teclado','valor':139.99},
    {'produto': 'carregador','valor':29.99},
    {'produto': 'webcam','valor':99.99}]
    bebidas = ['[1]-cerveja 350ml',2.49,'[2]-agua de coco 1l',5.99,'[3]-Refrigerante 2l',7.99,'[4]-Suco 1l',4.99]
    segmento = int(input('Segmetno:\n[1] mercearia\n[2] Bebidas\n[3] Eletronicos\nOpcao: '))
    while segmento > 3 or segmento < 1:
        print()
        print("OPÇÃO INVALIDA")
        print()
        segmento = int(input('Segmetno:\n[1] mercearia\n[2] Bebidas\n[3] Eletronicos\nOpcao: '))
    if segmento == 1:
        return mercearia
    elif segmento == 2:
        return bebidas
    else:
        return eletronico


def carrinho(produtos):
    cesto=[]
    total=[]
    add=None
    cont="s"
    for i, v in enumerate(produtos):
        print(f" {i} {v['produto']} R${v['valor']} ")
    print()
    while True:
        add=int(input("Qual produto vc deseja adicionar ao carrinho? "))
        if add == 1:
            cesto.append(produtos[0])
            total.append(produtos[1])
        elif add == 2:
            cesto.append(produtos[2])
            total.append(produtos[3])
        elif add == 3:
            cesto.append(produtos[4])
            total.append(produtos[5])
        elif add == 4:
            cesto.append(produtos[6])
            total.append(produtos[7])      
        elif add == 5:
            cesto.append(produtos[8])
            total.append(produtos[9])
        elif add == 6:
            cesto.append(produtos[10])
            total.append(produtos[11])
        print(cesto)
        print(total)
        cont=input("Quer adicionar mais produtos? [s/n]")
        if cont == "n":
            break
    return cesto



tsta=prod()
bigodin=carrinho(tsta)