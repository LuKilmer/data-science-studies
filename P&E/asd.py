from collections import Counter

idade = [16, 17, 18, 16, 17, 16, 18, 17, 16, 18,
         17, 16, 18, 16, 17, 18, 16, 17, 16, 18,
         17, 18, 16, 17, 18, 16, 17, 16, 18, 17]

contador = Counter(idade)
print(list(contador.values()))
print(list(contador.keys()))