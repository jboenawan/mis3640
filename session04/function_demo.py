def print_lyrics():
    print("Hey Jude. Don't make it bad.")
    print("Take a sad song and make it better.")

# print_lyrics()

# print(type(print_lyrics))

def repeat_lyrics():
    print_lyrics()
    print('Na - na - na - na - na, na - na - na - na')
    print_lyrics()

# repeat_lyrics()

def print_twice(name):
    print(name)
    print(name)

# print_twice('Andrew')

my_name = 'Zhi'
# print_twice(my_name)

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
#cat_twice(line1, line2)
#print(line1)

def give_me_a_break():
    str1 = 'break'
    return str1

# print(give_me_a_break()*10)

def give_me_a_break():
    str1 = 'break'    
    print('another break')
    return str1
    
print(give_me_a_break())


