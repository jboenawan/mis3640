AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
numbers = [42, 123]
empty = []
# print(AFC_east, numbers, empty)

AFC_east[3] = 'New York Giants'
# print(AFC_east)

# print('Buffalo Bills' in AFC_east)


L = [
        ['Apple', 'Google', 'Microsoft'],
        ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
        ['Adam', 'Bart', 'Lisa']    
]

# print(L[1][2][1])

# for team in AFC_east:
#     print(team)

numbers = [2, 0, 1, 6, 9]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    
numbers = [2, 0, 1, 6, 9]
new_numbers = [number * 2 for number in numbers]    
# print(new_numbers)   

my_list = ['spam', 1, ['New England Patriots',  'Buffalo Bills', 'Miami Dolphins', 'New York Giants'], [1, 2, 3]]
# print(len(my_list))
# print(len(my_list[2]))

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
# print(c)

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

print(only_upper('Babson College'))