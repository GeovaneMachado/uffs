num = []
while True:
    n = int(input('Digite um numero 0 para parar: '))
    if n == 0:
        break
    num.append(n)
soma = 0
num.sort()
print(num)
for i in num:
    if num.count(i) > 1:
        soma = i * num.count(i)
        num.append(soma)
        j = i
        while num.count(i) != 0:
            num.remove(i)
            if num.count(i) == 0:
                j = 0
num.sort()
print(num)
