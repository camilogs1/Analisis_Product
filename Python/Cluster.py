import pandas as pd

grupos = pd.read_csv('info_grupos_merged_separado_instituciones.csv')
grupos = grupos.drop_duplicates()

instituciones = grupos[['codigo del grupo', 'instituciones']]

integrantes = pd.read_csv('info_integrantes.csv')

articulos = pd.read_csv('articulos.csv')
count_articulos = articulos['grupo'].value_counts().reset_index()
count_articulos.rename(columns={'index': 'grupo','grupo':'Cantidad'}, inplace = True)

investigadores = pd.merge(integrantes, instituciones, left_on='codigo_grupo', right_on='codigo del grupo')

cluster = investigadores[['instituciones', 'categoria', 'posgrado']]

#Categoria
cluster1 = pd.get_dummies(cluster, columns=['categoria'])
cluster1.columns = ['instituciones', 'posgrado', 'Investigador_Asociado', 'Investigador_Emerito', 'Borrar', 'Investigador_Junior', 'Investigador_Senior']
cluster1 = cluster1.drop(['Borrar'], axis='columns')

#Posgrado
cluster2 = pd.get_dummies(cluster1, columns=['posgrado'])
cluster2.columns = ['instituciones', 'Investigador_Asociado', 'Investigador_Emerito', 'Investigador_Junior', 'Investigador_Senior', 'Doctorado', 'Especialidad_medica', 'Especializacion', 'Maestria/Magister', 'No_Informado', 'Perfeccionamiento', 'Pregrado/Universitario', 'Primaria', 'Primaria_Incompleta', 'Secundaria', 'Tecnico-Nivel_Medio', 'Tecnico-Nivel_Superior']
cluster2 = cluster2.drop(['Primaria', 'Primaria_Incompleta', 'Secundaria'], axis='columns')

#Contar por institución
U_count = cluster2.groupby(['instituciones'])['instituciones', 'Investigador_Asociado', 'Investigador_Emerito', 'Investigador_Junior', 'Investigador_Senior', 'Doctorado', 'Especialidad_medica', 'Especializacion', 'Maestria/Magister', 'No_Informado', 'Perfeccionamiento', 'Pregrado/Universitario', 'Tecnico-Nivel_Medio', 'Tecnico-Nivel_Superior'].agg('sum').reset_index()
