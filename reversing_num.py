'''
    Program to print the reverse of given number
'''
'''
    BY STRING METHOD
'''

def reverse(n):
    r = n[::-1]
    return r 

inp = input('Enter the number:')
print("Reverse of",inp,"is",reverse(inp))

'''
    BY INTEGER METHOD
'''
def get_reverse(n):
    rev = 0
    while(n > 0): 
        a = n % 10
        rev = rev * 10 + a 
        n = n // 10
    return rev

num = int(input('Enter the numner:'))
print("Reverse of",num,"is",get_reverse(num))
