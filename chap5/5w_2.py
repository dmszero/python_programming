#0404

#제어문
#======== 제어문 --- if문(ppt 12차시) ==========

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




#======= 반목문 1 ---for문 ========
#for문 -- ppt 13차시

#for문 1
''' for i in 1,3,4,5,6,8:
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
print("sum: ",sum) '''



#====== 반복문 2 ---while문 =========
#while문

#표준 while문
'''while 조건:
    수행문

# while문 1
i=10
while i>5 :
    print(i," 는 5보다 크다.") 
    i=i-1

#while문 예제1 -- n=1부터 5까지 찍어보는 프로그래밍
#1 2 3 4 5 
i=1
while i<=5:
    print(i,end='  **  ')
    i=i+1
else:
    print("while이 잘 끝남")
    print('현재 i의 값은',i,"d입니다.")'''




# =======<if 문과 while 문 예시> ---- 놀이 기구 탑승===========
#조건:
#4명 탑승 가능 5명 불가
#입력 키를 받음
#탑승인원 체크, 키 체크
#while 문을 끝내는 조건 --> 사람이 4명을 채웠나?

''' <코드 짜기>
    while 5명이 아닐 것:
    150 이 넘는가>
    -yes:
    -no:
else:
    4명이 탔습니다. 놀이기구 출발'''

'''people_str =0
people_str = input("몇명이 탑승하나요?")
people =int(people_str)
while people < 5:
    height = input("키는?")
    int_height = int(height)
    if int_height<150:
        people = people +1
        print("한명 탑승")
        print("현재 인원: ",people)
    else:
        print("탑승불가")
else:
    print("놀이기구 출발")'''


#========continue 와  break==========
#반복문 중간에 반복을 더이상 하지 않고 실행을 종료
#반목분 안에서 실행, 주로 if문 안쪽에서 사용됨 --> if문에 영향 안가고 반목문에 영향
#break는 모두 다끝내버리고 continue는

#예시 1
#input 으로 입력 받음
#무한반복 
#exit 라는 값 받음 -> 입력 받는 것 종료
#apple -> input the word 'apple 

while True :
    str = input ("enter the word==> ")
    if str== "exit":
        print("you enter the 'exit' ==> end")
        break
    else:
        if str =='apple':
            print('input the word "apple"')
            print("continue play")
            continue
        print("you enter the this word ==> ",str)
    
    print("stil in 'while' ")

print('end the "while" ')





#위에꺼 변영해서 test
#input 으로 입력 받음
#무한반복 
#exit 라는 값 받음 -> 입력 받는 것 종료
#apple 입력 -> input the word 'apple" 하고 다시 입력받기
#그 외의 단어 입력 받음 -> 해당 단어를 3번 찍어줄것,
#continue , break를 활용

while True :
    str=input("enter the word ==> ")
    if str == exit:
        print("you enter the 'exit' ==> end")
        break
    else:
        if str == 'apple':
            print('input the word "apple"')
            continue
        else:
            print('you enter the this word ==> 0',str,str,str)
print("end the 'while'")


