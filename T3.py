# function to find max of 3 nums
# def maxi(x,y,z):
#     if(x>=y and x>=z):
#         max=x
#     elif(y>=x and y>=z):
#         max=y
#     else:
#         max=z
#     return max
# x=int(input())
# y=int(input())
# z=int(input())
# print(maxi(x,y,z))

#function to multiply all numbers in list
# def mullist(L):
#     r=1
#     for x in L:
#         r=r*x
#     return r
# l1=[2,7,8]
# print(mullist(l1))

#program to reverse string
# t="ranj987" [::-1]
# print(t)

#function to calculate factorial of a number
# def fact(n):
#     return 1 if (n == 1 or n == 0) else n * fact(n - 1)
# a=int(input())
# print(fact(a))

#function to return distinct list
# def unique_list(lst_of_elements):
#     num = []
#     for a in lst_of_elements:
#         if a not in num:
#             num.append(a)
#
#     print("The list of unique elements is: ", num)
#
#
# lst_of_elements = []
# n = int(input("Enter number of elements : "))
# for i in range(0, n):
#     ele = int(input())
#     lst_of_elements.append(ele)
# print("The list entered by user : ", lst_of_elements)
#
# unique_list(lst_of_elements)

#prime or not
# def prim(num):
#
#     if num == 0 or num == 1:
#         print(num, "is not a prime number")
#     elif num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 print(num, "is not a prime number")
#                 print(i, "times", num // i, "is", num)
#                 break
#         else:
#             print(num, "is a prime number")
#     else:
#         print(num, "is not a prime number")
# a=int(input())
# print(prim(a))

#program to print even numbers in a list
# l=[3,6,3,54,8,9]
# for n in l:
#     if(n%2==0):
#        print(n,end=" ")
#lower and upper
# def st(a):
#     a=input()
#     lower = 0
#     upper = 0
#     for i in a:
#         if (i.islower()):
#             lower += 1
#         elif(i.isupper()):
#             upper += 1
#     print("The number of lowercase characters is:", lower)
#     print("The number of uppercase characters is:", upper)
# b=input()
# print(st(b))

#sum
# numbers = [1,2,3,4,5,1,4,5]
# Sum = sum(numbers)
# print(Sum)

#palindrome
def isPalindrome(s):
    return s == s[::-1]
s = "malayala"
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")





