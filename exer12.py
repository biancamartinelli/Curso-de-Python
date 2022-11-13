#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Digite o salário do funcionário: R$ '))
aumento = salario + (salario *0.15)

print('Um funcionário que ganhava {}, com 15% de aumento, passa a receber {:.2f}'.format(salario, aumento))
