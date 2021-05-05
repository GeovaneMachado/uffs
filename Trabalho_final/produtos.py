def prod():
    carrinho_de_compras=[]
    mercearia = ['[1]-feijão 1kg','[2]-arroz 5kg','[3]-sal 1kg','[4]-açucar 5kg','[5]-farinha 5kg','[6]-fermento 200g']
    p_mercearia=[7.99, 19.99, 3.99, 10.99, 14.99, 4.99]
    eletronico = ['[1]-Fone de ouvido', '[2]-mouse','[3]-teclado','[4]-carregador','[5]-webcam']
    p_eletronico = [79.99, 99.99, 139.99, 29.99, 99.99]
    bebidas = ['[1]-cerveja 350ml','[2]-agua de coco 1l','[3]-Refrigerante 2l','[4]-Suco 1l']
    p_bebidas=[2.49,5.99,7.99,4.99]
    segmento = int(input('Segmetno:\n[1] mercearia\n[2] Bebidas\n[3] Eletronicos\nOpcao: '))
    while segmento > 3 or segmento < 1:
        print()
        print("OPÇÃO INVALIDA")
        print()
        segmento = int(input('Segmetno:\n[1] mercearia\n[2] Bebidas\n[3] Eletronicos\nOpcao: '))
    while segmento == 1:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Bem vindo a mercearia=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(mercearia)
        ler=int(input("Qual produto voce dezeja adicionar ao carrinho? "))
        break

prod()