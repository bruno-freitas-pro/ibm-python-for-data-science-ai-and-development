import requests
from bs4 import BeautifulSoup

#Obter o código HTML
site = 'https://www.imdb.com/chart/top/'
consulta = requests.get(site)
html = consulta.text

#Pedir ao BS4 para ler o código e salvá-lo em uma variável
soup = BeautifulSoup(html, 'html5lib')

#Conferir o título da página
print(soup.title)

#Conferir qual é a primeira heading tag de cada nível
headings = (soup.h1, soup.h2, soup.h3, soup.h4, soup.h5, soup.h6)
 
for i in headings:
    if i is not None:
        print(i.name,': ',i)                      #Com espaço indesejado
        print(i.name,': ',i, sep='')              #Sem espaço indesejado

#Imprimir a primeira tabela presente na página
print(soup.table)

#Encontrar elementos seguindo a árvore...
print(soup.table.thead)
print(soup.table.tbody)
print(soup.table.tbody.tr)

#Exemplificando elemento pai
elemento_filho = soup.th
elemento_pai = elemento_filho.parent
print(elemento_pai)

#Apresentar o irmão com next_sibling e deixar o texto mais apresentável com prettify
elemento = soup.table.tbody.tr
irmao_1 = elemento.next_sibling.next_sibling
print(irmao_1.prettify())

#Apresentar os atributos de um determinado elemento
filme_1_ancora = soup.table.tbody.tr.td.next_sibling.next_sibling.a
print(filme_1_ancora.attrs)

#Descobrir o nome do filme, que é uma string
filme_1_ancora = soup.table.tbody.tr.td.next_sibling.next_sibling.a
print(filme_1_ancora.string)

#Descobrir os conteúdos da linha inteira, ainda de forma desordenada
filme_1_ranking = (soup.table.tbody.tr.td.next_sibling.next_sibling.contents)
print(filme_1_ranking)

#Descobrir apenas o ranking, em vez de descobrir todos os conteúdos da linha
filme_1_ranking = int(float(soup.table.tbody.tr.td.next_sibling.next_sibling.contents[0]))
print(filme_1_ranking)

#Descobrir o ano de lançamento do filme
filme_1_ano = soup.table.tbody.tr.td.next_sibling.next_sibling.span
print(filme_1_ano)

filme_1_ano = soup.table.tbody.tr.td.next_sibling.next_sibling.span.text[1:5]
print(filme_1_ano)

nota_imdb = float(soup.table.tbody.tr.td.next_sibling.next_sibling.next_sibling.next_sibling.text)
print(nota_imdb)

###### FIND_ALL ######
#Encontrar todas as linhas de todas as tabelas da página de uma vez só
linhas_tabela = soup.find_all('tr')
print(linhas_tabela)

#Encontrar todas as linhas de todas as tabelas da página e depois imprimir só as primeiras duas linhas
linhas_tabela = soup.find_all('tr')
print(linhas_tabela[0:2])

#Imprimir linha por linha, indicando o número da linha e seu conteúdo
linhas_tabela = soup.find_all('tr')
for i, linha in enumerate(linhas_tabela[0:2]):
    print("A linha", i, "é:", linha)

#Segregando mais a informação: separando célula por célula
linhas_tabela = soup.find_all('tr')
for i, linha in enumerate(linhas_tabela[0:3]):
    print("linha", i)
    celulas = linha.find_all(['th', 'td'])
    for j, celula in enumerate(celulas):
        print('coluna', j, 'conteúdo da célula:', celula)


### Opcionalmente, podemos salvar o conteúdo de todas as tabelas da página em uma lista ###
lista = soup.find_all(name=['tr', 'td'])
print(lista)


#Coletar todas as tags href de uma só vez
lista2 = soup.find_all(href=True)
 
#imprimir só os primeiros três itens da lista:
print(lista[0:3])

### Opcionalmente, podemos salvar apenas as tags href que estejam dentro da tabela ###
lista = soup.table.find_all(href=True)
#imprimir só os primeiros três itens da lista:
print(lista[0:3])

### Pesquisa por strings ###
busca_string = soup.find_all(string='(1994)')
print(len(busca_string))

busca_string = soup.find_all(string='Matrix')
print(busca_string)

import re
busca_string = soup.find_all(string=re.compile("Senhor"))
print(busca_string)

###### FIND (encontrar apenas o primeiro registro) ######
import re
busca_string = soup.find(string=re.compile("Senhor"))
print(busca_string)

###### USANDO CLASSES DO HTML PRA ENCONTRAR ELEMENTOS ######
nota_imdb = []
for i in soup.find_all('td', class_='imdbRating'):
    i = i.text
    i = float(i)
    nota_imdb.append(i) 
import pandas as pd
print(pd.DataFrame(nota_imdb))

###### OBTENDO OS LINKS DAS IMAGENS ######
#Apenas obter os links
for image in soup.find_all('img', limit=2):
    print(image)
    print(image.get('src'))

#Obter os links e salvá-los em uma lista
images_links = []
for image in soup.find_all('img', limit=2):
    images_links.append(image.get('src'))
print(images_links)
