#Assignment 1: Static Methods
# class MathOperations:
#     def add_numbers(x,y):
#         return x+y
#     def multiply_numbers(x,y):
#         return x*y
# sum=MathOperations.add_numbers(2,7)
# product=MathOperations.multiply_numbers(3,6)
# print(sum)
# print(product)

#Class Methods
# class Person:
#     # Class variable to count instances
#     count = 0
#
#     def __init__(self):
#         # Increment count whenever a new instance is created
#         Person.count += 1
#
#     @classmethod
#     def get_count(cls):
#         """Returns the current count of Person instances."""
#         return cls.count
#
# # Example usage:
# if __name__ == "__main__":
#     person1 = Person()
#     person2 = Person()
#
#     print(f"Number of Person instances created: {Person.get_count()}")  # Output: 3

#Using Both Static and Class Methods
# class TemperatureConverter:
#     def celsius_to_fahrenheit(x):
#         return x*(9/5)+32
#     def info():
#         return "Message Celsius to Farenheit is converted"
# a=30
# b=TemperatureConverter.celsius_to_fahrenheit(a)
# print(b)
# print(TemperatureConverter.info())

#Single Inheritance
# class Animal:
#     def sound(self):
#         print("Animal sound")
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
# a=Animal()
# d=Dog()
# a.sound()
# d.sound()

#Multiple Inheritance
# class Bird:
#     def fly(self):
#         print("Flying")
# class Fish:
#     def swim(self):
#         print("Swimming")
# class Duck(Bird,Fish):
#     def both(self):
#         print("Both Flying & Swimming")
# x=Duck()
# x.fly()
# x.swim()
# x.both()

#Abstract Class
# from abc import ABC, abstractmethod
# import math
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         """Calculate the area of the shape."""
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         """Calculate the area of the circle."""
#         return math.pi * (self.radius ** 2)
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         """Calculate the area of the rectangle."""
#         return self.width * self.height
#
# # Example usage:
# if __name__ == "__main__":
#     circle = Circle(radius=5)
#     rectangle = Rectangle(width=4, height=6)
#
#     print(f"Area of the circle: {circle.area():.2f}")      # Output: Area of the circle: 78.54
#     print(f"Area of the rectangle: {rectangle.area():.2f}")  # Output: Area of the rectangle: 24.00

#Encapsulation
# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self._balance = initial_balance  # Private attribute
#
#     def deposit(self, amount):
#         """Deposit money into the account."""
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited: ${amount:.2f}. New balance: ${self._balance:.2f}")
#         else:
#             print("Deposit amount must be positive.")
#
#     def withdraw(self, amount):
#         """Withdraw money from the account."""
#         if amount > 0:
#             if amount <= self._balance:
#                 self._balance -= amount
#                 print(f"Withdrew: ${amount:.2f}. New balance: ${self._balance:.2f}")
#             else:
#                 print("Insufficient funds.")
#         else:
#             print("Withdrawal amount must be positive.")
#
#     def get_balance(self):
#         """Return the current balance."""
#         return self._balance
#
# # Example usage:
# if __name__ == "__main__":
#     account = BankAccount(100)  # Initial balance of $100
#
#     account.deposit(50)          # Depositing $50
#     account.withdraw(30)         # Withdrawing $30
#     account.withdraw(150)        # Attempting to withdraw $150
#     print(f"Current balance: ${account.get_balance():.2f}")  # Checking balance

#Polymorphism with Method Overriding
# class Cat:
#     def speak(self):
#         print("Meow")
# class Dog:
#     def speak(self):
#         print("Woof")
# a=Cat()
# b=Dog()
# a.speak()
# b.speak()

#Polymorphism with Method Overloading
# class Calculator:
#     def add(self,a,b,c=0):
#         return a+b+c
# c=Calculator()
# s1=c.add(3,5)
# s2=c.add(7,5,4)
# print(s1)
# print(s2)

#Multilevel Inheritance
# class LivingBeing:
#     def breathe(self):
#         print("Breathing")
# class Mammal(LivingBeing):
#     def walk(self):
#         print("Walking")
# class Human(Mammal):
#     def think(self):
#         print("Thinking")
# c=Human()
# c.breathe()
# c.walk()
# c.think()

