# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela

a = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(a)}')
print(f'Só tem espaços? {a.isspace()}')
print(f'É um número? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em maiúsculas? {a.isupper()}')
print(f'Está em minúsculas? {a.islower()}')
print(f'Está capitalizado? {a.istitle()}')


#Usando if e else "sim e não."


a = input('Digite algo: ')

print('O tipo primitivo desse valor é:', type(a))
print('Só tem espaços?:', 'Sim.' if a.isspace() else 'Não.')
print('É um numero?:', 'Sim.' if a.isnumeric() else 'Não.')
print('É um alfabético?:', 'Sim.' if a.isalpha() else 'Não.')
print('É um alfanumérico?:', 'Sim.' if a.isalnum() else 'Não.')
print('Está em maiúsculo?:', 'Sim.' if a.isupper() else 'Não.')
print('Está em minúsculo?: ', 'Sim.' if a.islower() else 'Não.')
print('Está capitalizada?:', 'Sim.' if a.istitle() else 'Não.')