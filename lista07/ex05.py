def calc_pag(lista):
    dia = lista[0]/30
    lista[0] = lista[0] - lista[3]
    if lista[1] >= 20000:
        porc = lista[1]*0.05
    else:
        porc =lista[1]*0.03
    desc_falta = lista[2]*dia
    lista[0] += porc 
    lista[0] -=  desc_falta
    return lista[0]

valor = []
while True:
    valor.append(float(input('Salario liquido:')))
    valor.append(float(input('Total de vendas:')))
    valor.append(float(input('Faltas no mes:')))
    valor.append(float(input('Adiantamentos:')))
    total = calc_pag(valor)
    valor.clear()
    print(total)
    sair = str(input('Deseja continuar? [S/N]: ')).upper()
    while sair not in 'SN':
        sair = str(input('Deseja continuar? [S/N]: ')).upper()
    if sair == 'N':
        break