def prod():
    mercearia = [{'produto':'feijão 1kg','valor':7.99}, {'produto':'arroz 5kg','valor':19.99},{'produto':'sal 1kg','valor':3.99},
    {'produto': 'açucar 5kg','valor':10.99},{'produto':'farinha 5kg','valor':14.99},{'produto':'fermento 200g','valor':4.99}]
    eletronico = [{'produto':'Fone de ouvido','valor':79.99}, {'produto': 'mouse','valor':99.99},{'produto':'teclado','valor':139.99},
    {'produto': 'carregador','valor':29.99}, {'produto': 'webcam','valor':99.99}]
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
    adic_car=None
    cont="s"
    for i, v in enumerate(produtos):
        print(f" {i} {v['produto']} R${v['valor']} ")
    print()
    while True:
        adic_car=int(input("Digite o codigo do produto:  "))
        cesto.append(produtos[adic_car])
        cesto[-1]['quantidade'] = int(input('Quantidade do produto: '))
        cesto[-1]['valor'] *= cesto[-1]['quantidade']
        cont=input("Quer adicionar mais produtos? [s/n]")
        if cont == "n":
            break
    return cesto



tsta=prod()
bigodin=carrinho(tsta)