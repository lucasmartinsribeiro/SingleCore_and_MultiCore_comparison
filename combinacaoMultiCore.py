from mpi4py import MPI

import os
import sys
import random

os.system('clear')

# print('********************')
# print('** CHUVA OBI-2022 **')
# print('** Multi Core **')
# print('********************')

tam_medicoes = int(sys.argv[1])

combinacoes = []

comm = MPI.COMM_WORLD
id = comm.Get_rank()
number_processes = comm.Get_size()

start = round(id * ((2**tam_medicoes) / number_processes))
end = round(start + ((2**tam_medicoes) / number_processes) -1)

# print('Processo %d' %(id))
# print('inicializo em: %d - finalizo em: %d' %(start, end))

for i in range(start, end + 1):
  x = bin(i)
  combinacoes.append(x.split('b')[1].zfill(tam_medicoes))
# print(combinacoes)
# print()

soma_usuario = 10
medicao = ''
for x in range(0,tam_medicoes):
    medicao += str(random.randint(1, 10)) + ' '
medicao = medicao[:len(medicao) -1].split(' ')


total = 0
for l in combinacoes:
  soma = 0
  fatores = list(l)
  for pos in range(0, len(l)):
    soma += int(fatores[pos]) * int(medicao[pos])
  if soma == soma_usuario:
    total += 1
    # print(medicao)
    # print(fatores)
    # print()
#print('Total de combinações com a soma do Multi-Core: %d' % total)