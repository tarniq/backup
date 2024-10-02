frase = '[23:43, 30/04/2024] meu denguinho ♥️💜: toma olha como fico lindo meu denguinho ♥️💜: sim shxvjdidudjeod meu denguinho ♥️💜: preggs (ta do meu lado meu denguinho ♥️💜: mas a outra valia nota msm amor? meu denguinho ♥️💜: vai nao amor meu denguinho ♥️💜: vc é inteligente meu denguinho ♥️💜: e esforcado'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes <= qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)