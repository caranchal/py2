a = int(input("число от:"))
b = int(input("до:"))
que = int(input("введите число от 1 до 4 где\n 1 - вывести все цифры которые делятся на заданое число\n 2 - перемножить все заданые нечётные числа\n 3 - посчитать сколько раз введёное число встречается\n 4 - перевести заданные числа в римскую систему"))
List=list(range(a,b))
c=0
print("0")
for i in List:
    c=c+i
    print(c)
if que > 4 and que < 1:#проверка
	print("введите правильное число")
elif que == 1:
	number1 = int(input("делитель"))#деление
	for i in range(a, b):
		print((b - a)% i)
elif que == 2:
	for i in range(a,b):
		number2 = (i%2)
elif que == 3:
		number = int(input("введите число"))
		i.count(c)