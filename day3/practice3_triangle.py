import time
import math
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