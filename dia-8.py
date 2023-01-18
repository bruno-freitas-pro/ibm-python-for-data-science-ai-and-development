#dessa vez, vamos gerar um número aleatório
#importar o módulo random, que tem vários métodos
#pra gerar números aleatórios
import random

#declarar a variável hora
#queremos que seja hora cheia (inteiro)
#definir que hora é um valor aleatório (random)
#definir que hora é um valor entre 0 e 24 (uniform)
hora = int(random.uniform(0,24))

#Imprimir que horas são
#preste atenção nas vírgulas!
print ('são ', hora, ' horas')

#se a hora for
#maior ou igual que 8 E TAMBÉM menor que 18
if 8 <= hora <18:
    
#horário de trabalho é Verdadeiro
#o 'T' de 'True' deve ser maiúsculo
    horariodetrabalho = True
    
#do contrário, horário de trabalho é Falso
#o 'F' de 'False' deve ser maiúsculo
else:
    horariodetrabalho = False

#imprimir horariodetrabalho, pra conferir
print(horariodetrabalho)

#se NÃO é horariodetrabalho, imprima 'Vá descansar'
if not horariodetrabalho:
    print('Vá descansar um pouco')
    
#do contrário, imprima 'Vá trabalhar!'
else:
    print('Vá trabalhar!')

#o resultado esperado é ⬇⬇⬇
são  1  horas (a hora varia)
False
Vá descansar um pouco

OU

são 11 horas (a hora varia)
True
Vá trabalhar!
