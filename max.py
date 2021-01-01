'''
    Program to find the maximam from the given list
'''

def get_max(numbers):
    max = num[0]
    for i in range(1,len(num)):
        if  num[i] > max:
            max = num[i]
    return max

num =[]

while True :
    num1 =input('Enter the number:')
    if num1 == ' ':
        break
    else:
        num.append(int(num1))

print('Maximnum from given list is:',get_max(num))