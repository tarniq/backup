"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

Empacotamento e desempacotamento
--> para desempacotar basta colocar uma variavel pra tirar o valor de dentro
--> para empacotar os demais valores usar um * e o nome da variavel de "lixo" normalmente se usa *_ 

nome1 , nome2, *lista_nomes = ["Bella", "Joao", "Maria"]

print(nome2)

Tuplas ou tuples
--> lista imutaveis ou seja nao tem como alterar o valor delas dps de definidas
--> tanto tuplas e listas podem ser convertidas uma para outra basta colocar tuple(variavel) ou list(variavel)
"""

lista_nomes = ["Bella", "Joao", "Maria"]

for indice, nome in enumerate(lista_nomes):
    print(f"{indice}-> \t{nome}")