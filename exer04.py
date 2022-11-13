#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

numero=int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1

print('Analisando o número: {}, seu antecessor é:  {}, e o seu sucessor é: {}'.format(numero, antecessor, sucessor))


#Outra forma:

n = int(input('Digite um número: '))
print('Analisando o número {}, seu antecessor é: {}, seu sucessor é: {}'.format(n, (n-1), (n+2)))