def prod():
    mercearia = ['[1]-feijão 1kg',7.99,'[2]-arroz 5kg',19.99,'[3]-sal 1kg',3.99,'[4]-açucar 5kg',10.99,'[5]-farinha 5kg',14.99,'[6]-fermento 200g',4.99]
    eletronico = ['[1]-Fone de ouvido',79.99, '[2]-mouse',99.99,'[3]-teclado',139.99,'[4]-carregador',29.99,'[5]-webcam',99.99]
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
    add=None
    cont="s"
    for i in produtos:
        print(i)
    while True:
        add=int(input("Qual produto vc deseja adicionar ao carrinho? "))
        if add == 1:
            cesto.append(produtos[0])
            cesto.append(produtos[1])
        elif add == 2:
            cesto.append(produtos[2])
            cesto.append(produtos[3])
        elif add == 3:
            cesto.append(produtos[4])
            cesto.append(produtos[5])
        elif add == 4:
            cesto.append(produtos[6])
            cesto.append(produtos[7])      
        elif add == 5:
            cesto.append(produtos[8])
            cesto.append(produtos[9])
        elif add == 6:
            cesto.append(produtos[10])
            cesto.append(produtos[11])
        cont=input("Quer adicionar mais produtos? [s/n]")
        if cont == "n":
            break
    print(cesto)



tsta=prod()
bigodin=carrinho(tsta)