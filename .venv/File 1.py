print("Hello World")
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#creating a list of n numbers
n = 100
x = list(range(2, n+1))
for i in x: #says that for each number 'i' in list 'x'
    j = 2 #specifies j as 2 as a number multiplied by 2 is even, so it eliminates all non-prime numbers
    while i * j <= x[-1]: #x[-1] refers to the last number in list 'x', so it says that for all even numbers less...
        if i * j in x: #...than or equal to the last number in the list, if such a number is in the list...
            x.remove(i*j) #...then it must be removed
        j += 1 #once all multiples of two are eliminated, all multiples of 3 go next, then all multiples of 4, and so on
print("the list of prime numbers is:", x)

#type() tells you the type of an object

#Boolean operators example
x = True
y = False

# Using 'and' operator
print(x and y)  # Output: False

# Using 'or' operator
print(x or y)   # Output: True

# Using 'not' operator
print(not x)    # Output: False
print(not y)    # Output: True

#Comparison operators yield values such as True or False
print(5 == 5)
print(5 != 3)
print(7 > 3)
print(6 >= 6)
print(2 < 8)
print(4 <= 5)
#'is' is TRUE for identical objects
#'is not' is TRUE for different objects

#Variable names cannot start with a number
#Keywords such as 'and', 'or', 'True', 'not', etc. cannot be used as variable names

#Example of 'if' statement
number = 10
if number % 2 == 0:
    print(number, "is an even number")
    print("Nothing would be printed if it were odd")
#elif (else if) checks the elif conditions in the case that the 'if' condition is false
#else runs all the cases that are not covered by elif or if
    #Example
    number_2 = 7
    if number > 10:
        print("The number is greater than 10")
    elif number > 5: #There is no limit to the amount of 'elif' branches you can add
        print("The number is greater than 5 but not more than 10")
    else:
        print("The number is 5 or less")

#Getting out pieces of a string
word_1 = "Hello"
print(word_1[2]) #REMEMBER: the first character of a word is 0, the second 1, and so on
#[-1] yields the last character of the string
#String indices must always be integers

#Strings can be joined
hi = "Hello"
bye = "Bye"
print(hi+bye)
print(hi + " " + bye) #adds a space in between
toodles = "Hello"*4 #makes it so that hello is said 4 times
print(toodles)
for letter in hi: #strings are iterable
    print(letter)
print(hi[1:3]) #yields first and third characters of a string
print(hi[:4]) #yields up to, but not including, the 4th character of a string
print(hi[::3]) #yields every 3rd character in the string
print(hi[::-1]) #yields string but in reverse, as '1' would yield it in normal order

#dir() lists the methods available for an object
print(dir(hi))
help(hi.capitalize) #help(name_of_variable.name_of_method) tells you what the method does

#Applying a method
s = "hello world my name is John"
print(s.capitalize())
print(s.count(""))
print(s.replace(" ", "!!"))
print(s.split())

sk = "http://google.com and then there could be http://yahoo.com or even a website like http://bbc.co.uk"
print(sk.count(""))
print(sk[-1])

#Altered copies of strings can be created
s2 = "rr" + s[1:]
print(s2)

#Conversion types with '%'
    #%d- integer, %g - float, %x - hexadecimal, %s - string

#F-string example
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")
#Another example
def to_lowercase(input):
    return input.lower()
name2 = "Jonathan McKinsey"
print(f"{to_lowercase(name2)} thinks he is funny")

#File exercise
with open("log.txt", "w") as file:
    file.write("Hello\n")
    file.write("My\n")
    file.write("Name\n")
    file.write("Is\n")
    file.write("Matias\n")
    file.write("And\n")
    file.write("I\n")
    file.write("Am\n")
    file.write("Working\n")
print("File 'log.txt' has been created")

practice_file = open("log.txt", "r")
print(practice_file)
all = practice_file.read()
print(all)

#Sessions 3 and 4 exercises
print(type(2))
print(type(2.3))
print(type(False))
print(type(None))
print(type(4*2))
print(type(4/2))
print(type(3.0*1.0))
print(type(~3))
print(type(3 | 2))
print(type(print("xx")))

#Sessions 5 and 6 exercises
for x in range (11):
    for y in range(11):
        print(f"({x}, {y})")

for x in range (1, 10):
    if x%2 != 0:
        continue
    print(x)
print("We have 4 even numbers")

#Printing multiplication table from 1 to 10 without repeating expressions
for a in range(1, 11):
    for b in range(a, 11):  # Start from 'a' to avoid duplicates
        print(f"{a} x {b} = {a * b}")
    print()  # Adds a newline for better readability

#You can only do additions. Write a program that reads two positive, integer numbers a and b. It should compute a**b
def add_multiply(x, y):
    """Simulate multiplication using only additions"""
    result = 0
    for _ in range(y):
        result += x  # Add x, y times
    return result

def power(a, b):
    """Compute a ** b using only additions"""
    if b == 0:
        return 1  # Any number to the power of 0 is 1
    result = a
    for _ in range(b - 1):  # Multiply a by itself (b-1) times
        result = add_multiply(result, a)  # Use addition-based multiplication
    return result

# Read inputs
a = int(input("Enter base (a): "))
b = int(input("Enter exponent (b): "))

# Compute and print result
print(f"{a} ** {b} = {power(a, b)}")

#Read an int number. Check if the number is a palindrome. (A palindrome number read backwards has the same value
def is_palindrome(number):
    """Check if a number is a palindrome"""
    original = str(number)  # Convert number to string
    reversed_num = original[::-1]  # Reverse the string
    return original == reversed_num  # Check if original and reversed are the same

# Read an integer input from the user
num = int(input("Enter an integer: "))

# Check and print the result
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

#Getting input
prompt = "What is the speed of the car?"
speed = input(prompt)
print("The speed of the car is" + speed)

#Try/Except test
try:
    calculation = 10/2
except ZeroDivisionError:
    print("Numbers cannot be divided by Zero")
else:
    print(calculation)
finally:
    print("Thank you for using our program")

def calculate_net_salary():
        # Read input safely
        gross = float(input("Enter the gross salary: "))
        children = int(input("Enter the number of children: "))

        # Determine the income tax rate
        if gross < 1000:
            tax_rate = 0.10  # 10%
        elif gross < 2000:
            tax_rate = 0.12  # 12%
        elif gross < 4000:
            tax_rate = 0.14  # 14%
        else:
            tax_rate = 0.18  # 18%

        # Determine tax deduction per child
        if gross < 2000:
            child_discount = 0.01 * children  # 1% per child
        else:
            child_discount = 0.005 * children  # 0.5% per child

        # ✅ Ensure the effective tax rate does not go negative
        effective_tax_rate = max(0, tax_rate - child_discount)

        # ✅ Calculate correct net salary
        net_salary = gross * (1 - effective_tax_rate)

        # Print the correct net salary
        print(f"Net Salary: {net_salary:.2f}")

# Run the function
calculate_net_salary()
