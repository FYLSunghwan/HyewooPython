#HYERICA 19년 1학기 컴퓨팅적 사고 기말고사 예상문제(학생제공용)
#6번 문제
print("몇 학기를 수료했는지 입력하세요:")
sem = int(input())
print("평균 학점을 입력하세요(4.5 만점):")
scr = float(input())

per = 0.0

if sem<=8:
    if scr>=4.0:
        per=1.0
    elif scr>=3.5:
        per=0.5
    elif scr>=3.0:
        per=0.3
print("등록금의 {:d}%를 장학금으로 받을 수 있다.".format(int(per*100)))