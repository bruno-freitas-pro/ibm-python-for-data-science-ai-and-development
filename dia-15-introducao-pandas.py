###### EXEMPLO 1 ######

import pandas as pd
 
dicionario2 = {
    'chave1': 1,
    'chave2': 'joey',
    'chave3': (1, 2, 3),
    'bolinhadegude': [4, 5, 6],
    ('chave5', 'chave18'): 1,
    'chave nova': 'Van Halen'
}
 
dicionario2_quadro = pd.DataFrame(dicionario2)
print(dicionario2_quadro)

###### EXEMPLO 2 ######

#criar o dicionário
Carros2021 = {
    'Ranking' : ['1º', '2º', '3º', '4º', '5º', '6º', '7º', '8º', '9º', '10º', '11º', '12º', '13º', '14º', '15º', '16º', '17º', '18º', '19º', '20º', '21º', '22º', '23º', '24º', '25º', '26º', '27º', '28º', '29º', '30º', '31º', '32º', '33º', '34º', '35º', '36º', '37º', '38º', '39º', '40º', '41º', '42º', '43º', '44º', '45º', '46º', '47º', '48º', '49º', '50º'],
    'Marca' : ['Hyundai', 'Fiat', 'Jeep', 'Chevrolet', 'Jeep', 'Volkswagen', 'Fiat', 'Hyundai', 'Volkswagen', 'Chevrolet', 'Renault', 'Chevrolet', 'Toyota', 'Honda', 'Volkswagen', 'Nissan', 'Toyota', 'Volkswagen', 'Fiat', 'Hyundai', 'Renault', 'Toyota', 'Volkswagen', 'Fiat', 'Citroën', 'Volkswagen', 'Honda', 'Volkswagen', 'Peugeot', 'Fiat', 'Toyota', 'Chevrolet', 'Caoa', 'Renault', 'Toyota', 'Nissan', 'Caoa', 'Honda', 'Renault', 'Ford', 'Renault', 'Peugeot', 'Volkswagen', 'Honda', 'Chevrolet', 'Fiat', 'Honda', 'BMW', 'Fiat', 'Nissan'],
    'Modelo' : ['HB20', 'Argo', 'Renegade', 'Onix', 'Compass', 'Gol', 'Mobi', 'Creta', 'T-Cross', 'Onix Plus', 'Kwid', 'Tracker', 'Corolla', 'HR-V', 'Nivus', 'Kicks', 'Corolla Cross', 'Voyage', 'Cronos', 'HB20S', 'Duster', 'Yaris Hatcback', 'Virtus', 'Uno', 'C4 Cactus', 'Polo', 'Civic', 'Fox', '208', 'Siena', 'Hilux SW4', 'Spin', 'Chery Tiggo 5X', 'Sandero', 'Yaris Sedan', 'Versa', 'Chery Tiggo 8', 'WR-V', 'Logan', 'Ka', 'Captur', '2008', 'Taos', 'Fit', 'Cruze Sedan', 'Pulse', 'City', '320i', 'Dobló', 'V-Drive'],
    'Emplacamentos' : [86.455, 84.644, 73.913, 73.623, 70.906, 66.228, 65.847, 64.759, 62.307, 54.707, 52.916, 50.757, 41.891, 38.406, 36.664, 36.524, 34.249, 28.593, 27.887, 25.568, 22.457, 21.126, 20.563, 20.555, 19.552, 19.196, 18.949, 17.946, 16.342, 15.355, 13.641, 13.005, 12.555, 12.442, 12.436, 11.107, 10.462, 10.329, 9.478, 8.464, 8.304, 7.747, 7.732, 7.138, 7.09, 6.724, 6.138, 5.428, 5.355, 4.963]
}
import pandas as pd
df = pd.DataFrame(Carros2021)
print(df)

print(df[['Marca', 'Modelo']]) #>> Coloque entre colchetes duplos!


###### LOCALIZANDO VALORES ######

#importar o pandas
import pandas as pd

#criar o dicionário
dicionario = {
    'Coluna0' : ['0, 0 (A)', '1, 0 (E)', '2, 0 (I)', '3, 0 (M)', '4, 0 (Q)', '5, 0 (U)'],
    'Coluna1' : ['0, 1 (B)', '1, 1 (F)', '2, 1 (J)', '3, 1 (N)', '4, 1 (R)', '5, 1 (V)'],
    'Coluna2' : ['0, 2 (C)', '1, 2 (G)', '2, 2 (K)', '3, 2 (O)', '4, 2 (S)', '5, 2 (W)'],
    'Coluna3' : ['0, 3 (D)', '1, 3 (H)', '2, 3 (L)', '3, 3 (P)', '4, 3 (T)', '5, 3 (X)']
}
 
#criar o dataframe
df = pd.DataFrame(dicionario)

#imprimir pra conferir
print(df)

### LOCALIZANDO VALORES COM BASE NO ÍNDICE ###

#imprimir com base na localização dos inteiros
#Troque as posições para testar!
print(df.iloc[0, 0])

### LOCALIZANDO VALORES COM BASE NO NOME DA COLUNA ###

print(df.loc[0, 'Coluna3'])




###### IMPRIMIR UM SLICE (FATIA) ######

#Slice usando índice
slice = df.iloc[1:4, 0:4]
print(slice)

#Slice usando coluna
slice_col = df.loc[1:3, 'Coluna1':'Coluna2']
print(slice_col)
