import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

site = 'https://www.imdb.com/chart/top/'
consulta = requests.get(site)
html = consulta.text
soup = BeautifulSoup(html, 'html5lib')

#Criar uma lista
imdb_top_250 = []

#Procurar os dados da tabela no HTML
tabela_base = soup.find('table')
tabela_corpo = tabela_base.find('tbody')

#Extrair os dados da tabela e salvá-los numa lista
for i, linha in enumerate(tabela_corpo.find_all('tr')):

    #Obter o ranking do filme - strip() se livra dos espaçamentos no início e fim da frase
    ranking = linha.find(class_='titleColumn').contents[0].strip()
    
    #Eliminar o ponto ao final da string e convertê-lo em número inteiro
    ranking = int(ranking[0:(len(ranking)-1)])
    
    #Obter o título do filme
    titulo = linha.find(class_='titleColumn').a.text
    '''
    Obter o nome do diretor e dos atores principais:
        'find' procura pela coluna de título
        'a' acessa a tag HTML '<a>'
        'get' obtém o atributo 'title' da tag '<a>'
        'split()' separa os nomes dentro da string
    '''
    nomes = linha.find(class_='titleColumn').a.get('title').split(', ')
    
    #Remover o ' (dir.)' que fica no final do nome do diretor
    nomes[0] = nomes[0].replace(' (dir.)','')
    
    #Obter o ano a partir do formato '(0000)'
    ano = int(linha.find(class_='secondaryInfo').text[1:5])
    
    #Obter a nota do IMDB
    nota_imdb = float(linha.find(class_='imdbRating').text)
    
    #Adicionar cada dicionário à lista 'imdb_top_250'
    imdb_top_250.append({
        'Ranking': ranking,
        'Título': titulo,
        'Diretor': nomes[0],
        'Estrelas': nomes[1::],
        'Ano': ano,
        'Nota do IMDB': nota_imdb
        })

#Converter para um dataframe
df = pd.DataFrame(imdb_top_250)

#Imprimir em formato de tabela
print(df)

#Salvar para um arquivo
filename = 'file'
fileExtension = '.txt'
destination = Path(filename).with_suffix(fileExtension)
df.to_csv(destination)
