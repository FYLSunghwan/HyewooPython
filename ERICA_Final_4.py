#HYERICA 19년 1학기 컴퓨팅적 사고 기말고사 예상문제(학생제공용)
#4번 문제
name_list = []
while 1:
    print("이름을 입력하세요(종료를 원하시면 '1'을 입력하세요):")
    inp = input()
    if inp==1:
        break
    if inp in name_list:
        print("같은 이름이 이미 존재합니다.")
    else:
        name_list.append(inp)