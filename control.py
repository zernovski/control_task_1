# #1
# lst = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31,
# 55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]

# dic = {index: i for index, i in enumerate(lst)}
# print(dic)


# #2
# import random
# a = random.randint(1, 20)


# i = 0

# while i < 5:

#     b = int(input("Введите число от 1 до 20:"))

#     if b < a:
#         print("Слишком мало!")
#     elif b > a:
#         print("Слишком много!")
#     elif b == a:
#         print("Класс вы угадали!")
#         break
#     i += 1

# if i == 5:
#     print("Все вы не угадали. Конец игры.")


# #3
# some_string = "Adverts"
# print(some_string[2:5])

#4
n = "Aidana"
m = "Adilet"

s = n[0] + m[0] + n[1] + m[1] + n[2] + m[2] + n[3] + m[3] + n[4] + m[4] + n[5] + m[5]
print(s)