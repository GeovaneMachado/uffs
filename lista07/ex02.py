def vogais(a):
    a = a.upper()
    count = 0
    for i in a:
        if i in 'AEIOU':
            count += 1
    return f'{count} vogais'

    
name = str(input())
print(vogais(name))