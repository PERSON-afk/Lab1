# Program 1: Statistical Analysis Calculator
# This program calculates the average, median, and mode of a list of numbers entered by the user.
# It uses manual sorting algorithms and frequency counting to compute these statistical measures.

n = int(input("Enter number of elements: "))

nums_list = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    nums_list.append(num)

nums = tuple(nums_list)

# Average
total = 0
for num in nums:
    total += num
average = total / n
print("\nAverage:", average)

# Median
sorted_nums = list(nums)
for i in range(n):
    for j in range(i+1, n):
        if sorted_nums[i] > sorted_nums[j]:
            sorted_nums[i], sorted_nums[j] = sorted_nums[j], sorted_nums[i]

if n % 2 == 1:
    median = sorted_nums[n // 2]
else:
    median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
print("Median:", median)

# Mode
unique_vals = []
frequencies = []

for i in range(n):
    val = nums[i]
    if val in unique_vals:
        index = unique_vals.index(val)
        frequencies[index] += 1
    else:
        unique_vals.append(val)
        frequencies.append(1)

max_freq = max(frequencies)
modes = []
for i in range(len(unique_vals)):
    if frequencies[i] == max_freq:
        modes.append(unique_vals[i])

if max_freq == 1:
    print("Mode: No mode (all values appear only once)")
else:
    print("Mode:", modes[0] if len(modes) == 1 else f"Multiple modes: {modes}")


# Program 2: Character Frequency Counter
# This program counts the frequency of each alphabetic character in a text string,
# ignoring case and non-alphabetic characters, then displays the results in sorted order.

text = input("Enter text: ")

freq = {}

for char in text:
    if char.isalpha():
        char = char.lower()
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

print("Character frequencies:")
for char, count in sorted(freq.items()):
    print(f"{char}: {count}")


# Program 3: Collinearity Checker
# This program determines if a set of points lie on a straight line by checking
# if the slope between consecutive points is consistent using the cross-product method.

n = int(input("Enter number of points: "))
points = []

for i in range(n):
    x = float(input(f"Enter x{i+1}: "))
    y = float(input(f"Enter y{i+1}: "))
    points.append((x, y))

is_straight = True
for i in range(1, n - 1):
    x1, y1 = points[i - 1]
    x2, y2 = points[i]
    x3, y3 = points[i + 1]

    if (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1):
        is_straight = False
        break

if is_straight:
    print("The points form a straight line.")
else:
    print("The points do NOT form a straight line.")


# Program 4: Duplicate Remover and Sorter
# This program takes a list of numbers, removes duplicates using a set,
# and displays the unique numbers in sorted order.

nums = list(map(int, input("Enter numbers separated by space: ").split()))

unique_nums = set(nums)

sorted_nums = sorted(unique_nums)

print("Sorted list without duplicates:", sorted_nums)


# Program 5: Conditional List Filter
# This program filters a list based on position and prime number conditions:
# keeps even-positioned elements and odd-positioned elements only if they are prime numbers.

lst = list(map(int, input("Enter list elements separated by space: ").split()))

result = []

for i in range(len(lst)):
    num = lst[i]
    
    if i % 2 == 0:
        result.append(num)
    
    elif num >= 2:
        prime = True
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                prime = False
                break
        if prime:
            result.append(num)

print("Filtered list:", result)


# Program 6: List Analyzer with Manual Sorting
# This program sorts a list using bubble sort algorithm, finds min/max values,
# and removes duplicates manually by comparing consecutive elements.

n = int(input("Number of Numbers?"))
no = []
dup = []
for i in range(n):
    num = int(input(f"number {i+1}?"))
    no.append(num)
for i in range(n):
    for j in range(0,n-1-i):
        if no[j] > no[j+1]:
            t = no[j]
            no[j] = no[j+1]
            no[j+1] = t
print(f"ascending order \n{no}\n")
print(f"maximum value is \n{no[-1]}\n")
print(f"minimum value is \n{no[0]}\n")
dup.append(no[0])
for i in range(1,n):
    if no[i] != no[i-1]:
        dup.append(no[i])

print(f"without duplicates:{dup}")


# Program 7: Built-in List Analyzer
# This program performs the same operations as Program 6 but uses Python's built-in
# sort() function and set() for more efficient sorting and duplicate removal.

n = int(input("Number of Numbers?"))
no = []
for i in range(n):
    num = int(input(f"number {i+1}?"))
    no.append(num)
no.sort()
print(f"ascending order \n{no}\n")
print(f"maximum value is \n{no[-1]}\n")
print(f"minimum value is \n{no[0]}\n")
print(f"without duplicates:{set(no)}")


# Program 8: List Operations - Union and Difference
# This program takes two lists as input, combines them (union), and finds elements
# that exist in one list but not in the other (symmetric difference).

n1 = int(input("Number of Numbers in list 1?"))
no1 = []
for i in range(n1):
    num1 = int(input(f"number {i+1}?"))
    no1.append(num1)

n2 = int(input("Number of Numbers in list 2?"))
no2 = []
for i in range(n2):
    num2 = int(input(f"number {i+1}?"))
    no2.append(num2)
rem = []
k = []
com = no1
for y in range(n2):
    com.append(no2[y])
for i in range(n1):
    ctr = 0
    for j in range(n2):
        if no1[i] == no2[j]:
            ctr+=1
    if ctr == 0:
        rem.append(no1[i])


for i in range(n2):
    ctr = 0
    for j in range(n1):
        if no2[i] == no1[j]:
            ctr+=1
    if ctr == 0:
        rem.append(no2[i])

print(com)
print(rem)


# Program 9: Product Inventory Management System
# This program manages a product inventory with features to add products, update prices,
# search products within a price range, and display all products using a menu-driven interface.

products = {}

while True:
    print("\nMenu:")
    print("1. Add new product")
    print("2. Update product price")
    print("3. Find products within price range")
    print("4. Show all products")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter product name to add: ")
        if name in products:
            print(f"{name} already exists with price {products[name]}")
        else:
            try:
                price = float(input("Enter price: "))
                products[name] = price
                print(f"Product {name} added with price {price}")
            except ValueError:
                print("Invalid price. Please enter a number.")

    elif choice == '2':
        name = input("Enter product name to update: ")
        if name in products:
            try:
                price = float(input(f"Enter new price for {name}: "))
                products[name] = price
                print(f"Price of {name} updated to {price}")
            except ValueError:
                print("Invalid price. Please enter a number.")
        else:
            print(f"Product {name} not found.")

    elif choice == '3':
        try:
            low = float(input("Enter minimum price: "))
            high = float(input("Enter maximum price: "))
        except ValueError:
            print("Invalid input. Please enter numbers for price range.")
            continue

        found = []
        for name, price in products.items():
            if low <= price <= high:
                found.append(name)

        if found:
            print(f"Products priced between {low} and {high}:")
            for name in found:
                print(f"- {name}: {products[name]}")
        else:
            print(f"No products found in the price range {low} to {high}.")

    elif choice == '4':
        if products:
            print("All products and prices:")
            for name, price in products.items():
                print(f"{name}: {price}")
        else:
            print("No products available.")

    elif choice == '5':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter 1-5.")


# Program 10: Random Set Manipulator
# This program generates a set of 10 unique random numbers between 1-100,
# then removes the smallest and largest values from the set and displays the results.

import random

numbers = set()
while len(numbers) < 10:
    num = random.randint(1, 100)
    numbers.add(num)

print("Original set of 10 unique numbers:", numbers)

min_val = min(numbers)
max_val = max(numbers)

numbers.remove(min_val)
numbers.remove(max_val)

print("After removing smallest and largest:")
print("Removed smallest:", min_val)
print("Removed largest:", max_val)
print("Updated set:", numbers)


# Program 11: Word Frequency Counter
# This program counts the frequency of each word in a sentence by splitting the input
# into words and maintaining separate lists for unique words and their counts.

sentence = input("Enter a sentence: ")
words = sentence.split()

unique_words = []
word_counts = []

for word in words:
    if word in unique_words:
        index = unique_words.index(word)
        word_counts[index] += 1
    else:
        unique_words.append(word)
        word_counts.append(1)

print("\nWord Frequencies:")
for i in range(len(unique_words)):
    print(f"{unique_words[i]}: {word_counts[i]}")


# Program 12: Student Sports Participation Analyzer
# This program uses set operations to analyze student participation in cricket and football,
# finding students who play both sports, only one sport, or neither sport.

master = set(input("Enter all student roll numbers (space-separated): ").split())

cricket = set(input("Enter roll numbers of students who play cricket: ").split())

football = set(input("Enter roll numbers of students who play football: ").split())

both = cricket & football

only_one = (cricket ^ football)

neither = master - (cricket | football)

print("\nStudents who play both sports:", both)
print("Students who play only one sport:", only_one)
print("Students who play neither sport:", neither)


# Program 13: Stack and Queue Operations Simulator
# This program implements basic stack (LIFO) and queue (FIFO) data structures
# with push/pop and enqueue/dequeue operations through a menu-driven interface.

stack = []
queue = []

def push():
    val = input("Enter value to push to stack: ")
    stack.append(val)
    print(f"{val} pushed to stack.")

def pop():
    if not stack:
        print("Stack is empty.")
    else:
        val = stack.pop()
        print(f"{val} popped from stack.")

def enqueue():
    val = input("Enter value to enqueue in queue: ")
    queue.append(val)
    print(f"{val} enqueued in queue.")

def dequeue():
    if not queue:
        print("Queue is empty.")
    else:
        val = queue.pop(0)
        print(f"{val} dequeued from queue.")

while True:
    print("\nChoose an operation:")
    print("1. Push (Stack)")
    print("2. Pop (Stack)")
    print("3. Enqueue (Queue)")
    print("4. Dequeue (Queue)")
    print("5. Show Stack and Queue")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        push()
    elif choice == '2':
        pop()
    elif choice == '3':
        enqueue()
    elif choice == '4':
        dequeue()
    elif choice == '5':
        print("Current Stack:", stack)
        print("Current Queue:", queue)
    elif choice == '6':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")


# Program 14: Student Grade Management System
# This program manages student records with their marks, calculates average grades,
# identifies the top performer, and allows updating of student marks.

students = {
    "Chaitanya": [85, 90, 78],
    "DeepaK": [75, 80, 85],
    "Utsav": [92, 88, 95]
}

def display_averages(student_dict):
    print("Average marks of each student:")
    for name, marks in student_dict.items():
        avg = sum(marks) / len(marks)
        print(f"{name}: {avg:.2f}")

def find_topper(student_dict):
    topper = None
    highest_avg = -1
    for name, marks in student_dict.items():
        avg = sum(marks) / len(marks)
        if avg > highest_avg:
            highest_avg = avg
            topper = name
    print(f"Topper is {topper} with average marks {highest_avg:.2f}")

def update_marks(student_dict, name, new_marks):
    if name in student_dict:
        student_dict[name] = new_marks
        print(f"Marks updated for {name}.")
    else:
        print(f"Student {name} not found.")

display_averages(students)
find_topper(students)

update_marks(students, "Deepak", [85, 90, 80])

display_averages(students)
find_topper(students)


# Program 15: Unique Vowel Finder
# This program identifies and displays all unique vowels present in a given sentence,
# converting to lowercase and using set operations to eliminate duplicates.

vowels = {'a', 'e', 'i', 'o', 'u'}
sentence = input("Enter a sentence: ").lower()

unique_vowels = set()

for char in sentence:
    if char in vowels:
        unique_vowels.add(char)

print("Unique vowels used:", unique_vowels)