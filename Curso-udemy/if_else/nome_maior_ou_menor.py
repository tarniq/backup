"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 

"""

nome = input("Digite seu nome: ")

if len(nome) <=4:
    print("seu nome é pequeno!")
elif len(nome) > 4 and len(nome) <=6:
    print("Seu nome é normar")
else:
    print("Seu nome é muito grande")