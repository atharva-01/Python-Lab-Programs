'''
    Finding the Factorial by defing function method
'''
def get_factorial (n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

'''
    Finding factorial by recursion function metohd
'''
def get_factorial_recursion (n):
    if n== 1 :
        return 1
    else :
        return  get_factorial_recursion(n-1) * n

num = int(input("Enter the number:"))

print("The factorial of",num,"is:",get_factorial(num))
print("The factorial of",num,"by recursion method is:",get_factorial_recursion(num))

