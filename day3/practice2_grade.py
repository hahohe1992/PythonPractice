import time
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