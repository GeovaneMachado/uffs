def bem_vindo():
    from time import sleep
    cabe = '*=' *15
    comeco = 'Bem vindo a loja virtual'
    for i in cabe:
        print(i, end='')
        sleep(0.25)
    print('|  ', end='')
    for i in comeco:
        print(i, end='')
        sleep(0.25)
    print(f'{"|":>3}')
    for i in cabe:
        print(i, end='')

bem_vindo()