'''
    Program to find the sum of digits in given number
'''

def get_sum(num):
    sum =0
    for i in num :
        sum += int(i)
    return sum

num = input("Enter the number:")

print("The sum of digits of number",num,"is",get_sum(num))
