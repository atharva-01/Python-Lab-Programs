'''
    Write a function called is_sorted that takes a list as parameter and returns True if the list is sorted in asending
    order and False othrewise. For example:
    (i) is_sorted([1,2,2]) returns True
    (ii) is_sorted(['b','a']) returns False
    
'''
def is_sorted(test_list):
      
    if (test_list == sorted(test_list)) :
        return True
    else:
        return False

test_list =['a','c','d']
print(is_sorted(test_list)) 