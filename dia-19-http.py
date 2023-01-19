######## IMPORTAÇÃO DE TEXTO ########
######## SEM PAYLOAD ########

import requests
site = 'https://www.google.com.br'
solicitacao = requests.get(site)

print(solicitacao.status_code)

print(solicitacao.encoding)

print(solicitacao.text[0:100])

print(solicitacao.request.body)

print(solicitacao.headers)

#primeiro, vamos salvar o dicionário numa variável
cabecalho = solicitacao.headers
 
#consultamos algo... pode ser a data e depois o tipo de conteúdo:
print(cabecalho['Date'])
print(cabecalho['Content-Type'])


######## COM PAYLOAD ########

#URL base
http_get = 'http://httpbin.org/get'
 
#carga útil
payload = {
'Nome': 'Bruno',
'Idade': 29
}
 
#Criar a variável pra gerar a consulta
consulta = requests.get(http_get, params=payload)

print(consulta)

print(consulta.url)

print(consulta.request.body)

print(consulta.status_code)

print(consulta.text)

print(consulta.headers)

print(consulta.headers['Content-Type'])

print(consulta.json())







######## IMPORTAÇÃO DE IMAGEM COM PYTHON IMAGE LIBRARY (PIL) ########

#importar requests
import requests
 
#importar PIL
from PIL import Image
 
#atribuir a imagem a uma variável
get_image = requests.get('https://engenheirodedadosbaixarenda.files.wordpress.com/2022/05/meme-canetas-coloridas.jpg').content
 
#Criar um arquivo na pasta temporária
with open ('/tmp/imagem.jpg', 'wb+') as i:
    i.write(get_image)
    visualizar = Image.open(i)
    visualizar.show()


    
    
######## IMPORTAÇÃO DE IMAGEM COM TKINTER ########

#importar requests
import requests
 
#importar tkinter
import tkinter as tk
 
#importar PIL
from PIL import Image, ImageTk
 
#atribuir a imagem a uma variável
get_image = requests.get('https://engenheirodedadosbaixarenda.files.wordpress.com/2022/05/meme-canetas-coloridas.jpg').content
 
#Criar um arquivo na pasta temporária
with open ('/tmp/imagem.jpg', 'wb+') as i:
    i.write(get_image)
    root = tk.Tk()
    visualizar = ImageTk.PhotoImage(Image.open(i))
    tk.Label(root, image=visualizar).pack()
    root.mainloop()




######## ENVIO DE POST ########

#criar a variável contendo o endereço e a rota usada pra postar
http_post = 'http://httpbin.org/post'

#criar uma variável que vai gerar o POST
postagem = requests.post(http_post, data=payload)




######## OUTRAS VERIFICAÇÕES ########

#comparar as URLs da consulta e da postagem
print('URL da consulta:', consulta.url)
print('URL do post:', postagem.url)

#comparar o corpo da consulta e da postagem
print('corpo da consulta:', consulta.request.body)
print('corpo do post:', postagem.request.body)

print(postagem.json())

print(postagem.json()['form'])
