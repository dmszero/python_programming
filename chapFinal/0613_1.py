#============== <22번-1>  ============= 
#자동차의 등록번호와 생산년도 , 배기량으로 구성된 딕셔너리가 있다.
carDict={'H101':('2017','3000'),'K333':('2018','3000'),'H222':('2020','3200'),
         'M293':('2021','3000'),'H156':('2022','3000'),'K450':('2023','2700')}


#다음과 같은 형식으로 출력하는 코드 만드시오.
#결과   H101:('2017,''3000')
#       K333:('2018,''3000')
#       H222:('2020,''3200')
#       M293:('2021,''3000')
#       H156:('2022,''3000')
#       K450':('2023,''2700')

#답
for key in carDict.keys():
    print(key,carDict[key])

for key, value in carDict.items():
    print(key,value)


#============== <22-2번> ==============
#생산년도로 구성된 각 요소가 int 형인 yearList 를 생성하고 출력하는 코드를 쓰시오
#결과
#  [2017,2018,2020,2021,2022,2023]

#답
yearList=[]
for value in carDict.values():
    yearList.append(int(value[0]))
print(yearList)


#============== <22-3>번 ===============
#생산년도를 입력받아 해당 년도에 생성된 자동차가 몇 대인지 출력하는 코드를 작성하시오
#결과
#생산년도를 입력하세오: 2020
#2020의 등록 차는 2대입니다.
#2020은 사용자 입력값

#답
year = input("생산년도를 입력하세요: ")
print(year,"의 등록차는",yearList.count(int(year)),"대 입니다")

#for문
count =0
year=input("생산년도 입력: ")
for claue in carDict.values():
    if value[0] == year:
        count=count+1

print(year,"의 등록차는",count,"대 입니다")

#딕셔너리 부분 공부




#============구기종목과 인원과의 관계===========
# 스포츠 구기종목:     sport =['축구','야구','농구','배구']     |    num=[11,9,5,6] 
# 두 개의 list를 zip으로 묶어서 dictionary로 나타낸후,
# 사용자로부터 종목이름을 입력받아서, 그에 맞는 인원수를 출력하라 
#조건 
# while문 사용
# quit만나면 종료
#다른종목 들어오면 '몰라요' 다시 입력 받, continue,break활용

sport =['축구','야구','농구','배구'] 
num=[11,9,5,6]
sportDic=dict(zip(sport,num))

while 1:
    input_sport=input("종목이름을 입력하세요 인원 수를 알려줍니다: ")
    if input_sport=='quit':
        print("quit 입력 종료")
        break
    if input_sport in sportDic.keys():  
        print("인원수", sportDic[i])
    else:
        print("다른 종목 입력함. 모름")
        continue
    print(input_sport,"정보를 서치했습니다")
print("종료")


#================ lambda 함수 작성 ==============
#map, filter
#입력 숫자 하나 받고 출력으로 숫자 +1를 하는 함수

def addone(num): 
    return num +1
print(addone(10))

#lambda입력값: return 값
print((lambda num : num+1)(10))

#1.숫자 두개 입력받아서 합은 return 하는 함수
print((lambda n1,n2:n1+n2)(10,30))
def sum(n1,n2):
    return n1+n2

#2.숫지 두개를 입력받아서 a,b 입력, a%b를 출력하라.
print((lambda a,b:a%b)(10,30))
def cal(a,b):
    return a%b

#map(),filter()함께 쓰이는 lambda
'''print((lambda num:num+1)(10))
[20,22,23,24,25,26]
=>[21,23,24,25,26,27]
map(function, 입력값 리스트)'''

print(list(map(lambda num:num+1,[20,22,23,24,25,26])))


map(function,list1, list2)
#1.숫자 두개 입력받아서 합을 return 하는 함수
list1=[100,200,300,400]
list2=[5,2,4,10]

print(list(map(lambda n1,n2 :n1+n2,list1,list2)))


#2.숫자 두개를 입력받아서 a,b 입력, a%b를 출력하라.
print(tuple(map(lambda n1,n2: n1%n2,list1,list2)))
print(tuple(map(lambda n1,n2: n1/n2,list1,list2)))

#3.filter를 사용하여 list[1,-2,3,-5,8,-3]에서 음수를 모두 제거하자
#filter(function,list)
print(filter(lambda x: x>0,[1,-2,3,-5,8,-3]))
print(list(filter(lambda x: x>0,[1,-2,3,-5,8,-3])))


