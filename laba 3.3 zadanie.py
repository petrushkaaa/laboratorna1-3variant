from random import random
a = []
for i in range(20):
    n = int(random() * 100) - 50 
    print(n, end=', ')
    if n > 0:
        a.append(n)
print()
print(a)
