# #EXERCICIO 1 - A

# import matplotlib.pyplot as plt
# from IPython.display import display
# import pandas as pd

# #criação do conjunto de dados
# dados = [["investir em mais ações", 562], ["investir em mais títulos", 144], ["não investir", 288], ["investir o mesmo valor de 2012", 461]]
# tabela = pd.DataFrame(dados, columns=["Intenções de investimento", "Frequencia"])
# display(tabela)

# #para criar a página
# figura = plt.figure()

# #para criar o gráfico
# pizza = plt.pie(tabela["Frequencia"], labels=tabela["Intenções de investimento"], autopct='%1.1f%%', shadow=True, startangle=90)

# #para mostrar o gráfico na página
# plt.show()

# #EXERCICIO 1 - B

# import pandas as pd
# import matplotlib.pyplot as plt
# from IPython.display import display

# #criação dos dados
# dados = [["Estados Unidos", 15], ["Itália", 4], ["Etiópia", 2], ["África do Sul", 2], ["Tanzânia", 1], ["Quênia", 9], ["México", 4], ["Marrocos", 1], ["Grã-Bretanha", 1], ["Brasil", 2], ["Nova Zelândia", 1]]
# tabela = pd.DataFrame(dados, columns=["Nacionalidade dos vencedores da prova masculina", "Frequência"])
# display(tabela)

# #criando a página para aparecer o gráfico de pizza
# figura = plt.figure()

# #para criar o gráfico
# pizza = plt.pie(tabela["Frequência"], labels=tabela["Nacionalidade dos vencedores da prova masculina"], autopct='%2.1f%%', shadow=True, startangle=90)

# #para mostrar o gráfico na página
# plt.show()

# EXERCICIO 2

# import pandas as pd
# import matplotlib.pyplot as plt
# from IPython.display import display

# #criação dos dados
# dados = [["América do Norte", 15], ["Europa", 5], ["África", 13], ["América Central",4], ["América do Sul", 2], ["Oceania", 1]]
# tabela = pd.DataFrame(dados, columns=["Nacionalidade dos vencedores da prova masculina", "Frequência"])
# display(tabela)

# #criando a página para aparecer o gráfico de pizza
# figura = plt.figure()

# #para criar o gráfico
# pizza = plt.pie(tabela["Frequência"], labels=tabela["Nacionalidade dos vencedores da prova masculina"], autopct='%2.1f%%', shadow=True, startangle=90)

# #para mostrar o gráfico na página
# plt.show()




#EXERCICIO 3 - A

import pandas as pd
import matplotlib.pyplot as plt


# Criação do conjunto de dados
dados = pd.DataFrame({'Nº de medalhas': [44, 65, 104, 82, 88]})
dados.index = ['Alemanha', 'Grã-Bretanha','Estados Unidos','Rússia','China']

# Organizando os dados em ordem decrescente
dados = dados.sort_values(by='Nº de medalhas', ascending=False)

# Criação do gráfico de Pareto
from matplotlib.ticker import PercentFormatter

# Definição das cores
cor_barra = 'darkviolet'
cor_linha = 'red'
tam_linha = 4

# Construindo o gráfico básico (gráfico de barras)
fig, pareto = plt.subplots() #colocar varios gráficos em uma janela

pareto.bar(dados.index, dados['Nº de medalhas'], color=cor_barra)
pareto.set(xlabel='Países',
           ylabel='Nº de medalhas',
           title = 'Número de medalhas obtidas por atletas de cinco países nos Jogos Olímpicos de Londres - 2012')

# Inserção de rótulos nas barras do gráfico de Pareto
barras = pareto.patches #patches = configuração para modelar as barras
valores = dados['Nº de medalhas']

#zip = pegar dois conjuntos e transformar em um só (1º valor de uma lista com o 1º de outra e junta em um só e asssim suscessivamente)
for barra, valor in zip(barras, valores):
    altura = barra.get_height()
    pareto.text(barra.get_x()+barra.get_width()/2, altura,
                valor, ha='center', va='bottom')
    
# #para mostrar o gráfico na página
plt.show()

# #EXERCICIO 3 - B

