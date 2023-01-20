import glob                         #Ajuda a abrir os arquivos
import pandas as pd                 #Usado para várias tarefas
import xml.etree.ElementTree as ET  #Usado para tratar XML
from datetime import datetime       #Usado para marcar o horário no log

temp = "temp.tmp" #Arquivo temporário
arquivo_log = "log.txt" #Registro dos fatos
destino = "dados_transformados.csv" #Destino na etapa de carregamento (load)

###### ETAPA DE EXTRAÇÃO ######

def extrair_csv(arquivo_base):
    dataframe = pd.read_csv(arquivo_base)
    return dataframe

def extrair_json(arquivo_base):
    dataframe = pd.read_json(arquivo_base,lines=True)
    return dataframe

def extrair_xml(arquivo_base):
    tree = ET.parse(arquivo_base)
    root = tree.getroot()
    cabecalho = ["nome", "altura", "peso"]
    dataframe = pd.DataFrame(columns = cabecalho)
    for pessoa in root:
        nome = pessoa.find("nome").text
        altura = float(pessoa.find("altura").text)
        peso = float(pessoa.find("peso").text)
        dataframe_xml = pd.DataFrame([[nome, altura, peso]], columns = cabecalho)
        dataframe = pd.concat([dataframe, dataframe_xml], ignore_index = True)
    return dataframe

def extract():
    #Criar um dataframe vazio pra receber os dados
    dados_extraidos = pd.DataFrame(columns=['nome','altura','peso'])
     
    #Processar os arquivos CSV
    for csv in glob.glob("*.csv"):
        dados_extraidos = pd.concat([dados_extraidos, extrair_csv(csv)], ignore_index=True)
     
    #Processar os arquivos JSON
    for json in glob.glob("*.json"):
        dados_extraidos = pd.concat([dados_extraidos, extrair_json(json)], ignore_index=True)
     
    #Processar os arquivos XML
    for xml in glob.glob("*.xml"):
        dados_extraidos = pd.concat([dados_extraidos, extrair_xml(xml)], ignore_index=True)
     
    return dados_extraidos

###### ETAPA DE TRANSFORMAÇÃO ######
def transform(dados):
        #Converter polegadas pra metros
        #Converter os dados pra 'float'
        dados.altura = dados.altura.astype(float)
        #Arredondar pra duas casas decimais
        dados['altura'] = round(dados.altura * 0.0254, 2)
         
        #Converter libras pra quilos
        #Converter os dados pra 'float'
        dados.peso = dados.peso.astype(float)
        #Arredondar pra duas casas decimais
        dados['peso'] = round(dados.peso * 0.45359237, 2)
        return dados

###### ETAPA DE CARREGAMENTO ######
def load(destino, dados_exportados):
    dados_exportados.to_csv(destino)

###### REGISTRO NO LOG ######
def log(mensagem):
    #Definir o formato de data-hora
    formato_data_hora = '%Y-%m-%d-%H:%M:%S.%f'
     
    #Obter a data e hora atuais
    agora = datetime.now()
     
    #Converter a data e a hora para o formato desejado
    data_hora = agora.strftime(formato_data_hora)
     
    #Gravar as informações no log
    with open(arquivo_log,"a") as logfile:
        logfile.write(data_hora + ',' + mensagem + '\n')

log("Processo de ETL iniciado!")

log("Extração iniciada!")
dados_extraidos = extract()
print('dados extraídos:\n', dados_extraidos, '\n')
log("Fim da extração")

log("Transformação iniciada!")
dados_transformados = transform(dados_extraidos)
print('dados transformados: \n', dados_transformados, '\n')
log("Transformação finalizada!")

log("Carregamento iniciado!")
load(destino, dados_transformados)
log("Carregamento finalizado!")

log("Processo ETL finalizado!")
