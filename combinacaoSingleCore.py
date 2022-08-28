import os
import random
import sys

os.system('clear')

# print('********************')
# print('** CHUVA OBI-2022 **')
# print('** Single Core **')
# print('********************')

TAMANHO_MEDICAO = int(sys.argv[1])

combinacoes = []
tam_medicoes = TAMANHO_MEDICAO 
#int(input('Qtas. medições? '))
#print('\nCombinações: ')
for i in range(0, 2**tam_medicoes):
  x = bin(i)
  combinacoes.append(x.split('b')[1].zfill(tam_medicoes))
#print(combinacoes)
#print()
soma_usuario = 10 
#int(input('Qual a soma? '))
medicao = random.sample(range(1, TAMANHO_MEDICAO + 1), TAMANHO_MEDICAO) 
#input('Digite os valores (%d valores com espaços entre eles): ' %tam_medicoes).split(' ')

total = 0
for l in combinacoes:
  soma = 0
  fatores = list(l)
  for pos in range(0, len(l)):
    soma += int(fatores[pos]) * int(medicao[pos])
  if soma == soma_usuario:
    total += 1
    #print(medicao)
    #print(fatores)
    #print()
#print('Total de combinações com a soma: %d' % total)