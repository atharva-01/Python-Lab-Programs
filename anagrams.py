'''
    Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function called in 
    is_anagram that takes two strings and returns True if they are anagrams.
    Example for anagrams:
    rat = tar , car = arc , elbow = below
'''

def is_anagram(str1, str2):
    list1 =[]
    list2= []
    for i in str1 :
        if i != ' ' :
            list1.append(i)
    for j in str2:
        if j != ' ':
            list2.append(j)
    list1.sort()
    list2.sort()
    if list1 == list2 :
        return True
    else :
        return False

print(is_anagram('dormitory','dirty room'))