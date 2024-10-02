"""
split e join com list e str
split - divide uma string (list)
join - une uma string
strip - remove o espaço do começo e do final da str

"""
import os

frase = " privet macarrao com pera           , macaco subindo no poste         , musica ruim        "

lista_palavras =  frase.split()
os.system('cls')
#print ("*"*10)
#print (lista_palavras)
#print ("*"*10)

lista_frases_cruas = frase.split(" ,")
#print((lista_frases_cruas))

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases)
lista_unidas = ', '.join(lista_frases)
print(lista_unidas)

