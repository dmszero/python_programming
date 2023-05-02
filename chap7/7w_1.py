#0418
#튜플, 딕셔너리, 집합

#=======list===========
#리스트는 수정, 변경, 일부 원소 삭제 가능함
lst =[]

#===========tuple============
#수정 불가 => 튜플
#tuple
#  Ex1)
'''
t1 =(1,2,3,4)
print(t1)
t2= tuple()
print(t2)
t3=1,2,4,5,10
print(type(t3))

print(t3.index(3))
print(t3.count(3))
'''
#tuple
#  Ex2)
t4= 1,2,3,4,5,3,3,10,3
t5=100,200,300
print("t4+t5:",t4+t5)
print("t4: ",t4)
print("t5: ",t5)

#sort 
#원본은 안바뀜 -->sorted() -->tuple can use
print(sorted(t4) ,"\n")
#원본이 바뀜 ---->lst.sort()



#===========dictionary===========
#key: value -->key르
d1={1001:"홍길동",1002:"김길동",1003:"고길동",1004:"이길동"}
print(d1[1001])
# print(d1[0])--- error -> cause) only can key(1001, 1002, 1003, 1004)


#dictionary 
# Ex1)
#빈 dictionary 만들기
#d2={} , 강좌 딕셔너리
d2=dict()
d2['강좌명']='파이썬'
d2['개설 요일'] ='화요일'
d2['년도'] =2023
d2['수강생'] =['김','이','정']
print("d2: ",d2)
print(d2['수강생'])
print(len(d2),"\n")

# Ex2)
#dictionary의 key:value => 1:jan 2:feb ...12:dec
print("====================== < for문을 돌려서 각각의 value 찍기 > ====================")
month ={1:'jan',2:'feb',3:'mar',4:'apr',5:'may',6:'jun',7:"july",8:'aug',9:"sep",10:"oct",11:"nov",12:"dec"}
for i in range(1,13): #---->1~12까지
    print(month[i],'\n')

# Ex3)
#dictionary method
print("month.keys(): ", month.keys())
print("month.vlaues(): ",month.values())
print("month.items(): ",month.items())

# <Ex3을 적용한 활용 예제 : for문 돌려서 각각의 vlaue 찍기>
#month.keys() 활용
for i in month.keys(): #---> [1,2,3,4,5,6..,12]
    print(month[i])

#month.values() 활용
for i in month.values(): #--->[jan,feb,mar,apr...dec]
    print(i)

#month.items() 활용
for i in month.items():  #---> (1,jan) (2,feb)
    print(i,"\n")

#month 활용
for i in month: #--> month = month.keys()
    print(i)  #key -10
    print(month[i]) #value

#Ex4) 삭제
# pop()
print("month.pop(1) :", month.pop(1)) #----> key값을 주고, 해당 item을 제거
print(month)

# popitema()
print("month.popitem() : ",month.popitem()) #----> 제일 마지막 item을 제거
print(month,"\n")

#Ex5) 수정
# update() --> 기존의 키 값이 업데이트 한 값으로 바뀜, 키 값이 없으면 새롭게 키가 추가됨
month.update({3:'3월'})
print(month)
month.update({15:"15월"})
print(month)


#======== dictionary - tuple -list 변환 =========
#tuple =>변경, 수정 불가 
#tuple -> list 로 변경  
seqli=['a','b','c','d']
#list를 tuple로 바꿈
seqtu=tuple(seqli)
print(seqtu)
print(type(seqtu))

#tuple을 list로 변경
seqli2= list(seqtu)
print(seqli2)
print(type(seqli2))

#list를 dictionary로 변경
seqd=dict(enumerate(seqli))
print(seqd)
print(type(seqd))

#========= zip ============
#list,tuple 이 여러개 ->하나의 튜플 조합으로 된 리스트
# Ex1)
l1=['1조','2조','3조']
YA =['홍','김','이']
YB =['최','한','James']

z= zip(l1,YA,YB)
print(type(z))
print(z)
print(list(z)) #--> z를 list로 바꿈
print(tuple(zip(l1,YA,YB))) #--> zip 을 다시 선언후 tuple로 변경

# Ex2)
l2 = ['한식','양식','중식','분식']
l3 =['전주식당','홍콩반점','청년다방','취성루']
l4=['피자','제육','파스타','김밥']
print(list(zip(l2,l3,l4)))

for i in range(4) :
    print(l2[i],l3[i],l4[i])

l5 = list(zip(l2,l3,l4))
for i in l5 :
    print(i[0],i[1],i[2])

#두개의 리스트를 dictionary 로 바꿀 때는 무조건 zip 이 필요함
print()
print(dict(zip(l2,l3)))

#enmurate 이용
print(list(enumerate(l2)))
print(dict(enumerate(l2)))

#dictionary로 만든다