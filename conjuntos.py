A = {1, 2, 3, 4}

B = {3, 4, 5, 6, 7}


A.add(2)

numeros = [1,2,3,2,1,4,5,3,2,1]
numeros_unicos = list(set(numeros))
print(numeros_unicos)

test = {10,'hola',1.0, False}


A = {1, 2, 3, 4}

B = {3, 4, 5, 6, 7}

A.union(B)
A | B

A.intersection(B)
A & B

A.difference(B)
A - B
B.difference(A)
B - A

A.symmetric_difference(B)
(A - B) | (B - A)
A ^ B

numeros = list(range(1000))
#%timeit 500 in numeros -> mais lento
numeros_set = set(numeros)
#%timeit 500 in numeros_set -> mais rapido