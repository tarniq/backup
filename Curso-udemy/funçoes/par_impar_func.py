def par_impar(x):
    if x % 2 == 0:
        return("seu numero é par")
    return("seu numero é impar")


entrada = int(input("Digite um numero: "))

resultado = par_impar(entrada)
print(resultado)