import time
import math
#輸入半徑計算其圓周長和面積
radius = float(input('Please enter the radius: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('perimeter is: %.2f' % perimeter)
print('area is: %.2f' % area)
time.sleep(10)