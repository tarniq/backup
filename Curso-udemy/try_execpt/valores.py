Valor1 = input("Digite o primeiro valor: ")
Valor2 = input("Digite o segundo valor: ")
conferir = Valor1.isdigit()
conferir2 = Valor2.isdigit()

try:
    Valor1_float = float(Valor1)
    Valor2_float = float(Valor2)
    if Valor1_float > Valor2_float:
        print(f"{Valor1_float} é maior que {Valor2_float}")
    elif Valor1_float < Valor2_float:
        print(f"{Valor1_float} é menor que {Valor2_float}")
    elif Valor1_float == Valor2_float:
        print ("NUMEROS IGUAIS")
except:
    print("voce nao digitou um nuemro")
    

