###### Obter dados de um csv ######

#Criar um arquivo csv na pasta temporária

!echo -e 'bruno@exemplo.com.br;202;Bruno;Freitas\nisabela@exemplo.com.br;34304;Isabela;Capetti\nmariana@exemplo.com.br;22209;Mariana;Silva\npedro@exemplo.com.br;3082;Pedro;Peterson' > /tmp/emails.csv

#importar o pandas
import pandas as pd

#Criar uma variável pra ler o arquivo
arquivo_csv = '/tmp/emails.csv'

#Criar um DataFrame a partir do CSV e indicar o separador
df = pd.read_csv(arquivo_csv, sep=';')

#Nomear as colunas do DataFrame:
df.columns = ['Email', 'Matrícula', 'Nome', 'Sobrenome']

#Imprimir pra ver como ficou
print(df)


#Criar uma função que extrai um arquivo csv
def extrair_csv(arquivo_base):
    dataframe = pd.read_csv(arquivo_base)
    return dataframe
