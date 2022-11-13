#Escreva um programa que converta uma temperatura digitada ºC e converta para ºF.

temperatura = float(input('Informe a temperatura em °C: '))
conversao = temperatura * 9/5 + 32

print('A tempertura de {} °C  corresponde a {} °F'.format(temperatura, conversao))