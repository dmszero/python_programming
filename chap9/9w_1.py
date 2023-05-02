#0502
#=======함수  ---> input 주면 output 나옴==========
'''
input - 숫자 - num1
output = 숫자 -output_num
이런 기능을 하는 function -multi
''' 

#funtion 
# Ex1) 3을 곱하는 함수
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