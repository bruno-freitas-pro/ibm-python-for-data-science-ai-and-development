#Importar a API para usar usar os dados da CoinGecko
from pycoingecko import CoinGeckoAPI
 
#importar pandas e definir o apelido pd
import pandas as pd
 
#Definir um apelido para a API
cg = CoinGeckoAPI()
 
#Obter os preços
info_btc = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='brl', days=30)
 
#Gerar um dataframe só com os preços e códigos de data/hora
dados = pd.DataFrame(info_btc['prices'], columns=['TimeStamp', 'Preço (R$)'])
 
#Mostrar a data em formato humanizado
dados['Data'] = pd.to_datetime(dados['TimeStamp'], unit='ms')
 
#Organizar os dados que vamos usar pros candlesticks
dados_candlestick = dados.groupby(dados.Data.dt.date).agg({'Preço (R$)':['min', 'max', 'first', 'last']})
 
#importar os objetos gráficos do plotly
import plotly.graph_objects as go
 
#importar a ferramenta de plotagem
from plotly.offline import plot
 
#definir um gráfico >>>>>>>>>>>Mais observações>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
grafico = go.Figure(data=[go.Candlestick(x= dados_candlestick.index,                    #Indicar posições no eixo X
                                         open=dados_candlestick['Preço (R$)']['first'], #buscar o primeiro preço do dia
                                         high=dados_candlestick['Preço (R$)']['max'],   #buscar o preço máximo
                                         low=dados_candlestick['Preço (R$)']['min'],    #buscar o preço mínimo
                                         close=dados_candlestick['Preço (R$)']['last']) #buscar o último preço do dia
                    ])
 
#customizar o layout
grafico.update_layout(xaxis_rangeslider_visible=False, xaxis_title='Data', yaxis_title='Preço (R$)', title='Gráfico Candlestick de Bitcoin nos últimos 30 dias')
 
#plotar o gráfico
plot(grafico, filename='/tmp/grafico_candlestick_btc.html')
