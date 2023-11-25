# código de geração do gráfico
import pandas as pd,seaborn as sns, matplotlib.pyplot as plt

#Abertura de arquivo CSV para extração dos dados
with open(file='gasolina.csv',mode='r',encoding='utf8') as arquivo:
  dados_df = pd.read_csv(arquivo)

#Plotagem do gráfico de linha com os dados do dados
with sns.axes_style('whitegrid'):
  grafico_gasolina = sns.lineplot(data=dados_df,x='dia',y='venda',color='green')
  grafico_gasolina.set(title='Preço de venda por dia em julho de 2021',ylabel = 'Preço de Venda(R$)',xlabel='Dias')
  grafico_gasolina.figure.set_size_inches(w=25/2.54,h=15/2.54)

  #Plotagem do gráfico de linha com os dados do dados_df
  plt.savefig('gasolina.png')