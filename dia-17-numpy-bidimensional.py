import numpy as np

###### CRIAR UM ARRAY COM BASE EM UMA LISTA ######

lista1 = [[1, 2, 3, 4], [11, 12, 13, 14], [21, 22, 23, 14]]
array1 = np.array(lista1)
print(array1)

###### CONFERIR OS ATRIBUTOS DE UM ARRAY BIDIMENSIONAL ######

#Tamanho
print(array1.size)

#Número de dimensões
print(array1.ndim)

#Forma
print(array1.shape)

###### SLICING ######
lista1 = [[1, 2, 3, 4], [11, 12, 13, 14], [21, 22, 23, 14]]
array1 = np.array(lista1)

#Imprimir o primeiro elemento do array (nesse caso, uma lista)
print(array1[0])

#Imprimir os dois primeiros elementos do array (nesse caso, duas listas)
print(array1[0:2])

#Imprimir o primeiro elemento, da primeira lista
print(array1[0, 0])

#Imprimir o segundo e o terceiro elementos da primeira lista
print(array1[0, 1:3])

#Imprimir só o primeiro elemento/coluna de todas as listas
print(array1[:,0])

#Imprimir do segundo ao último elementos/colunas de todas as listas
print(array1[:,1:])

#Imprimir do primeiro ao segundo elementos desde a segunda até a última lista
print(array1[2:,0:2])

#Imprimir do primeiro ao segundo elementos da segunda e terceira lista
print(array1[1:3,0:2])






###### OPERAÇÕES MATEMÁTICAS ######

a = np.array([[4, 8], [3, 7]])
b = np.array([[1, 0], [5, 2]])
print(a) #só pra conferir
print(b) #só pra conferir


#Adição
print(a+b)
print(np.add(a, b))


#Subtração
print(a-b)
print(np.subtract(a, b))


#Multiplicação de matriz por escalar
print(np.multiply(2, a))
print(2*a)


#Multiplicação de matrizes - produto de Hadamard - se aplica a matrizes com as mesmas dimensões
print(a*b)
print(np.multiply(a,b))

#Multiplicação de matrizes - produto do ponto - se aplica quando o número de linhas de uma é igual ao número de colunas da outra.
print(np.dot(a, b))


#Mais um exemplo
A = np.array([[1, 2], [3, -1]])
B = np.array([[1, -2, 3], [2, 4, 0]])
print(A) #só pra conferir
print(B) #só pra conferir
print(np.dot(A, B))

#Divisão
print(a/b)
print(np.divide(a,b))
