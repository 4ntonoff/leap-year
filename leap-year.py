year = int(input("Введите год "))
if ((year % 4 == 0) & (year % 400 == 0)):
    print("Этот год високосный")
elif year % 100 == 0:
    print("Год",year,"Невисокосный")
else:
    print("Год",year,"Невисокосный")