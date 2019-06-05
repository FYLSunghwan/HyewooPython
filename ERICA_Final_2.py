#HYERICA 19년 1학기 컴퓨팅적 사고 기말고사 예상문제(학생제공용)
#2번 문제
print("시작값을 입력하세요:")
st = int(input())
print("종료값을 입력하세요:")
ed = int(input())
print("증가값을 입력하세요:")
add = int(input())
print("{}에서 {}까지의 {}씩 증가시킨 값의 합계:".format(st,ed,add))
sum = 0
for i in range(st,ed,add):
    sum+=i
print(sum)