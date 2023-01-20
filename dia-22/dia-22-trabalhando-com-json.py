###### Criar uma função que extrai um arquivo json ######

import json
import pandas as pd

#Criando um arquivo json de exemplo
!echo '[\
  {\
    "Email": "bruno@exemplo.com.br",\
    "Matrícula": 202,\
    "Nome": "Bruno",\
    "Sobrenome": "Freitas"\
  },\
  {\
    "Email": "isabela@exemplo.com.br",\
    "Matrícula": 34304,\
    "Nome": "Isabela",\
    "Sobrenome": "Capetti"\
  },\
  {\
    "Email": "mariana@exemplo.com.br",\
    "Matrícula": 22209,\
    "Nome": "Mariana",\
    "Sobrenome": "Silva"\
  },\
  {\
    "Email": "pedro@exemplo.com.br",\
    "Matrícula": 3082,\
    "Nome": "Pedro",\
    "Sobrenome": "Peterson"\
  }\
]' > /tmp/emails.json

#Como abrir o arquivo json

with open ('/tmp/emails.json', 'r') as openfile:
    objeto_json = json.load(openfile)
print(objeto_json)

#Como extrair o arquivo json para um dataframe
def extrair_json(arquivo_base):
    dataframe = pd.read_json(arquivo_base,lines=True)
    return dataframe
