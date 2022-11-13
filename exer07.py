#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

distancia = float(input('Uma distância em metros: '))
cm = distancia * 100
mm = distancia * 1000
hm = distancia / 100
dam = distancia / 10
dm = distancia * 10

print('A medida de {} corresponde a: \n{} km \n{} mm \n{} hm \n{} dam \n{} dm'.format(distancia, cm, mm, hm, dam, dm))
