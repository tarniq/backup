"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""

Horario = input("Informe o Horario atual: ")

try:
    Horario_int = float(Horario) 
    if Horario_int <= 11:
        print("BOM DIA")
    elif Horario_int > 12 and Horario_int <=17:
        print("boa tarde")
    elif Horario_int > 18 and Horario_int <=23:
        print("Boa noite")
except:
    print("Voce nao digitou um numero valido, tente algo entre 00 a 23")
