import time
#使用變量保存數據並進行算術運算
a = 321
b = 123
print('a + b = ', a + b)
print('a - b = ', a - b)
print('a * b = ', a * b)
print('a / b = ', a / b)
print('a // b = ', a // b)
print('a % b = ', a % b)
print('a ** b = ', a ** b)

#使用input函數輸入
#使用int()進行類型轉換
#用佔位符號格式化輸出的字符串
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %d' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

"""
使用type()檢查變量的類型
"""

a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world!'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

#運算符的使用
a = 5
b = 10
c = 3
d = 4
e = 5
print('a0 = ', a)
a += b
print('a1 = ', a)
a -= c
print('a2 = ', a)
a *= d
print('a3 = ', a)
a /= e
print('a4 = ', a)

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print('flag1 = ', flag1)
print('flag2 = ', flag2)
print('flag3 = ', flag3)
print('flag4 = ', flag4)
print('flag5 = ', flag5)
print(flag1 is True)
print(flag2 is not True)

#類型轉換
a = 100
b = str(a)
c = 12.345
d = str(c)
e = '123'
f = int(e)
g = '123.456'
h = float(g)
i = False
j = str(i)
k = 'hello'
m = bool(k)
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))
print(e)
print(type(e))
print(f)
print(type(f))
print(g)
print(type(g))
print(h)
print(type(h))
print(i)
print(type(i))
print(j)
print(type(j))
print(k)
print(type(k))
print(m)
print(type(m))


time.sleep(5)