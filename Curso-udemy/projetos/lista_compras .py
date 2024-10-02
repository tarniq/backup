import os

entrada = input("Dseja faze uma lista de: ")
lista = []
while entrada:
    
    entrada_lista = input(f"O que deseja fazer na sua lista de {entrada} ? \n[I]nserir um novo intem, [A]pagar um item, [V]er a lista completa, [S]air para encerrar a lista : ")
    
    #Validaçao entrada

    if entrada_lista not in ["i","a","v","s"]:
        print("voce nao digitou uma das opçoes validas.")
        os.system('cls')
   
    #Inserir item novo

    elif entrada_lista.upper().startswith("I"):
        os.system('cls')
        lista.append(input("Digite o item: "))
    
    #Apagar item

    elif entrada_lista.upper().startswith("A"):
            
        if lista == []:
                
            os.system('cls')
                
            print("sua lista ainda nao contem nenhum item para apagar.")
            continue

        for n, i in enumerate(lista):
                print(n,i)

        indice = input("escolha um indice pra apagar: ")

        try:
             indice_int = int(indice)
             del lista [indice_int]
        except IndexError :
             print("Digite um indice valido.")
        except ValueError:
             print("Digite o numero do item que quer deletar")
             
    #Ver lista completa

    elif entrada_lista.upper().startswith("V"):
        
        os.system('cls')

        if lista == []:
                print("sua lista ainda nao contem nenhum item.")
        
        for n,i in enumerate(lista):
            print(n, i)
    
    #Sair da lista

    elif entrada_lista.upper().startswith("S"):
        print("Ate mais.")
        break