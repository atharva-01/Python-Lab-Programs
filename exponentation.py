'''
    Program to find the exponent of the given number to the power given by user
'''

def get_exp(base ,power):
    value = base ** power
    return value

base = float(input('Enter the base :'))
power = float(input('Enter the power :'))

print('The value of number whose base is',base,'and power is',power,'is:',get_exp(base,power))