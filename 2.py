#1

n = int(input("Enter a number: "))

if n < 2:

    print("Not prime")

else:

    is_prime = True

    for i in range(2, n):

        if n % i == 0:

            is_prime = False

            break

    if is_prime:

        print("Prime")

    else:

        print("Not prime")





#2 

for i in range(1, 101):

    if i % 2 == 0:

        print(i)



#3

n = int(input("Enter a number: "))

fact = 1

i = 1

while i <= n:

    fact = fact * i

    i = i + 1

print(fact)





#4

n = int(input("Enter a number: "))

for i in range(1, 11):

    print(n, "x", i, "=", n * i)



#5

n = int(input("How many numbers? "))

numbers = []

for i in range(n):

    num = int(input("Enter number: "))

    numbers.append(num)

largest = numbers[0]

smallest = numbers[0]

for i in numbers:

    if i > largest:

        largest = i

    if i < smallest:

        smallest = i

print("Largest:", largest)

print("Smallest:", smallest)





#6

positive = 0

negative = 0

zero = 0

for i in range(10):

    num = int(input("Enter number: "))

    if num > 0:

        positive += 1

    elif num < 0:

        negative += 1

    else:

        zero += 1

print("Positive:", positive)

print("Negative:", negative)

print("Zero:", zero)





#7

n = int(input("Enter number of terms: "))

a = 0

b = 1

for i in range(n):

    print(a)

    c = a + b

    a = b

    b = c





#8

n = input("Enter a number: ")

rev = ""

for i in n:

    rev = i + rev

if n == rev:

    print("Palindrome")

else:

    print("Not Palindrome")



#9

for num in range(100, 1000):

    a = num // 100

    b = (num // 10) % 10

    c = num % 10

    if a**3 + b**3 + c**3 == num:

        print(num)



#10

a = int(input("Enter first number: "))

b = int(input("Enter second number: "))

print("1. Addition")

print("2. Subtraction")

print("3. Multiplication")

print("4. Division")

choice = int(input("Enter your choice: "))



if choice == 1:

    print("Result:", a + b)

elif choice == 2:

    print("Result:", a - b)

elif choice == 3:

    print("Result:", a * b)

elif choice == 4:

    if b != 0:

        print("Result:", a / b)

    else:

        print("Cannot divide by zero")

else:

    print("Invalid choice")
