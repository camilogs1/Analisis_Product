import numpy as np
import pandas as pd

## Lectura de archivos
papers = pd.read_csv('https://docs.google.com/spreadsheets/d/1OFg9Jzypg_uwsmFxyXFSgtdfXfgsN9AG/export?format=csv&gid=808772593')
papers['ano'] = pd.to_numeric(papers['ano'], errors='coerce')
papers = papers.dropna(subset=['ano'])
papers['ano'] = papers['ano'].astype(int)
papers = papers[papers['ano'] > 2014]

researchers = pd.read_csv('https://docs.google.com/spreadsheets/d/1mpwR15wHbrFbO1s8DWsDdLta_aou7gHD/export?format=csv&gid=2102359855')
researchers['universidad'] = researchers['grupo']

## Investigadores en internos y externos
authors_others = papers[['id', 'autores', 'ano']]
authors_others = authors_others.explode('autores')
authors_others = authors_others.groupby(['id']).mean()
