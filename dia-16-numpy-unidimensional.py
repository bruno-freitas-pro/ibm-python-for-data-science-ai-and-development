###### CRIANDO UM ARRAY ######

import numpy as np
print(np.__version__)

array1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

###### CONFERINDO AS CARACTERÍSTICAS DO ARRAY ######

print(type (array1))

print(array1.dtype)

#quantos elementos tem o array?
print(array1.size) 

#Quantas dimensões tem o array?
print(array1.ndim)

#Quantos elementos existem em cada dimensão do array?
print(array1.shape)


###### ARRAY COM NÚMEROS REAIS ######

array2 = np.array ([3.14, 2.7182, 6.022, 1.618, 299.792458, 6.673, 6.626])
 
print(type(array2)) #tipo

print(array2.dtype) #tipo de dados contidos no array

###### ÍNDICES E SLICES DE ARRAYS ######

array3 = np.array([21, 1, 3, 5, 7, 9, 11])

array3[0] = 13 #substitui o elemento 0, que é 21, por 13

array3[4] = 8 #substitui quinto elemento, que é 7, por 8

print(array3)

array3[1:3] = 15, 17

print(array3)

array3b = array3[2:6] #selecionar do terceiro ao sexto elemento
print(type(array3b)) #conferir se o resultado é um ndarray
print(array3b) #imprimir os elementos do array3b

array3c = array3[2:6:2] #selecionar do terceiro ao sexto elemento, pulando um elemento e anotando um.
print(array3c)

array3d = array3[2:6:3] #selecionar do terceiro ao sexto elemento, em passos triplos.
print(array3d)

### MAIS EXEMPLOS ###

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

print(a[9:])   #imprimir do décimo ao último elemento
 
print(a[:5])   #imprimir do primeiro ao quinto elemento
 
print(a[::2])  #imprimir o array inteiro em passos de dois
 
print(a[::3])  #imprimir o array inteiro em passos de três
 
print(a[1::2]) #imprimir os ÍNDICES ímpares

#Selecionar elementos do array com base em uma lista 
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

selecao = [0, 2, 4, 6, 8, 10]
b = a[selecao] #Entre colchetes!
print(b)

#Trocar alguns elementos do array com base em uma lista de índices
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

selecao = [0, 2, 4, 6, 8, 10]

a[selecao] = 99
print(a)




###### OPERAÇÕES ARITMÉTICAS COM ARRAYS ######

#Soma
x = np.array([3, 2])
y = np.array([5, 1])
xy = x+y
print(xy)

x = np.array([3, 2])
y = np.array([5, 1])
xy = np.add(x, y)
print(xy)

x = [3, 2]
y = [5, 1]
xy = []
 
for n, m in zip(x, y):
    xy.append(n+m)
print(xy)

#Subtração
x = np.array([3, 2])
y = np.array([5, 1])
xy = x-y
print(xy)

x = np.array([3, 2])
y = np.array([5, 1])
xy = np.subtract(x, y)
print(xy)

#Multiplicação simples
ab = np.array([1, 2])
abc = 2*ab
 
print(abc)

ab = np.array([1, 2])
abc = np.multiply (2, ab)
 
print(abc)

#Multiplicação de dois arrays
x = np.array([3, 2])
y = np.array([5, 3])
xy = x*y
print(xy)

x = np.array([3, 2])
y = np.array([5, 3])
xy = np.multiply(x, y)
print(xy)

#Produto do ponto
x = np.array([3, 2])
y = np.array([5, 3])
ponto = np.dot(x, y)
print(ponto)

#Divisão
x = np.array([10, 100, 300])
y = np.array([5, 20, 3])
xy = x/y
print(xy)

x = np.array([10, 100, 300])
y = np.array([5, 20, 3])
xy = np.divide(x, y)
print(xy)

#Broadcasting
x = np.array([0, 1, 2, 3])
x = x+1
print(x)




###### FUNÇÕES UNIVERSAIS ######

#Média
array4 = np.array([-13, 3, 256, 7, 5, 9])
print(array4.mean())

#Máximo
array4 = np.array([-13, 3, 256, 7, 5, 9])
print(array4.max())

#Mínimo
array4 = np.array([-13, 3, 256, 7, 5, 9])
print(array4.min())

#Desvio padrão (standard deviation)
array4 = np.array([-13, 3, 256, 7, 5, 9])
print(array4.std())
 
array5 = np.array([1, 1, 1, 1])
print(array5.std())

#Mapeamento de arrays
a = np.array([0, np.pi/2, np.pi])
b = np.sin(a)
print(b)

#Espaçamentos lineares

#Espaçamento de meio centímetro
a = np.linspace(0, 4, num=9)
print(a)       #Conferir os elementos
print(type(a)) #Conferir o tipo de python
print(a.dtype) #Conferir o tipo de dados

#Espaçamento de um centímetro
a = np.linspace(0, 4, num=5)
print(a)       #Conferir os elementos
print(type(a)) #Conferir o tipo de python
print(a.dtype) #Conferir o tipo de dados

#Começar com um número negativo, considerando um espaçamento, por exemplo, de uma parede
a = np.linspace(-0.5, 4, num=10)
print(a)





###### IMPRIMIR REPRESENTAÇÕES GRÁFICAS ######
import matplotlib               #importa matplotlib
import matplotlib.pyplot as plt #importa matplotlib.pyplot com o apelido plt
x=np.linspace(0, 2*np.pi, 100)  #cria o array x, composto por 100 amostras com intervalos igualmente espaçados
y=np.sin(x)                     #calcula o seno de cada um dos 100 pontos do array x e salva essa informação no array y
matplotlib.use('TkAgg')         #indica ao matplotlib para usar o tkinter 
plt.plot(y, x)                  #cria um plot (basicamente, um gráfico). O eixo x será impresso na horizontal, e o eixo y na vertical.
plt.show()                      #imprime o gráfico na tela, usando o tkinter

#O código abaixo teoricamente funciona exatamente igual:
import matplotlib.pyplot as plt #importa matplotlib.pyplot com o apelido plt 
x=np.linspace(0, 2*np.pi, 100)  #cria o array x, composto por 100 amostras com intervalos igualmente espaçados
y=np.sin(x)                     #define que y é igual ao seno de x
plt.plot(y, x)                  #cria um plot (basicamente, um gráfico). O eixo x será impresso na horizontal, e o eixo y na vertical.
plt.show()                      #imprime o gráfico na tela, usando o tkinter

###### IMPRESSÃO DE ARRAY USANDO FOR ######
#Modo comum
import numpy as np
a = np.array([9, 8, 7])
 print(a)

#Modo lista
a = np.array([9, 8, 7])
for i in a:
    print(i)
