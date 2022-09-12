import pandas as pd
import numpy as np

papers = pd.read_csv("https://docs.google.com/spreadsheets/d/17b_d24WF2dRBedatAqgArWodAaAn6-o0/export?format=csv&gid=1924642330")
papers = papers[papers['ano'] > 2014]

researchers = pd.read_csv("https://docs.google.com/spreadsheets/d/17b_d24WF2dRBedatAqgArWodAaAn6-o0/export?format=csv&gid=1531675683")
researchers = researchers.assign(universidad='ucla')

grupos = pd.read_csv("https://docs.google.com/spreadsheets/d/1cBgEyyYtEyx0fvBmsRi4Yv6J2Iptv1T9AVIhp2KVmk4/export?format=csv&gid=165819311")

#Hipotesis 1
# La clasificación de los investigadores influye positivamente en la calidad de la producción científica.
papersA = papers.assign(autores=papers.autores.str.split(", ")).explode('autores')
inves = researchers.loc[:, ['integrantes', 'clasification']]

h1 = pd.merge(papersA, inves, left_on='autores', right_on='integrantes')
h1 = h1.drop(columns='integrantes')
h1 = h1.loc[:, ['autores', 'clasification', 'grupo', 'titulo', 'SJR_Q', 'categoria_revista']]

#Hipotesis 2
#La clasificación de los investigadores influye positivamente en la cantidad de la producción científica.
h2 = researchers.loc[:, ['integrantes', 'grupo', 'clasification', 'articulos']]

#Hipotesis 3
#La clasificación de los investigadores influye positivamente en el impacto de la producción científica.

#Hipotesis 4
#El tiempo de duración del grupo de investigación influye positivamente en la calidad de la producción.
papersB = papers.loc[:, ['grupo', 'titulo', 'categoria_revista', 'SJR_Q', 'ano']]
gruposA = grupos.loc[:, ['grupo', 'fecha_creacion']]

h4 = pd.merge(papersB, gruposA, left_on='grupo', right_on='grupo')