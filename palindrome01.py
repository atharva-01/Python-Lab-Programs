''' 
    Program to check whetehet the given string is palidrome or not.
    palidrome - is a sting which reads  backwards as forwards

'''

def isPalindrome(s):
    return s == s[::-1]

s = input('Enetr the string:')
if isPalindrome(s) :
    print('Yes',s,'is Palidrome')
else:
    print('No',s,'is not Palidrome')