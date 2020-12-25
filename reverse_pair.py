'''
    Two words are a 'reverse pair' if each is the reverse of the other. Write a program that finds all the reverse 
    pairs in the word list.

'''
def reversing_str(word_list):
    reverse_pair_list = []
    for i in word_list :
        r = i[::-1]
        reverse_pair_list.append(r)
    return reverse_pair_list

print(reversing_str(['one','two','three']))