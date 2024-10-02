from math import pow
nome = str(input("Digite seu nome: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso/pow(altura, 2)
print(f"\n {nome} tem {altura:.2f} de altura \n pesa {peso:.2f} quilos e seu IMC é \n {imc:.2f}")

