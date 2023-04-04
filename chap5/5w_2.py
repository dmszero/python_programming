#0404

#제어문
#if문 -- ppt 12차시

#표준 if문
''' if 조건:
    실행문1
else :
    샐행문2 '''

#if문 예제1 - 시간
''' hour =15
if hour <12:
    print("12시가 지났으니 오후입니다.")
elif hour <18:                                                    # else if =elif
    print("12시가 지나고, 18시가 안지났으니 오후입니다")
else:
    print("12시가 지나지 않았으니 오전입니다." "\n")
1

#if문 예시2 - 장학금
score_str = input('점수는?')
score = int(score_str)
if score <200:
    print("장학금 50만원 지급")
elif score<400:
    print("100만원 지급")
else:
    print("200만원 지급",'\n')

#if문 예시3 - 점심식사
answer = input("Do you wanna Subway sandwich? yes or no --->> ")
if answer=='yes':
    print('8 building 1st floor')
else: 
    again_answer =input ("Do you wanna cafeteria?")
    if again_answer =='yes':
        print("8 building 3rd floor")
    else:
        print('you can eat another food') '''




#반목문
#for문 -- ppt 13차시

#for문 1
for i in 1,3,4,5,6,8:
    print(i)

#for문 2
print("range1")
for i in range(0,11,1):
    print(i)

#for문 3
print("range2")
for i in range(11):
    print (i)

#for문 예제1 -- 1부터 10까지 합 출력
sum =0
for i in range(1,11,1):
    sum = sum+i
    print(i,"번째 sum은",sum)
    #sum+=1
else:
    print("for 문의 조건이 더이상 만족하지 않습니다.")
    print('i가 range(11)에서 벗어남')
    print("for 문이 break 나 continue로 종료된게 아니라 정상종료에만 실행")
print("sum: ",sum)


#for문 예쩨 2 -- 놀이기구 탑승(4명이 탑승 가능, 키 150 이상)
