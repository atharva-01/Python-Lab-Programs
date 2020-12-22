'''
    Wrie the function called nested_sum that takes a list of lists of integers and adds up the element from all of 
    the elememt from all of the nested lists.
    Eg t = [[1,2][3],[4,5,6]]

    nested_sum(t) = 21

'''

def nested_sum(nested_list):
    sum = 0
    for i in nested_list:
        for j in i:
            sum = sum + j 
    return sum

nested_list = [[1,2],[3],[4,5,6]]
print("The sum of given list of lists of integers is:",nested_sum(nested_list))
