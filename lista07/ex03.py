def area_circulo(r):
    from math import pi
    area = pi * r**2
    return f'{area:.2f}'

def area_triangulo(b, h):
    area = b * h / 2
    return f'{area:.2f}'

def area_retangulo(b, a):
    area = b * a
    return area

def titulo(palavra):
    print(f'{"-"*30}')
    print(f'{palavra.upper()}'.center(30))
    print(f'{"-"*30}')

while True:
    titulo('MENU')
    print('[C] Area do circulo\n[T] Area do Triangulo\n[R] Area do retangulo\n[S] Finalizar')
    opc = str(input('Opcao: ')).upper()
    while opc not in 'CTRS':
        print('Opcao invalida!!')
        opc = str(input('Opcao: ')).upper()
    if opc == 'C':
        titulo('Area do circulo')
        raio = float(input('Digite o raio do circulo: '))
        raio = area_circulo(raio)
        print(f'A area do ciculo é: {raio}')
    else:
        if opc == 'T':
            titulo('area do triangulo')
            base = float(input('Base: '))
            alt = float(input('Altura: '))
            tot = area_triangulo(base, alt)
            print(f'A area do triangulo é: {tot}')
        else:
            if opc == 'R':
                titulo('Area do retangulo')
                base = float(input('Base: '))
                alt = float(input('Altura: '))
                tot = area_retangulo(base, alt)
                print(f'A area do retangulo é: {tot}')
            else:
                titulo('Programa finalizado')
                break
