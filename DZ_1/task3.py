"""
Напишите программу, которая выводит все чётные числа от нуля до введённого
пользователем числа включительно.
"""

num = int(input("Введите конечное числo -> "))

counter = ''
for i in range(1, num + 1):
    
    if i % 2 == 0:
        counter += str(i) + '; '
    else:
        continue

print("Чётные числа с 1 до", num, "=>", counter)