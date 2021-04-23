n1 = [8, 2, 4, 2, 4] 
n2 =  [3, 3, 7, 5, 2]
soma_num = []
soma = 0
resto = sobra = 0
for i in range(4, -1, -1):
    soma = n1[i] + n2[i] + sobra
    resto = soma % 10
    sobra = soma // 10
    soma_num.append(resto)
if sobra > 0:
    soma_num.append(sobra)
soma_num.reverse()
print(n1)
print(n2)
print(soma_num)