def collatz(number):
	if number % 2 == 0:
		print(str(number/2))
		return number/2
	else:
		print(str(3*number+1))
		return 3*number+1


print("input a integer")
try:
	i = int(input())
	result = collatz(i)
	while result != 1:
		result = collatz(result)					# 循环调用
except ValueError:  							# 错误捕捉
	print("please input a integer")
