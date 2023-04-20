def print_upper_words(words):
    '''
    For a list of words, print out each word on a separate line, but all uppercase. 
    '''
    for word in words:
        print (word.upper())

print ('words from uppercase', print_upper_words(["hello", "hey"]))   

def print_upper_words2(words):
    '''
    For a list of words, print out each word that starts from the letter 'e' (either upper or lowercase)
    '''
    for word in words:
        if word[0] == 'e' or word[0] == 'e':
            print (word.upper())

print ('words from uppercase starting on E', print_upper_words2(["hello", "hey", 'egg', 'eager']))

def print_upper_words3(words, must_start_with):
    '''
    Print the words that only start from certain letters from  must_start_with
    '''
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print (word.upper())

print ('words from uppercase starting on a certain letter', print_upper_words3(["hello", "hey", 'egg', 'eager', 'apple'], must_start_with = {'h', 'a'}))