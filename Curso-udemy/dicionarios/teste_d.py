def registro_aluno(*args):
    alunos = {} 
    def resgistro_nomes(nome):
        ...
        alunos['nome'] = nome
        
        return(resgistro_nomes)
    
    def resgistro_idades(idade):
        alunos['idade'] = idade
        
        return(resgistro_idades)
      
    return(alunos)

while True:
    nome = "thales" #input("Digite o nome do aluno: ")
    idade = "18" #input("Digite a idade do aluno: ")
    escolha = "V" #input("O que deseja fazer agora [A]dicionar mais alunos, [V]er lista de alunos, [S]air")
    
    if escolha == "A":
        continue
    
    elif escolha == "V":
        print(registro_aluno(nome,idade))
    
    break