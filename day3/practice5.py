import time
import math
#百分制成績轉等級制成績
score = float(input('enter your score: '))
if score >= 90:
	grade = 'A'
elif score >= 80:
	grade = 'B'
elif score >= 70:
	grade = 'C'
elif score >= 60:
	grade = 'D'
else:
	grade = 'F'
print('your grade is: ', grade)

time.sleep(5)

#輸入三邊長,若能夠成三角形就計算其周長和面積
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
	print('perimeter: %f' % (a + b + c))
	p = (a + b + c) / 2
	#海龍公式
	area = math.sqrt(p * (p - a) * (p - b) * (p - c))
	print('area: %f' % (area))
else:
	print('cant make a triangle.')

time.sleep(5)

#輸入月收入和五險一金來計算個人所得稅
salary = float(input('monthly income: '))
insurance = float(input('insurance: '))
diff = salary - insurance - 3500
if diff <= 0:
	rate = 0
	deduction = 0
elif diff < 1500:
	rate = 0.03
	deduction = 0
elif diff < 4500:
	rate = 0.1
	deduction = 105
elif diff < 9000:
	rate = 0.2
	deduction = 555
elif diff < 35000:
	rate = 0.25
	deduction = 1005
elif diff < 55000:
	rate = 0.3
	deduction = 2755
elif diff < 80000:
	rate = 0.35
	deduction = 5505
else:
	rate = 0.45
	deduction = 13505
tax = abs(diff * rate - deduction)
print('personal tax: $%.2f' % tax)
print('real income: $%.2f' % (diff + 3500 - tax))

time.sleep(5)