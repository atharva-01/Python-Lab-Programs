'''

    Program to find the gcd(greatest commom divisor) of two numbers

'''

def find_gcd(a, b):
     while b:
         a,b = b , a % b
     return a

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

print("The gcd of numbers",num1,"and",num2,"is",find_gcd(num1,num2))

'''

    To find gcd of more than two numbers enter the numbers ,give space and hit enter to exit the while loop

'''


numbers = []
while True:
    inp = input("Enter the number :")
    if inp == ' ':
        break 
    else:
        numbers.append(int(inp))

gcd = find_gcd(numbers[0],numbers[1])
for i in range(2, len(numbers)):
    gcd = find_gcd(gcd, numbers[i])

print("The gcd of numbers",numbers,"is",gcd)