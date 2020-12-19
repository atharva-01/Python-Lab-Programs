'''
    Program to find the square root of the number by the newton's method
'''

def get_sqt(num , precision):
    sqt = num
    while abs(num - sqt*sqt )> precision:
        sqt = (sqt + num/sqt) / 2
    return sqt
num = int(input("Enter the number :"))
precision = float(input('Enter the precision :'))

print(get_sqt(num, precision))
