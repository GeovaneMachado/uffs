def bem_vindo():
    from time import sleep
    print('*=' *15)
    comeco = 'Bem vindo a loja virtual'
    print('|  ', end='')
    for i in comeco:
        print(i, end='')
        sleep(0.25)
    print(f'{"|":>4}')
    print('*=' *15)
bem_vindo()