# Write a Python program to create a class named Car. Define attributes like brand, model, and year. Create an object of the class and display the details of the car?
# class Car:
#     brand="Kia"
#     Model="Seltos"
#     Year="2022"
# s1=Car()
# print(Car)
# print(s1.brand)
# print(s1.Model)
# print(s1.Year)

#Create a class Student with attributes name, roll_number, and marks. Define a constructor to initialize these attributes and a method display_info() to print the student's details?
# class Student:
#     def __init__(self,name,rollno,marks):
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks
#     def disp(self):
#         print("Hello my name is "+self.name,self.rollno,self.marks)
# p1=Student("Ran",23,54)
# p1.disp()

#Create a class Rectangle with attributes length and breadth. Include methods to calculate the area and perimeter of the rectangle. Create multiple objects and display the area and perimeter for each?
# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def disp(self):
#         area=(self.length*self.breadth)
#         peri=2*(self.length+self.breadth)
#         print(area,peri)
# p1=Rectangle(3,4)
# p1.disp()
# p2=Rectangle(8,4)
# p2.disp()
#
#Write a class Circle with an attribute radius and methods get_area() and get_circumference(). These methods should return the area and circumference of the circle, respectively ?
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def get_area(self):
#         return 3.14*self.radius*self.radius
#     def get_circumference(self):
#         return 2*3.14*self.radius
# c=Circle(5)
# a=c.get_area()
# b=c.get_circumference()
# print(a)
# print(b)

#Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.
# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
# class Account:
# 	def __init__(self):
# 		self.balance=0
# 		print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
#
# 	def credit(self):
# 		amount=float(input("Enter amount to be Deposited: "))
# 		self.balance += amount
# 		print("\n Amount Deposited:",amount)
#
# 	def debit(self):
# 		amount = float(input("Enter amount to be Withdrawn: "))
# 		if self.balance>=amount:
# 			self.balance-=amount
# 			print("\n You Withdrew:", amount)
# 		else:
# 			print("\n Insufficient balance ")
#
# 	def display(self):
# 		print("\n Net Available Balance=",self.balance)
#
# # Driver code
#
# # creating an object of class
# s = Account()
#
# # Calling functions with that class object
# s.credit()
# s.debit()
# s.display()

#Create a class Employee with an attribute employee_count (class variable) and a class method increment_employee_count() to increase the count whenever a new employee object is created. Show the updated employee count after creating new objects
# class Employee:
#     count = 0  # This is a class variable
#
#     def __init__(self, name):
#         self.name = name  # This is an instance variable
#         Employee.count += 1  # Accessing the class variable using the name of the class
# person1 = Employee("Ayan")
# person2 = Employee("Bobby")
# person3=Employee("Valz")
# print(Employee.count)

#Create a class Book with attributes title, author, and price. Write a constructor that allows the user to either initialize all three attributes or just the title and author (in which case the price should be set to a default value). Display the details of the book using an instance method
# class Book:
#     def __init__(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price
#     def disp(self):
#         print("Author of this book "+self.title+" is "+self.author+" priced ",self.price )
# a=Book("Hamlet","Shakespeare",450)
# a.disp()

#Write a class TemperatureConverter with an instance method celsius_to_fahrenheit(celsius) that takes a temperature in Celsius and returns its Fahrenheit equivalent. Create an object of the class and use the method to convert various temperatures.
# class TemperatureConverter:
#     def __init__(self,celsius):
#         self.celsius=celsius
#     def celsius_to_fahrenheit(self):
#         return (self.celsius * 9/5) + 32
# c=TemperatureConverter(38)
# a=c.celsius_to_fahrenheit()
# print(a)

#Create a class Time with attributes hours and minutes. Add a method add_time() that takes another Time object, adds its values to the current object, and returns a new Time object with the resulting sum.
# class Time:
#
#     def __init__(self, hrs=0, mins=0):
#         """ Create a MyTime object initialized to hrs, mins, secs """
#         self.hours = hrs
#         self.minutes = mins
#
#
#     def __str__(self):
#         timeString = ""
#         if self.hours < 10:
#             timeString += "0"
#         timeString += str(self.hours) + ":"
#         if self.minutes < 10:
#             timeString += "0"
#         timeString += str(self.minutes)
#
#         return timeString
#
# def add_time(t1, t2):
#     h = t1.hours + t2.hours
#     m = t1.minutes + t2.minutes
#     sumTime = Time(h, m)
#     return sumTime
#
# currentTime = Time(5, 15)
# breadTime = Time(3, 15)
# doneTime = add_time(currentTime, breadTime)
# print(doneTime)

#Create a class EmployeeSalary with class variables basic_salary and bonus_percentage. Write a class method set_bonus_percentage() to change the bonus percentage for all employees. Create an instance method calculate_total_salary() to calculate and return the total salary (basic + bonus) for a specific employee.
# class EmployeeSalary:
#     # Class variables
#     basic_salary = 0
#     bonus_percentage = 0.0
#
#     def __init__(self, basic_salary):
#         self.basic_salary = basic_salary
#
#     @classmethod
#     def set_bonus_percentage(cls, new_bonus_percentage):
#         cls.bonus_percentage = new_bonus_percentage
#
#     def calculate_total_salary(self):
#         # Calculate the total salary based on the class variables
#         bonus = (self.basic_salary * self.bonus_percentage) / 100
#         total_salary = self.basic_salary + bonus
#         return total_salary
#
# # Example usage
# if __name__ == "__main__":
#     # Set bonus percentage for all employees
#     EmployeeSalary.set_bonus_percentage(10)  # Set bonus to 10%
#
#     # Create an employee with a basic salary of 5000
#     employee1 = EmployeeSalary(5000)
#     total_salary1 = employee1.calculate_total_salary()
#     print(f"Total Salary for Employee 1: {total_salary1}")
#
#
#     # Change the bonus percentage
#     EmployeeSalary.set_bonus_percentage(20)  # Set bonus to 15%
#
#     # Calculate total salary again for employee 1 and employee 2
#     total_salary1 = employee1.calculate_total_salary()
#     print(f"Total Salary for Employee 1 after bonus change: {total_salary1}")
#



