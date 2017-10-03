# fin = open('words.txt')
# line = fin.readline()
# print(repr(line))


# fin = open('words.txt')
# for line in fin:
#     word = line.strip()
#     print(word)

def find_long_words():
    """
    prints only the words with more than 20 characters
    """
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word, len(word))

# find_long_words()

def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter “e” in it
    """
    for letter in word:
        if letter.lower() == 'e':
            return False
    return True
    # return not 'e' in word.lower()

# print(has_no_e('Babson'))
# print(has_no_e('College'))
# print(has_no_e('EA'))

def find_words_no_e():
    fin = open('words.txt')
    counter_no_e = 0
    counter_total = 0
    for line in fin:
        counter_total +=1
        word = line.strip()
        if has_no_e(word):
            # print(word)
            counter_no_e += 1
    return counter_no_e/counter_total

# print('The percentage of the words with no "e" is {:.2f}%.'.format(find_words_no_e()*100))

def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

# print(avoids('Babson', 'e'))
# print(avoids('College', 'e'))

def find_words_no_vowels():
    fin = open('words.txt')
    counter_no_vowel = 0
    counter_total = 0
    for line in fin:
        counter_total +=1
        word = line.strip()
        if avoids(word, 'aeiouy'):
            print(word)
            counter_no_vowel += 1
    return counter_no_vowel/counter_total

print('The percentage of the words with vowel letters is {:.2f}%.'.format(find_words_no_vowels()*100))