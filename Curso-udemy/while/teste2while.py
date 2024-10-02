idade = int(input("Digite o ano que nasceu que eu falarei sua: "))
contador = 0
conta = 2024 - idade
while contador < conta:
    contador += 1
    print("?")
    if contador == conta :
        print(f"voce tem {contador} anos certo ?")
        break