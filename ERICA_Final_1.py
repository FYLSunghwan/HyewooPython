#HYERICA 19년 1학기 컴퓨팅적 사고 기말고사 예상문제(학생제공용)
#1번 문제 <점수 입력 후 성적 출력하기>
print("점수를 입력하세요:")
score = int(input())
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")
