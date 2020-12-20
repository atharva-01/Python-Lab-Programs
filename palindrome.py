'''
    A palindrome is a word that is spelled the same backward and forward, like “noon” and “redivider”. Recursively, a word
    is a palindrome if the first and last letters are the same and the middle is a palindrome.The following are functions
    that take a string argument and return the first, last, and middle letters:
     def first(word):    
          return word[0] 
     def last(word):  
            return word[-1] 
     def middle(word): 
            return word[1:-1]
    1. Type these functions into a file named palindrome.py and test them out. What happens if you call middle with a
     string with two letters? One letter? What about the empty string, which is written “” and contains no letters?
    2. Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False
       otherwise. Remember that you can use the built-in function len to check the length of a string.

'''
def first(word):    
    return word[0] 
def last(word):  
    return word[-1] 
def middle(word): 
    return word[1:-1]

def is_palindrome(word):
    if first(word) == last(word) and middle(word) == word[1:-1]:
        return True
    else :
        return False

word = input('Enter the word:')
print(is_palindrome(word))

'''
    When function middle is called with two letters or one letter or with "" no letters it returns empty value.
'''