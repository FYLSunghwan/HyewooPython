#HYERICA 19년 1학기 컴퓨팅적 사고 기말고사 예상문제(학생제공용)
#9번 문제

sum = 0
count = 0

for i in range(2,10001,2):
    sum+=i
    count+=1

print(int(sum))
print(int(count))
print(int(sum/count))