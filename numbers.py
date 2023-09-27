m = int(input())
m1 = m // 10000  # 1
m2 = m % 10000 // 1000  # 2
m3 = m % 1000 // 100  # 3
m4 = m % 100 // 10  # 4
m5 = m % 10  # 5
print(m1, m2, m3, m4, m5, sep='\n')



num1, num2, num3 = int(input()), int(input()), int(input())
counter = 0  # переменная счётчик
if num1 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num2 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num3 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
print(counter)
