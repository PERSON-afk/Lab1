# 1. Function to greet a user with a simple message
def greet_user(name):
    print(f"Hello, {name}! Welcome!")
greet_user("Kushal")


# 2. Function to greet a user, takes input from user
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python!")
x = input("Name?")
greet_user(x)


# 3. Function to calculate power with default exponent
def power(base, exponent=2):
    return base ** exponent
print(power(3, 4))
print(power(5))


# 4. Function to display book information using keyword arguments
def book_info(title, author, year):
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Year: {year}")
book_info(title="1984", author="Kushal Giri", year=1949)
book_info(author="Bid Van", year=1997, title="Namaste Nepal")
book_info(year=2003, title="The Vinci Code", author="Dan Brown")


# 5. Function to sum any number of arguments using *args
def sum_numbers(*args):
    return sum(args)
print(sum_numbers(10, 20))
print(sum_numbers(1, 2, 3))
print(sum_numbers(4, 5, 6, 7, 8))


# 6. Function to display student profile using **kwargs
def student_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
student_profile(name="Kushal", age=18, grade="12th")


# 7. Lambda function to calculate square of a number
square = lambda x: x ** 2
print(square(5))
print(square(12))


# 8. Using map and lambda to double each number in a list
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)


# 9. Using filter and lambda to find numbers divisible by 10
numbers = [10, 15, 20, 25, 30]
divisible_by_10 = list(filter(lambda x: x % 10 == 0, numbers))
print(divisible_by_10)


# 10. Convert Celsius to Fahrenheit and filter values below 100°F
celsius = [36.5, 37.0, 39.2, 35.6, 38.7]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
below_100 = list(filter(lambda f: f <= 100, fahrenheit))
print("Fahrenheit:", fahrenheit)
print("Below 100°F:", below_100)