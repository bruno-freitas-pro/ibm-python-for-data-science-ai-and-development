###### Tabela maiores vencedores da F1 ######

### Modo rápido, porém pouco preciso ###

#Importar tudo que vamos precisar
import pandas as pd
#Indicar qual é o site
url = 'https://en.wikipedia.org/wiki/List_of_Formula_One_Grand_Prix_winners'
#Obter todos os dataframes
lista_de_dataframes = pd.read_html(url, flavor='bs4')
print(lista_de_dataframes[2])


### Outro modo rápido, um pouco mais preciso ###

#Caso não saibamos como encontrar a tabela, podemos usar o código abaixo:
#Importar tudo que vamos precisar
import pandas as pd
 
#Indicar qual é o site
url = 'https://en.wikipedia.org/wiki/List_of_Formula_One_Grand_Prix_winners'
 
#Obter todos os dataframes
melhores_pilotos = pd.read_html(url, match="Formula One Grand Prix winners", flavor='bs4')
 
#Imprimir o resultado
print(melhores_pilotos)




### Modo lento e com bastante precisão ###

#Importar tudo que vamos precisar
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Indicar qual é o site
url = 'https://en.wikipedia.org/wiki/List_of_Formula_One_Grand_Prix_winners'

#Obter o código HTML do site
dados = requests.get(url).text

#Criar uma variável chamada soup, que trata o código HTML
soup = BeautifulSoup(dados, 'html5lib')

#Criar uma varíável contendo só as tabelas
tabelas = soup.find_all('table')

#Procurar a tabela desejada, com base no título (caption) da tabela
for indice, tabela in enumerate(tabelas):
    if ('Formula One Grand Prix winners') in str(tabela.caption):
        indice_tabela = indice

#converter a tabela em string, e em seguida em DataFrame
maiores_vencedores_f1 = pd.read_html(str(tabelas[indice_tabela]), flavor='bs4')

#Imprimir o DataFrame
print(maiores_vencedores_f1)
