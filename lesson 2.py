# a = int(input())
# b = int(input())
# print((a * b) ** (1/2))

# number = (input())
# if len(number) == 1:
#     print("Число однозначное")
#
# if len(number) == 2:
#     print("Число двухзначное")
# print(number[1] + number[0])
#
# if len(number) == 3:
#     print("Трёхзначное")
# print(number[2] + number[1] + number[0])


# a = input()
# q = a.count('1')
# q1 = a.count('2')
# q2 = a.count('3')
# q3 = a.count('4')
# q4 = a.count('5')
# q5 = a.count('6')
# q6 = a.count('7')
# q7 = a.count('8')
# q8 = a.count('9')
# a1 = (q + q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8)
# print(a1)

# a = input()
# if 'хороший' in a:
#     a1 = a.replace('хороший', 'очень хороший')
#     print(a1)


# login = int(input())
# email = input()
# phone_number = input()
# password = int(input())

# if login >= 6:
#     print("Your login right!")
# else:
#     print("No! Your login not right")
# if password >= 6:
#     print("Your password right!")
# else:
#     print("No! Your password not right")
# if '@' in email:
#     print("Your email right!")
# else:
#     print("No! Your email not right")
# if phone_number[0] == '+' and phone_number[1] == '7' or phone_number[0] == 8:
#     print("Your phone number right")
# else:
#     print("No! your phone number right")
#
# login = int(input())
# email = input()
# phone_number = input()
# password = int(input())
#
# TrueX = [login and password >= 6, '@' in email]
# TrueX = [phone_number[0] == '+' and phone_number[1] == '7' or phone_number[0] == 8]]
# if all(TrueX):
#     print("Right")
# else:
#     print("Not right")

import random

print('1 - камень, 2 - ножницы, 3 - бумага')
a = int(input("Ваш выбор"))
b = random.randint(1, 3)
if a == 1 and b == 1:
    print("Ничья!")
if a == 1 and b == 2:
    print("Вы победили!")
if a == 1 and b == 3:
    print("Повезёт в другой раз!?")
if a == 2 and b == 1:
    print("Вы проиграли!")
if a == 2 and b == 2:
    print("Ничья!")
if a == 2 and b == 3:
    print("Вы выиграли! Мои поздравления")
if a == 3 and b == 1:
    print("Вы выиграли")
if a == 3 and b == 2:
    print("Повезёт в другой раз!?")
if a == 3 and b == 3:
    print("Ничья!")
