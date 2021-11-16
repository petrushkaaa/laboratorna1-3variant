import random
a=list()
for i in range (0,100):
  a.append(random.randint(-100,100))
print('Массив',a,"\n")
min = a[-20]
for i in range(len(a)):
  if (a[i] < min):
    min = a[i]
    k=i
print (k)
print ('Минимальное значение: ',min)
def bubble_sort(a):
  swapped = True
  while swapped:
    swapped = False
    for i in range(len(a) - 1,):
      if i<k: 
        if a[i] > a[i + 1]:
          a[i], a[i + 1] = a[i + 1], a[i]
          swapped = True
