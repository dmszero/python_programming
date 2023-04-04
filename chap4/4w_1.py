#0328.py 변수와 키워드 다양한 연산자


i =3
''' 3 = ii
print(ii)
'''

'''
# a+=b
a=10
b=5
a+=b #a=a+b=10+5=15
print(a)

#a -= b
a=10
b=5
a-=b
print('a+=b : a=',a,"\n")

#a *= b
a =10
b=5
a*=b
print('a*=b : a=',a,"\n")


#input()
name= input("what's your namae?")
print("my name is",name,"\n") 

yearclass2 = input("what's your class?")
print("my class is",yearclass2,"\n")
print(type(yearclass2))

age = input("what's your age?")
print("i'm",age,"years old")
print(type(age))
print("my dad age is 30 more than my age, so ",int(age+30),"years old")
'''

#int()
#float()
#str()
a=10
str_a=str(a)
print("type(a): ", type(a))
print("type(str_a): ",type(str_a))

#행성 지구 반지름을 입력받아 지구 둘레 길이 구하기(6차시ppt)
planet =input('choose the planet')
strRadius = input(planet+'the radius?')
radius =int(strRadius)

length =2*3.14*radius
print(planet,'radius:',radius)
print(planet,'length: ',length)

