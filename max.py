def get_max(numbers):
    max = num[0]
    for i in range(1,len(num)):
        if  num[i] > max:
            max = num[i]
    return max

num = [58 , 89 ,56 ,98]
print(get_max(num))