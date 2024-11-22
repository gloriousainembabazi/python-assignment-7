
# Loops (question 1)

# Basic:
# 
#  Write a Python program that prints all even numbers between 1 and 20 using a for loop.

for x in range(1,21):
  if x  % 2 == 0:      # completed
     print(x)

# Intermediate: 

# Use a while loop to ask the user to input a number until they provide a number greater than 10.
num = 0
num > 10
while num<=10:
      num =int(input('Enter the number greater than 10:')) # completed
      if num <= 10:
       print("please enter the number greater than 10")




# Advanced: 

# Write a program that prints the multiplication table (from 1 to 10)
#  for numbers from 1 to 5 using nested for loops.

for i in range(1,6):
  for j in range(1,11):
      print(f" {i}x{j} = {i*j}\t",end="")


    


# Challenge: ()
# Given a list of integers, [4, 7, 2, 9, 12, 15],
#  write a program using a for loop to find the sum of all odd numbers and print the result.

numbers = [4,7,2,9,15]
odd_sum = 0
for num in numbers:
     if num % 2 != 0:
       odd_sum += num 
 
print(f"The sum of all odd numbers is : ",odd_sum)


# Lists (question 2)

# Basic:
#  Create a list of 5 fruits and print each fruit on a new line using a for loop.

fruits =['apple','orange','grapes','maize','lemon']
for fruit in fruits:          #   completed
    print(fruit)


# Intermediate:

#  Write a function that takes a list of numbers
#  and returns a new list with each number squared.
#  Example: [1, 2, 3] should become [1, 4, 9].

numbers = [2,4,6,]
squared = []
for num in numbers:
    squared.append(num**2) # completed
    print(squared)



# Advanced:
#  Write a Python program that takes two lists,
#  list1 = [1, 2, 3] and list2 = [4, 5, 6],
#  and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_lists = list1 + list2
print(combined_lists)
 

# Challenge: Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], 
# write a program to find and print the two largest
#  numbers in the list without using the max() function.

numbers = [3, 1, 4, 1, 5, 9, 2]
largest = float('-inf')  # S
second_largest = float('-inf')

# Iterate through the list
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("The largest number is:", largest)
print("The second largest number is:", second_largest)

# Dictionaries
#  1 Basic:
#  Create a dictionary with three key-value pairs
#  representing a student's information: name, age, and grade.
#  Print each key-value pair on a new line.


 
student_info = {"Name":'Glorious',"Age":22,"Grade":"4th" }
for key,value in student_info.items():  #  completed
   print(key,value)




# Intermediate: Write a function that takes a dictionary 
# of people's names and their ages, 
# {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a 
# list of names of people who are 21 or older.

def select_adults(people):
    return [name for name, age in people.items() if age >= 21]  # completed
people = {'Alice': 24, 'Bob': 19, 'Charlie': 30}
print(select_adults(people))

# Advanced: Given a dictionary representing items in a store with their prices,
# {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a 
# program that takes a list of items bought,
#  ['apple', 'orange', 'banana', 'banana'], and calculates the total cost.
def calculate_total_cost(prices, items_bought):
     total_cost = sum(prices[item] for item in items_bought)
     print( total_cost)
 
store = {'apple': 0.5, 
'banana': 0.3,
 'orange': 0.7}
items_bought = ['apple', 'orange', 'banana', 'banana']
print(calculate_total_cost(store, items_bought))

# Challenge: Write a program that counts the
#  occurrences of each word in a given sentence. 
# Example: for the sentence "hello world hello," 
# the output should be {'hello': 2, 'world': 1}.

def word_count(sentence):
     words = sentence.split()
     return {word: words.count(word) for word in set(words)}

sentence = "hello world hello"
print(word_count(sentence))

# Object-Oriented Programming (OOP)
# Basic: Create a class called Car with attributes brand and color. 
# Instantiate an object of the Car class and print its attributes.

class Car:
     def __init__(self, brand, color):
         self.brand = brand
         self.color = color # completed

car = Car("Toyota", "Red")
print(car.brand)
print(car.color)

# Intermediate: Add a method called start_engine to the Car class that prints 
# # a message saying the engine of the car has started. Create an instance of Car and call the method.

class Car:
     def __init__(self, brand, color):
         self.brand = brand
         self.color = color

     def start_engine(self):
         print(f"The engine of the {self.brand} has started!") # completed

car = Car("Toyota", "Red")
car.start_engine()

# # Advanced: Create a class called BankAccount with attributes account_number and balance. Add methods to:
# class BankAccount:
# # Deposit an amount.
# # Withdraw an amount (only if sufficient balance exists).
# # Print the account balance.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def print_balance(self):
        print(f"Account balance: {self.balance}")

account = BankAccount(12345678, 100)
account.deposit(50)
account.withdraw(30)
account.print_balance()

# # Challenge: Implement a class called Library that manages a collection of books. 
# # Each book has a title, author, and available status. The Library class should have methods to:
# # Add a book to the library.
# # Remove a book from the library.
# # Check if a book is available by title.
# # Borrow a book (mark it as unavailable if it’s available).
# # Return a book (mark it as available again if it was borrowed).
class Library:
     def __init__(self):
         self.books = {}

     def add_book(self, title, author):
         self.books[title] = {"author": author, "available": True}
         print(f"Added book: {title} by {author}")

     def remove_book(self, title):
         if title in self.books:
             del self.books[title]
             print(f"Removed book: {title}")
         else:
             print(f"Book not found: {title}")

     def is_available(self, title):
         if title in self.books:
             return self.books[title]["available"]

         else:
             return False

def borrow_book(self, title):
         if self.is_available(title):
             self.books[title]["available"] = False
             print(f"You borrowed: {title}")
         else:
             print(f"Book not available: {title}")

def return_book(self, title):
         if title in self.books and not self.books[title]["available"]:
             self.books[title]["available"] = True
             print(f"Returned book: {title}")
         else:
             print(f"Book not found or not borrowed: {title}")


library = Library()
library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")
print(library.is_available("1984"))  # True
library.borrow_book("1984")
print(library.is_available("1984"))  # False
library.return_book("1984")
print(library.is_available("1984"))  # True
