import time
#用戶身分驗證
username = input('Please enter username: ')
password = input('Please enter password: ')
#如果希望輸入密碼時,終端沒有回應,可以使用getpass模塊的getpass函數
#import getpass
#password = getpass.getpass('Please enter password: ')
if username == 'admin' and password == '123456':
	print('Login Success!')
else:
	print('Login Fail!')

#分段函數求值
x = float(input('x = '))
if x > 1:
	y = 3 * x - 5
elif x >= -1:
	y = x + 2
else:
	y = 5 * x + 3

print('f(%.2f) = %.2f' % (x, y))

#Flat is better than nested.


#英制單位英寸和公制單位公分的互換
value = float(input('Please enter length: '))
unit = input('Please enter unit: ')
if unit == 'in':
	print('%f inch = %f cm' % (value, value * 2.54))
elif unit == 'cm':
	print('%f cm = %f inch' % (value, value / 2.54))
else:
	print('invaild input')

#擲骰子決定做什麼事
from random import randint
face = randint(1, 6)
if face == 1:
	result = 'sing'
elif face == 2:
	result = 'dance'
elif face == 3:
	result = 'woff'
elif face == 4:
	result = 'push up'
elif face == 5:
	result = 'tongue twister'
else:
	result = 'joke'
print(result)

time.sleep(5)