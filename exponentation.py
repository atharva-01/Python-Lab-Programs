'''
    Program to find the exponent of the given number to the power given by user
'''

def get_exp(base ,power):
     pow = 1
     for i in range(power):
         pow = pow * base
     return pow

base = float(input('Enter the base :'))
power = int(input('Enter the power :'))

print('The value of number whose base is',base,'and power is',power,'is:',get_exp(base,power))