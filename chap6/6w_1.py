#0411
#리스트, 튜플, 딕셔너리, 집합

#리스트 ppt 16차시
['kim ','lee','park','choi']

#튜플 -----------------------> can't modify (insert, append, change data etc.) but list can
('kim ','lee','park','choi')

#딕셔너리 -> 사전 {key:value,k1:v1,k2:v2,....}
address = {'홍길동':'서울','김길동':'부천','james':'미국'}
print(address['홍길동'])

#=============list================
#숫자, int, float, string 다 가능함
lst = [10,20,30,40,50]
str_list = ['apple','banana']
print(type(lst))
print(lst[0]," ",lst[1]," ",lst[len(lst)-1],"\n")  #--->length는 1부터 시작하기 때문에 마지막 값을 출력하고 싶으면 len()-1 써야함

#빈 리스트 생성 -> 하나씩 원소를 추가
list1=[]
#list2=list()
print(list1)
list1.append('python')
list1.append('java')
list1.append('c++')
print(list1)
print(list1[0],"\n")

print("========for1=======")
for i in range(len(list1)): #range(3) -> 0,1,2
    print(list1[i])

print("========for2=======")
for i in list1: #same = for i in {python,java,c++}
    print(i,"\n")

print(list1)
print("count :",list1.count("python")) # the word 'python's count
print("index :",list1.index("python"),"\n") # the word 'python's index

#list_modify

list1[0]="AI"
list1[2]= "IOT"
print(list1)

#['AI','java','IOT','python','python','python','python']
list2= list1[0:3:1] #0,1,2 -> 'AI', 'java', 'IOT'
print(list2) 
list2 = list1[1:5:1] #-> 'java', 'IOT'
print(list2)
list2 = list1[1:len(list1):2] #->'java'
print(list2)
list2 = list1[2:6:3] #->'IOT'
print(list2)
list2 = list1[::-1] #->'IOT', 'java', 'AI'
print(list2)


#list1, list3
#list1의 일부를 list3에 대입 

list2 = list1[2:6:3]
['IOT','python']
print(list2)
list3=[1,2,3,4,5,6,7,8]

#list3[1]=list2
#print(list3)
list3[1:2]=list2
print(list3)

#=============tuple================