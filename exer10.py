#Faça um programa q leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta pinta uma área de 2m².
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de {} x {} e sua área é de: {} m² '.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {} litros de tinta'.format(tinta))
