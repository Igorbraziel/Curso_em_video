import random
str1 = str(input('Digite o primeiro nome: '))
str2 = str(input('Digite o segundo nome: '))
str3 = str(input('Digite o terceiro nome: '))
str4 = str(input('Digite o quarto nome: '))

vetor = [str1, str2, str3, str4]

print('O aluno escolhido foi: {}'.format(random.choice(vetor)))