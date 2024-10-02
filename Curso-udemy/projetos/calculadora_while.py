Entrada = input("Voce deseja entrar na calculadora ? ")
Entrada = Entrada.lower().startswith("s")
conta = ""
while Entrada == True:

    print ("="*35)

    Primeiro_numero = input("Digite o Primeiro numero: ")
    Segundo_numero = input("Digite o Segundo numero:  ")
    #validação dos numeros digitados.
    try:
          Primeiro_numero_int = int (Primeiro_numero)
          Segundo_numero_int = int (Segundo_numero)
    except:
          print("Voce nao digitou um numero tente outra vez!!")
          continue 

    print ("="*35)
    #Escolha de opeção.
    
    print("Qual operaçao deseja realizar ?")
    Operador = input("Digite ""+"" para realizar somar, ""-"" para subitrair, ""*"" para mutiplicar e ""/"" para dividir, insira a resposta: ")

    #validação de operador
    Operador_permitidos = "+-*/"
    try:
          if Operador not in Operador_permitidos:
                print("Voce nao digitou uma operaçao valida, tente outra vez!")
                continue
          if len(Operador) > 1:
                print("Voce digitou mais de uma operaçao, tente uma por vez!")
                continue
    except:
          print("Voce nao digitou nenhuma operaçao tente outra vez!!")
          continue
    
    #Operações
    if Operador == "+":
          conta = (Primeiro_numero_int + Segundo_numero_int)
          
    if Operador == "-":
          conta = (Primeiro_numero_int - Segundo_numero_int)
        
    if Operador == "*":
          conta = (Primeiro_numero_int * Segundo_numero_int) 

    if Operador == "/":
          conta = (Primeiro_numero_int / Segundo_numero_int)

    print ("="*35)
    #resultado final
    print(f"O resultado da operaçao {Primeiro_numero_int} {Operador} {Segundo_numero_int} é: {conta}!! ")

    print ("="*35)

    sair = input("Voce deseja [S]air ? ")
    sair = sair.lower().startswith("s")

    if sair == True:
            break

print("Ok, até mais!")