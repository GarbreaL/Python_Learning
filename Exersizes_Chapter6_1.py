"""
字符串验证功能
isX系列函数
"""

while True:
	print('Enter your age')
	age=input()
	if age.isnumeric():
		break;
	else:
		print('Please enter a number for your age')

while True:
	print('Enter your password')
	pwd=input()
	if pwd.isalnum():
		break;
	else:
		print('Password can only have letters and numbers')

print('Your age is:'+str(age))
print('Your password is:'+str(pwd))
