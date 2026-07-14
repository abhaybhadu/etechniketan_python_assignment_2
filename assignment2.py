

# Question 33

s1 = "practice is important to perfectly learn python"

indexes = []

for i in range(len(s1)):
    if s1[i] == "p":
        indexes.append(i)

print(indexes)




# Question 34

strings = ["aba", "abc", "121", "madam", "hi", "1991", "python"]

count = 0

for word in strings:
    if len(word) > 2 and word == word[::-1]:
        count += 1

print("Palindrome count =", count)



# Question 35

s1 = "How much wood would a woodchuck chuck if a Woodcutter could chuck wood to build a wooden house to woo his wife"

words = s1.split()

result = []

for word in words:
    if len(word) >= 4 and word.lower().startswith("w"):
        if word not in result:
            result.append(word)


# Question 36

s = input("Enter a string: ")

count = {}

for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print(count)




# Question 37

products = {
    "soap": 50,
    "oil": 200,
    "laptop": 60000,
    "phone": 25000,
    "mouse": 500
}

costliest = max(products, key=products.get)

print("Costliest product is", costliest)

print(result)

# Question 38

d = {
    'name': 'Kelly',
    'age': 25,
    'salary': 8000,
    'city': 'New york'
}

keys_to_remove = ['name', 'salary']

for key in keys_to_remove:
    if key in d:
        del d[key]



# Question 39

num = int(input("Enter a number: "))

while num >= 0:
    if num == 0:
        print("Blast!")
    else:
        print(num)
    num -= 1

# Question 40

print("Welcome to the Grade Checker Program!")

while True:

    marks = float(input("Enter your marks (0-100): "))

    if marks >= 90:
        print("Your grade is A+")
    elif marks >= 80:
        print("Your grade is A")
    elif marks >= 70:
        print("Your grade is B")
    elif marks >= 60:
        print("Your grade is C")
    elif marks >= 50:
        print("Your grade is D")
    else:
        print("Your grade is Fail")

    choice = input("Do you want to continue? (yes/no): ").lower()

    if choice == "no":
        print("Thank You!")
        break



# Question 41

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

# Question 42

password = "python123"

attempt = 1

while attempt <= 3:

    user = input("Enter Password: ")

    if user == password:
        print("Access Granted")
        break
    else:
        print("Wrong Password")
        attempt += 1

if attempt > 3:
    print("Access Denied")

# Question 43

import random

print("Welcome to the Simple Coin Toss Game!")

while True:

    guess = input("Guess (heads/tails): ").lower()

    while guess not in ["heads", "tails"]:
        print("Invalid input!")
        guess = input("Guess (heads/tails): ").lower()

    toss = random.choice(["heads", "tails"])

    print("Coin shows:", toss)

    if guess == toss:
        print("You guessed it right!")
    else:
        print("Wrong guess!")

    again = input("Do you want to play again? (yes/no): ").lower()

    if again == "no":
        print("Thanks for playing!")
        break



print(d)