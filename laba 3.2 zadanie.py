def SumOfOddNumbers(List):
    summa = 0
    for number in List:
        if number % 2:
            summa +=number
    return summa

def OrimeNumber(x):
    if x ==1:
        return 0
    for i in rage(2, x):
        if x % i ==0:
            return 0
        return x
List = [4,6,2,1,19,43,21,3,112,7]
print ('Сумма нечетных чисел - ', SumOfOddNumbers(List))
