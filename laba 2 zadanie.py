import random
m = random.randint(1,100)
x = 0
while x !=m :
    x = float(input("число: "))
    if x < m :
        print("У меня больше")
    elif x > m :
        print("У меня меньше")
    elif x == m :
        print("победа")
    
