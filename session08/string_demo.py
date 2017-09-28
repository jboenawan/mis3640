team = 'New England Patriots'

letter = team[0]
# print(len(team))

# print(team[len(team)-1])
# print(team[-1])

# index = 0
# for i in range(len(team)):
#     if team[i] != ' ':
#         print(team[i])

# for letter in team:
#     if letter.isalpha():
#         print(letter)



prefixes = 'JKLMNOPQ'
suffix = 'ack'
# for letter in prefixes:
#     if letter in ['O', 'Q']:
#         letter = letter+'u'    
#     print(letter + suffix)

# for letter in prefixes:
#     if letter != 'O' and letter != 'Q':
#         print(letter + suffix)
#     else:
#         print (letter +'u'+ suffix)

team = 'New England Patriots'
# print(team[0:11])
# print(team[12:20])

# print(team[ : 11])
# print(team[12:])

# print(team[::-2])

# print(team[::2])

team = 'New England Patriots'
# team[12:20] = 'Seahawks'


new_team = team[:12] + 'Beavers'
# print(team)
# print(new_team)

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

# print(find(team, 'W'))

def count(word, letter):
    lowerword = word.lower()
    c = 0
    for x in lowerword:
        if x == letter.lower():
            c = c + 1
    return c

vowels = 'aeiou'
number_of_vowels = 0
for letter in vowels:
    number_of_vowels += count(team, letter)

print(number_of_vowels)

print(count(team, 'N'))
