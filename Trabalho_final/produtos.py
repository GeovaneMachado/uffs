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
    else:
        if segmento == 2:
            return bebidas
        else:
            if segmento == 3:
                return eletronico

   
   
   
   
    #carrinho_de_compras=[]
    #while segmento == 1:
    #    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Bem vindo a mercearia=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    #    print(mercearia)
    #    ler=int(input("Qual produto voce dezeja adicionar ao carrinho? "))
    #    break

jogo=prod()
print(jogo)