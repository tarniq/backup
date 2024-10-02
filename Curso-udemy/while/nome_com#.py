nome = input("Digite seu nome: ")
nome_L_contagem = len(nome)
indice_soma = 0
novo_nome = "" 
while indice_soma < nome_L_contagem:
      letra = nome [indice_soma]
      novo_nome += (f"{letra}♥")
      (indice_soma) += 1

print(f'♥{novo_nome}')
   