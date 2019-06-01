import time
import math
#計算輸入的年份是否為閏年
year = int(input('Please enter a year: '))
#若代碼太長,寫成一行不便閱讀, 可以使用\或()拆行
is_leap = (year % 4 == 0 and year % 100 != 0 or
			year % 400 == 0)
print(is_leap)

time.sleep(10)