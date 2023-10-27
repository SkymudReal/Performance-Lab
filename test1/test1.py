n, m = map(int, input("Введите переменные n и m через пробел: ").split())

i = 1
print("Путь: ")
while True:
    print(i, end='')
    i = 1 + (i + m - 2) % n
    if i == 1:
        break

