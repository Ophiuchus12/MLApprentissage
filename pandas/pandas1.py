import pandas as pd

print (pd.__version__)

#Creation d'un dataframe à partir d'un dictionnaire

dataSet = pd.DataFrame({ 'Col1' : [1, 2, 3, 4],
                         'Col2' : ['A', 'B', 'C', 'D'],
                         'Col3' : [10.5, 20.5, 30.5, 40.5] })

print (f"My Dataframe from dictionary:\n{dataSet}")
print (f"Type of dataSet: {dataSet.dtypes}")

#modifier le type d'une colonne
dataSet['Col1'] = dataSet['Col1'].astype('float64')
print (f"\nDataframe after changing type of Col1:\n{dataSet}")
print (f"\nType of dataSet: {dataSet.dtypes}")

#Indiquer que les clés soit utiliser comme index
dataSet2 = pd.DataFrame.from_dict({ 'Col1' : [1, 2, 3, 4],
                         'Col2' : ['A', 'B', 'C', 'D'],
                         'Col3' : [10.5, 20.5, 30.5, 40.5] }, orient = 'index')

print (f"\nMy Dataframe from dictionary with keys as index:\n{dataSet2}")


#Creation d'un dataframe à partir d'un tableau numpy
import numpy as np

np_array = np.array ([[1,2,3],[4,5,6],[7,8,9]])
dataSet3 = pd.DataFrame(np_array, columns=['Col1', 'Col2', 'Col3'])
print (f"\nMy Dataframe from numpy array:\n{dataSet3}")

np_array[0,0]= 99

print (f"\nDataframe after modifying an element:\n{dataSet3}")