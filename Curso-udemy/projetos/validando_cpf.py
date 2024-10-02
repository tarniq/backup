import random
import sys
import re

cpf = ''

for i in range(9):
    cpf += str(random.randint(0,9))
print(cpf)

digito_9 = cpf [:9]

soma_d = 0
soma_segundo_d = 0

indicie_multiplicador = 10

#Primeiro digito

for i in digito_9:
        
        soma_d += int(i)*indicie_multiplicador
        indicie_multiplicador -= 1

resultado_m = (soma_d*10)%11
priemiro_digito = 0 if resultado_m > 9 else resultado_m


print(priemiro_digito)

#Segundo digito

indicie_multiplicador_s = 11
segundo_d_processados = digito_9 + str(priemiro_digito)

for i in segundo_d_processados:
        
        soma_segundo_d += int(i)*indicie_multiplicador_s
        indicie_multiplicador_s -= 1

resultado_segundo = (soma_segundo_d*10)%11
segundo_digito = 0 if resultado_segundo > 9 else resultado_segundo

print(segundo_digito)

cpf_calculo = f'{digito_9}{priemiro_digito}{segundo_digito}'

print(cpf_calculo)

cpf += f'{priemiro_digito}{segundo_digito}'

#Validaçao

if cpf == cpf_calculo:
    print("Seu cpf é valido")
else:
    print("Seu cpf é invalido")



#Opçao para entrada de dados pelo usuario

#entrada = input('CPF [746.824.890-70]: ')
#cpf = re.sub(
#     r'[^0-9]',
#        '',
#    entrada
#)
#cpf += f'{priemiro_digito}{segundo_digito}' (colocar essa linha a cima da validaçao)