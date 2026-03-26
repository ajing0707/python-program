#변수 선언
select = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계:"))

#1번 계산
if select == 1 :
    select_1 = input(" *** 수식을 입력하세요 : ")
    answer1 = eval(select_1)
    print("%s 결과는  %s입니다." % (select_1, answer1))

#2번 계산
elif select == 2 :
    select_2_1 = int(input(" *** 첫 번째 숫자를 입력하세요 : "))
    select_2_2 = int(input(" *** 두 번째 숫자를 입력하세요 : "))
    
    answer2 = 0
    for i in range(select_2_1, select_2_2 + 1) :    
        answer2 += i
    
    print("%d+...+%d는 %d입니다." % (select_2_1, select_2_2, answer2))
