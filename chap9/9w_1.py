#0502
#=======함수  ---> input 주면 output 나옴==========
'''
input - 숫자 - num1
output = 숫자 -output_num
이런 기능을 하는 function -multi
''' 

#funtion 
# Ex1) 3을 곱하는 함수
'''
def multi (num1) : # 들여쓰기 주의
    output_num = num1 *3
    print("여기는 multi 함수 안입니다.")
    return output_num

# 정의한 함수 호출 (함수 정의 후에 호출 가능함)
print(multi(10)) #return 30

# Ex2) hello 함수 정의하여 사람 호출하기
def hello(p1="james",p2="lena"):
    print("hello,",p1)
    print("hello,",p2)

print("=기본값=")
hello()
print("=사용자값=")
hello('eileen','mark')

# Ex3) 두 개의 숫자 입력받아, 두 개의 합을 함수 내에서 출력
def mysum(num1,num2):
    print("두 숫자의 합:",num1+num2)
mysum(100,1000)

def mysum2(num1,num2):
    return num1+num2
result =mysum2(100,2000) #return 2100
print(result)
print(mysum2(100,2000))


# === 지역 변수, 전역 변수 ===
# Ex1)
num=100 #global variable 전역 변수
print("num: ", num)
def addone():
    num =10 # 내부 함수에서 num을 수정하지 않아도 실행 가능 (위에 선언된 전역변수로 실행됨)
    print("addone():",num+1) #num+1==>11
    print("addone() num:",num) #num=>10
    num = num*8+20
    return num
result1= addone()
print("***num: ", num) #100
print("***num: ", result1)


# Ex2)
#내부 함수에서 전역변수 사용하면 좋겠고
#수정과 함수가 끝나도 그 값이 반영되었으면 좋겠음 ---> 내부 function에 global num (전역변수) 선언
num=100 #global variable 전역 변수
print("num: ", num)
def addone():
    global num  #전역변수 사용하겠음 -> 변수에 새로운 값 대입가능 (밖에 있는 전역변수 사용 중)
    num =num+1
   
addone()
print("***num: ", num)

#======= 인자 갯수 여러개 ---> * 사용 =======
# Ex4)
#인자의 갯수가 여러 개인 경우
print()
print(1,2,3,4,5,6,7,8,9)
print()
def hello2(*names):
    for i in names:
        print("hello,",i) #hello홍길동
hello2("홍길동","김길동","고길동")

#Ex5)
# 여러 개 인자의 합을 구하는 함수
def Sum(*numbers): # *가 있으면 갯수 상관없이
    result =0
    for i in numbers:
        result = result+i
    return result
print(Sum(1,2,3,4,5))
l1=[1,2,3,4,5,6,7,8,9,10]
print(Sum(*l1))


#딕셔너리를 이용한 함수
#dictionary = {key1:value,key2:value2} 
coffee ={"americano":2000,"latte":3000,"tea":4000} 
def printmenu(**keyvalue):
    for k in keyvalue:
        print(k,keyvalue[k])

printmenu(**coffee)
printmenu(hotchoco=3000,pizza=6000,coke=2000)

def fun1(*num,**menu):
    #num들의 합
    result1 = 0
    for i in num:
        result = result +i
    return result
    # menu출력
    for k in menu:
        print(k,menu[k])
l1=[1,2,3,4,5,6,7,8,9,10]
coffee ={"americano":2000,"latte":3000,"tea":4000} 

fun1(*l1,*coffee)
'''

#========== lambda function ============
#function을 만드는데, 이름짓기가 귀찮다. 실행문이 하나 밖에 없다
def addone(x):
    return x +1
print(addone(100))

#lambda parameter_name : parameter로 실행하는 문
print((lambda x:x+1)(100)) # addone(100) = (100)--> 두 개 똑같음

def mysum2(num1,num2):
    return num1+num2
print(mysum2(200,2000))
print((lambda num1,num2 : num1+num2)(200,2000))


#======map, filter =======
#map---> map(함수, input 리스트)
'''l2=[1,2,3,4,5]
addone()
l3=[2,3,4,5,6,7]
map(addone,l2)  #---->l3

#map(lambda함수, input 리스트)
#map(addone,l2)(lambda x: x+1)(100)
print(list(map(lambda x :x+1,l2)))
'''

#lambda n1,n2 : n1+n2
l1=[1,2,3,4,5,6,7,8,9,10]
l2=[1,2,3,4,5]
print(list(map(lambda n1,n2 : n1+n2,l1,l2)))