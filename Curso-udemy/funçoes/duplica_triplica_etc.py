def multiplicaçoes(quantida_x):
    def multiplicar(numero):
        return int(quantida_x)*int(numero)
    return multiplicar
    

numero_u = input("digite um numero: ")
multiplicador = input("digite um multiplicador: ")

resultado = multiplicaçoes(multiplicador)
print(resultado(numero_u))

# duplicar = multiplicaçoes(10)

    
    

