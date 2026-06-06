
# languages = ['Spanish', 'English', 'Russian', 'Chinese']
# for index, language in enumerate(languages):
#     print(f'Index {index} and language {language}')

# digit = int(input("Enter a digit: "))
# res = 1
# for i in range(1, digit+1): #for loop using range
#     res *= i
# print(f"factorial of {digit} is {res}")

## Print all the factors of a number
# digit = int(input("Enter a digit: "))
# factors = []
# for i in range(1, digit+1):
#     if(digit % i == 0):
#         factors.append(i)
# print(f"factors of {digit} are: {factors}")

# #Accept a number and check if it a perfect number or not.
# digit = int(input("Enter a digit: "))
# factors = []
# for i in range(1, digit):
#     if(digit % i == 0):
#         factors.append(i)

# sum = 0
# for i in range(len(factors)):
#     sum += factors[i]

# if(sum == digit):
#     print(f"{digit} is a perfect number")
# else:
#     print(f"{digit} is not a perfect number")

# # Check string is Pallindrome or not
# str = input("Enter the string:")
# is_palindrome = True
# for i in range(len(str)):
#     for j in range(len(str)-1, -1, -1):
#         if(i+j == len(str)-1):
#             if(str[i] != str[j]):
#                 print(f"{str} is not a palindrom")
#                 is_palindrome = False
#                 break
#     break  
# if(is_palindrome):    print(f"{str} is a palindrom")


# text = input("Enter the string: ")
# if text == text[::-1]:
#     print(f"{text} is a palindrome")
# else:
#     print(f"{text} is not a palindrome")

# #Create a random number guessing game with python.
# import random
# ranint = random.randint(1, 10)
# game_flow = 1
# while (game_flow):
#     guess = int(input("Enter a num:"))
#     if(ranint == guess):
#         print(f"Congratulations you guess the number {ranint}")
#         game_flow = 0
#     elif (ranint < guess):
#         print("number is lower")
#     else:
#         print("number is greater")

