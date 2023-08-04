# QUESTÃO 5 
num_alunos = 10
alu_freq = 0
alu_nota = 0
alu_aprov = 0
ch = int(input("Informe a carga horaria em horas da disciplina: "))
for i in range (num_alunos):
    nota = float(input("Informe a nota final do aluno: "))
    presença = int(input("Informe a presença em horas do aluno: "))
    if presença<ch*(3/4):
        alu_freq+=1
    elif nota<5.0:
        alu_nota+=1
    else:
        alu_aprov+=1
print(f'{alu_aprov} alunos foram aprovados na disciplina')
print(f'{alu_nota} alunos foram reprovados pela nota na disciplina')
print(f'{alu_freq} alunos foram reprovados por falta de frequência na disciplina')