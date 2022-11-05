#Instructor             = Assoc.Prof. Dr.Seyhun Altunbay
#Student ID             = 19COMP1047
#Student Name           = Batuhan Küçük
#Course & Section Name  = CSE598.1 DATA ANALYTICS

def getSum(n):
    sum = 0
    while (n != 0):
        sum = sum + (n % 10)
        n = n // 10

    return sum

number = int(input("Please enter number between 0 and 1000: "))
print(getSum(number))