#1

list1 = [1, 2, 3, 2, 4, 1, 5, 3]

print(f"original list={list1}")

unique_list = []

for i in list1:

    if i not in unique_list:

        unique_list.append(i)

print(unique_list)



numbers = (4, 7, 1, 9, 2, 8, 5, 3, 6, 0)





#2

max_num = numbers[0]

min_num = numbers[0]

for i in numbers:

    if i > max_num:

        max_num = i

    if i < min_num:

        min_num = i

print(max_num)

print(min_num)





#3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for i in numbers:

    if i % 2 == 0:

        even_numbers.append(i)

print(even_numbers)





#4

string = "hello world"

char_count = {}

for char in string:

    if char in char_count:

        char_count[char] += 1

    else:

        char_count[char] = 1

print(char_count)





#5

primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}

n = int(input("Enter a number: "))

if n in primes:

    print("Yes")

else:

    print("No")





#6

list1 = [1, 2, 3, 4, 5]

list2 = [4, 5, 6, 7, 8]

set1 = set(list1)

set2 = set(list2)

intersection = set1 & set2

print(list(intersection))





#7

dict1 = {'a': 10, 'b': 20, 'c': 30}

dict2 = {'b': 5, 'c': 15, 'd': 25}

result = {}

for key in dict1:

    if key in dict2:

        result[key] = dict1[key] + dict2[key]

    else:

        result[key] = dict1[key]

for key in dict2:

    if key not in result:

        result[key] = dict2[key]

print(result)





#8

names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]

count = {}

for name in names:

    if name in count:

        count[name] += 1

    else:

        count[name] = 1

print(count)





#9

list1 = [1, 2, 3, 4, 5]

list2 = [2, 4]

result = []

for i in list1:

    if i not in list2:

        result.append(i)

list1=result

print(result)





#10

d = {}

n = int(input("How many key-value pairs? "))

for i in range(n):

    key = input("Enter key: ")

    value = input("Enter value: ")

    d[key] = value

search_key = input("Enter key to search: ")

if search_key in d:

    print(d[search_key])

else:

    print("Key not found")
