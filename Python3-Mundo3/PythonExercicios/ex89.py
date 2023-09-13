notas = list()
aluno = list()

while True:
    nome = str(input('Digite o nome do aluno: '))
    notas.append(float(input('Digite a primeira nota: ')))
    notas.append(float(input('Digite a segunda nota: ')))
    aluno.append(nome)
    aluno.append(notas[:])
    notas.clear()
    opção = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while opção not in 'SN':
        print('Tente novamente!', end = ' ')
        opção = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if opção == 'N':
        break
    k = 1
print('#=' * 20)
for i in range(0, len(aluno), 2):
    print(f'BOLETIM DO {k}º ALUNO ({aluno[i].upper()}):')
    print(f'MÉDIA FINAL: {(aluno[i+1][0] + aluno[i+1][1]) / 2:.1f}')
    print('#=' * 20)
    k += 1
    
while True:
    opção = int(input('''Deseja ver as notas de qual aluno?
(DIGITE O NÚMERO 999 PARA ENCERRAR): '''))
    if opção == 999:
        break
    if 0 < opção <= (len(aluno)) / 2:
        print('=' * 35)
        print(f'AS NOTAS DO ALUNO(A) {aluno[2*(opção-1)].upper()} SÃO:') 
        print(f'N1: {aluno[2*(opção-1) + 1][0]}')
        print(f'N2: {aluno[2*(opção-1) + 1][1]}')
        print('=' * 35)
    else:
        print('=' * 50)
        print('ALUNO NÃO CADASTRADO!!!, DIGITE NOVAMENTE')
        print('=' * 50)
