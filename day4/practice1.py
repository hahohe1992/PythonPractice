import time
#用for迴圈實作1~100總和
sum = 0
for x in range(101):
	sum += x
print(sum)

#range可以用來產生一個不變的數列,且這個序列通常是用在(有規律)循環中
#range(101)可以產生一個0~100的整數序列
#range(1,100)可以產生一個1~99的整數序列
#range(1,100,2)可以產生一個1~99的奇數序列,其中2表示步長/序列的增量

#用for迴圈實作1~100的偶數總和
sum = 0
for x in range(0, 101, 2):
	sum += x
print(sum)

#透過循環中使用分支結構來實現相同功能
#用for迴圈實作1~100的偶數總和
sum = 0
for x in range(1, 101):
	if x % 2 == 0:
		sum += x
print(sum)

#while迴圈實現猜數字遊戲
#random出一個1~100的數字, 根據猜出來的數字分別給出"大/小/正確"的提示
import random
answer = random.randint(1, 100)
counter = 0
while True:
	counter += 1
	number = int(input("Please enter: "))
	if number < answer:
		print('guess bigger')
	elif number > answer:
		print('guess smaller')
	else:
		print('youre right!')
		break
print('youve guessed %d times' % counter)
if counter > 10:
	print('emmm...')

time.sleep(5)
