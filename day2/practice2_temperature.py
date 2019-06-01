import time
#華氏轉攝氏溫度
#F = 1.8C + 32
f = float(input('請輸入華氏溫度: '))
c = (f - 32) / 1.8
print('轉換後的攝氏溫度為: ', c)
print('%1f華氏溫度 = %.1f攝氏溫度' % (f, c))
time.sleep(10)