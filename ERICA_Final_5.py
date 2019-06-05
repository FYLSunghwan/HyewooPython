#HYERICA 19년 1학기 컴퓨팅적 사고 기말고사 예상문제(학생제공용)
#5번 문제
import random
cnt=0
while(1):
    cnt+=1
    inp = int(input())
    rnd = random.randint(1,100)
    if inp==rnd:
        print("축하합니다. 시도횟수는 {}회입니다.".format(cnt))
        break;
    elif inp>rnd:
        print("랜덤값이 낮음")
    else:
        print("랜덤값이 높음")
    print("정답은 {}입니다.".format(rnd))
