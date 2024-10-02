lista_m = []
entrada = True
while entrada is True:
    entrada_op = int(input("1 para ver sua lista, 2 para adicionar itens, 3 para remover itens, 4 para mexer itens de lugar: "))
    if entrada_op == 1:
        print(lista_m)
    elif entrada_op == 2:
        item_add = input ("qual item deseja adicionar: ")
        lista_m.append(item_add)
    elif entrada_op == 3:
        print (lista_m)
        item_pop = int(input("qual item quer remover da lista: "))
        lista_m.pop(item_pop)
