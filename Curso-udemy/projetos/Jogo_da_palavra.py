import random
print("="*24)
print("Jogo da Palavra Secreta")
print("="*24)

Entrada = input("Deseja jogar: ")
Entrada = Entrada.upper().startswith("S")

Palavras = ["raios", "funde", "bella", "amigo"]
palavra_secreta = random.choice(Palavras)
 
tentativa = 0


while Entrada == True:
    
    palavra_exibida = ""

    palavra_dig =  input("digite uma palavra: ")
    palavra_dig_lower = palavra_dig.lower()
    try:
        if not palavra_dig_lower.isalpha():
             print("voce nao digitou uma letra")
             continue
        
        elif len (palavra_dig_lower) < 5:
            print("Voce digitou menos de 5 letras")
            continue
        
        elif len (palavra_dig_lower) > 5:
            print("Voce digitou mais de 6 letras")
            continue

    except ValueError:
            print("voce nao digitou uma letra")

    for letra in palavra_secreta.lower():

        if letra in [palavra_dig_lower[0]] and palavra_secreta[0] in [palavra_dig_lower[0]]:
            palavra_exibida += f"{palavra_secreta[0]} "
            tentativa += 1
                
        elif letra in [palavra_dig_lower[1]] and palavra_secreta[1] in [palavra_dig_lower[1]]:
            palavra_exibida += f"{palavra_secreta[1]} "
            tentativa += 1

        elif letra in [palavra_dig_lower[2]] and palavra_secreta[2] in [palavra_dig_lower[2]]:
            palavra_exibida += f"{palavra_secreta[2]} "
            tentativa += 1

        elif letra in [palavra_dig_lower[3]] and palavra_secreta[3] in [palavra_dig_lower[3]]:
            palavra_exibida += f"{palavra_secreta[3]} "
            tentativa += 1

        elif letra in [palavra_dig_lower[4]] and palavra_secreta[4] in [palavra_dig_lower[4]]:
            palavra_exibida += f"{palavra_secreta[4]} "
            tentativa += 1

        else:
            palavra_exibida += "❌ "
            tentativa += 1

    if palavra_dig_lower == palavra_secreta:
        print ("Voce ganhou!!")

    elif tentativa < 25:
        print(palavra_exibida)
        continue
    
    else:
        print("Voce perdeu !!")
        
    continuar = input("Quer jogar outra vez ? --> ")    
    continuar = continuar.upper().startswith("S")

    if continuar == True:
           tentativa = 0
           continue
    else:
        print("Até mais!")
        break

    # a letra precisa estar na frase e no local certo, ou seja preciso comparar o local da letra que o usuario digitou com a letra da palavra aleatoria
    #Palavra_R = random.choice(Palavras)
    #Palavras = ["raios", "funde", "bella", "amigo"]
