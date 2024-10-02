# mexendo com args
def somas(*args):
    soma_total = 0 
    for i in args:
        soma_total += int(i)
    return soma_total


numeros_u = input("digite varios numeros pra saber a soma total deles: ")

tupla_num = tuple(numeros_u.split(","))



print(*tupla_num)
resultado = somas(*tupla_num)
print(resultado)


