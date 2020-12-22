'''
    Write a function called cumsum that takes a list of numbers and returns the cumulative sum; that is, a new list 
    where the i th element is the sum of the first +1 elements from the original list.
    Eg: t = [1,2,3]
    cumsum(t) = [1,3,6]

'''
def cumsum(num_list):
    new_list=[] 
    j=0
    for i in range(0,len(num_list)):
        j += num_list[i]
        new_list.append(j)
    return new_list

num_list = [1,2,3]
print(cumsum(num_list))