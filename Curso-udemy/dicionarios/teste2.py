
alunos = {}
while True:
    alunos['nome'] += input("Digite o nome do aluno: ")
    alunos['idade'] += input("Digite a idade do aluno: ")
    escolha = input("O que deseja fazer agora [A]dicionar mais alunos, [V]er lista de alunos, [S]air")
    
    if escolha == "A":
        continue
    
    elif escolha == "V":
        print(alunos)
    
    break