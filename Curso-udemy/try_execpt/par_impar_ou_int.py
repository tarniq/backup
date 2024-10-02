"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

"""

Valor_digitado = input("Digite um valor: ")

try:
    Valor_digitado_int = int(Valor_digitado)
    if Valor_digitado_int % 2 == 0:
        print("Valor é par")
    else :
        print("Valor é impar")
except:
    print("Voce nao digitou um numero inteiro")