from cProfile import label
from xml.dom.minidom import TypeInfo
import matplotlib.pyplot as plt
import pandas as pd

dadosSingle = pd.read_csv('saidaSigleCore.dat', sep=';', header=None)

dadosMulti = pd.read_csv('saidaMultiCore.dat', sep=';', header=None)

listDadosSingle = dadosSingle.values.tolist()
listDadosMulti = dadosMulti.values.tolist()

plt.style.use('ggplot')
#plt.style.use('seaborn')
plt.plot(dadosSingle[0], dadosSingle[1], ls='-', lw='1', marker='o', label='SingleCore')
plt.plot(dadosMulti[0], dadosMulti[1], ls='-', lw='1', marker='o', label='MultiCore')
plt.title('Time comparison between SingleCore and MultiCore')
plt.grid()
plt.legend(loc="upper left")
plt.show()
