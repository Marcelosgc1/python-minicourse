# QUESTÃO 5
eng=0
com=0
mat=0

je=0
jc=0
jm=0

ve=0
vc=0
vm=0

se=0
sc=0
sm=0

while True:
    al = int(input('Que curso você faz? [1 - Engenharia; 2 - Computação; 3 - Matemática]: '))
    id = int(input('Qual a sua idade? '))
    
    # ENGENHARIA
    if(al==1):
        eng+=1
        se+=id
        if(id>ve):
            ve=id
        if(19<id<26):
            je+=1
    
    # COMPUTAÇÃO
    elif(al==2):
        com+=1
        sc+=id
        if(id>vc):
            vc=id
        if(19<id<26):
            jc+=1
    
    # MATEMÁTICA
    elif(al==3):
        mat+=1
        sm+=id
        if(id>vm):
            vm=id
        if(19<id<26):
            jm+=1

    e = int(input('Todos os dados já foram informados? [1 para Sim; 2 para Não]: '))
    if (e==1):
        break
####################################################################################

# LETRA A)
print(f'O curso de engenharia tem {eng} alunos, o de computação tem {com} e o de matemática {mat}')

# LETRA B)
print(f'O curso de engenharia tem {je} alunos entre 20 e 25 anos, o de computação tem {jc} alunos entre 20 e 25 anos e o de matemática tem {mat} alunos entre 20 e 25 anos')

# LETRA C)
if(ve>=vc) and (ve>=vm):
    print(f'O curso com o aluno mais velho é o de Engenharia, o aluno tem {ve} anos de idade!')
elif(vc>=vm):
    print(f'O curso com o aluno mais velho é o de Computação, o aluno tem {vc} anos de idade!')
else:
    print(f'O curso com o aluno mais velho é o de Matemática, o aluno tem {vc} anos de idade!')

# LETRA D)
if((se/eng)<=(sc/com)) and ((se/eng)<=(sm/mat)):
    print(f'O curso com a menor média de idade é a de Engenharia, com {round((se/eng), 2)} de média')
elif((sc/com)<=(sm/mat)):
    print(f'O curso com a menor média de idade é a de Computação, com {round((sc/com), 2)} de média')
else:
    print(f'O curso com a menor média de idade é a de Matemática, com {round((sm/mat), 2)} de média')