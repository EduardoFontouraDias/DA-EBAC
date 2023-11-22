import pandas as pd,seaborn as sns, matplotlib.pyplot as plt


#Abertura de arquivo CSV para extração dos dados
with open(file='./gasolina.csv',mode='r',encoding='utf8') as arquivo:
  dados = pd.read_csv(arquivo)

#Transformação dos dados em CSV para DataFrame do Pandas para manipulação
gasolina_df = pd.DataFrame(dados)
print(len(gasolina_df))
gasolina_df.head()

#Plotagem do gráfico de linha com os dados do gasolina_df
with sns.axes_style('darkgrid'):
  grafico_gasolina = sns.lineplot(data=gasolina_df,x='dia',y='venda',color = 'red')
  grafico_gasolina.set(title='Gráfico de variação do preço da gasolina',xlabel = 'Dias',ylabel = 'Preço(R$)')
  grafico_gasolina.figure.set_size_inches(w=25/2.54,h=10/2.54)

  #Salvar o arquivo como imagem no formato .png
  plt.savefig('gasolina.png')