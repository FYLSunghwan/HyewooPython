#HYERICA 19년 1학기 컴퓨팅적 사고 기말고사 예상문제(학생제공용)
#8번 문제

data = [108, 32, 51, 234, 231, 123, 452, 123, 321, 109, 120, 178, 179, 192, 169]

sum = 0
count = 0
total_sum = 0
for i in data:
    total_sum+=i
    count+=1
avg = total_sum/count
for i in data:
    if i>=avg:
        sum+=i
print(avg)
print(sum)