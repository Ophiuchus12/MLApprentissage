#listes vs numpy -> tailles en mémoire et performances

import numpy as np
import sys

#MEMOIRE

N = 10000
py_list = list(range(N))
np_array = np.array([py_list])

# taille réelle d'une liste Python = conteneur + objets int
size_py_true = sys.getsizeof(py_list) + sum(sys.getsizeof(x) for x in py_list)

# taille réelle NumPy = structure + données compactes
size_np_true = sys.getsizeof(np_array) + np_array.nbytes

print("Taille totale liste Python :", size_py_true)
print("Taille totale tableau NumPy :", size_np_true)
print("Rapport liste / NumPy :", size_py_true / size_np_true)

#PERFORMANCES
import time

max_value = 100_000_000
list_1 = list(range(1, max_value + 1))
start_time = time.time()
sum_list_1 = sum(list_1)
end_time = time.time()
print(f"Performance somme liste Python jusqu'à {max_value : ,}")
print(f"Somme liste Python : {sum_list_1 : ,}")
print("Temps liste Python :", end_time - start_time, "secondes")

list2 = np.array(np.arange(max_value + 1), dtype='int64')
start_time = time.time()
sum_list2 = np.sum(list2)
end_time = time.time()
print(f"Performance somme tableau NumPy jusqu'à {max_value : ,}")
print(f"Somme tableau NumPy : {sum_list2 : ,}")
print("Temps tableau NumPy :", end_time - start_time, "secondes")