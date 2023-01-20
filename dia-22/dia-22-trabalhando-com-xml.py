###### Obter dados de um arquivo xml ######

import pandas as pd

#Criar um arquivo csv na pasta temporária
echo '<?xml version="1.0" encoding="utf-8"?><listaDeEmails><pessoa><Email>bruno@exemplo.com.br</Email><Matricula>202</Matricula><Nome>Bruno</Nome><Sobrenome>Freitas</Sobrenome></pessoa><pessoa><Email>isabela@exemplo.com.br</Email><Matricula>34304</Matricula><Nome>Isabela</Nome><Sobrenome>Capetti</Sobrenome></pessoa><pessoa><Email>mariana@exemplo.com.br</Email><Matricula>22209</Matricula><Nome>Mariana</Nome><Sobrenome>Silva</Sobrenome></pessoa><pessoa><Email>pedro@exemplo.com.br</Email><Matricula>3082</Matricula><Nome>Pedro</Nome><Sobrenome>Peterson</Sobrenome></pessoa></listaDeEmails>' > /tmp/emails.xml

#Criar uma função que extrai um arquivo csv
def extrair_xml(arquivo_base):
    dataframe = pd.DataFrame(columns=["nome", "altura", "peso"])
    tree = etree.parse(arquivo_base)
    root = tree.getroot()
    for pessoa in root:
        nome = pessoa.find("nome").text
        altura = float(pessoa.find("altura").text)
        peso = float(pessoa.find("peso").text)
        dataframe = dataframe.append({"nome":nome, "altura":altura, "peso":peso}, ignore_index=True)
    return dataframe
