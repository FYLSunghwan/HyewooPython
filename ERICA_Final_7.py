#HYERICA 19년 1학기 컴퓨팅적 사고 기말고사 예상문제(학생제공용)
#7번 문제
print("높이를 입력하세요:")
h = float(input())
cnt = 0
while 1:
    if h>=0.00001:
        cnt+=1
        h/=2.0
    else:
        break
print("공이 튀긴 횟수는",cnt,"회입니다.")

###왜 21횐지 이해X.
###22회가 맞음