#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1 + nota2) / 2


print('A média do aluno está entre {} e {} é igual a: {}'.format(nota1, nota2, media))