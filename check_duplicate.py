'''
    Write a function called has_duplicate that takes a list and returns True if there is any duplicate element that 
    appears more than once. It should not modify the original list.

'''
def has_duplicate(list1):
    ss = set(list1)
    if len(ss) < len(list1):
        return True
    else:
        return False

print(has_duplicate(['one','two','three','one']))