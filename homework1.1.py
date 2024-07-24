a = input("Первое число ")
b = input("Второе число ")
c = input("Треть число ")
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
elif not a == b == c:
    print(0)
