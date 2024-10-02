nome = input('copie e cole um texto: ')
encontrar = input('Digite o que deseja encontrar nesse texto: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não no texto')
    