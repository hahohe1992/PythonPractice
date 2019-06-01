import time

#輸出9x9乘法表
for i in range(1, 10):
	for j in range(1, i+1):
		print('%d * %d = %d' % (i, j, i * j), end = '\t')
	print()

#判斷輸入的數字是否為質數
from math import sqrt
num = int(input('Please enter a positive integer: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
	if num % x == 0:
		is_prime = False
		break
if is_prime and num != 1:
	print('%d is a prime number.' % num)
else:
	print('%d is not a prime number.' % num)

#找出兩個輸入正整數的最大公因數和最小公倍數
x = int(input('x = '))
y = int(input('y = '))
if x > y :
	x, y = y, x
for factor in range(x, 0, -1):
	if x % factor == 0 and y % factor == 0:
		print('The GCD of %d and %d is %d' % (x, y, factor))
		print('The LCM of %d and %d is %d' % (x, y, x * y // factor))
		break

#列印出各種三角形圖案
row = int(input('rows you want: '))
for i in range(row):
	for j in range(i + 1):
		print('*', end = ' ')
	print()

for i in range(row):
	for j in range(row):
		if j < row - i - 1:
			print(' ', end = ' ')
		else:
			print('*', end = ' ')
	print()

for i in range(row):
	for j in range(row - i - 1):
		print(' ', end = ' ')
	for j in range(2 * i + 1):
		print('*', end = ' ')
	print()



time.sleep(10)