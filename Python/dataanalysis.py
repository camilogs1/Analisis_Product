import numpy as np
import pandas as pd

papers = pd.read_csv('https://docs.google.com/spreadsheets/d/1OFg9Jzypg_uwsmFxyXFSgtdfXfgsN9AG/export?format=csv&gid=808772593')
papers1 = papers['ano'] > 2014

researchers = pd.read_csv('https://docs.google.com/spreadsheets/d/1mpwR15wHbrFbO1s8DWsDdLta_aou7gHD/export?format=csv&gid=2102359855')

