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
print(list3,'\n')


print('==============list_ food 예제================')
#===========list food 예제=============
#list insert _food 
food =[]
food.append("chicken")
food.append("sandwich")
print(food)
food.insert(0,"pizza") # insert 'pizza' into list's 1st
print(food)
food.insert(2,"pasta")
print(food)
food.remove('chicken') # delete 'chicken'
print(food,'\n')

#pop --> food list 에서 빼내기
print("food.pop :", food.pop())
print(food)
print("food.pop:",food.pop())
print(food,'\n')

#<서로 다른 list를 합치는 예제>
print(food)
dessert =['coffe','cake','waffle']
#Ex1) 새로운 list를 생성
food_list = food + dessert  
print(food_list)
#Ex2) extend 사용
food.extend(dessert)
print(food,'\n')

#reverse -> 순서를 거꾸로 한다.
print(food)
food.reverse() 
print(food)

#food.clear()
'''del food
print(food)'''

#sort()
#sorted()
l1 = ['banana','apple','orange','mango']
print(l1)
print("sorted(l1): ",sorted(l1))
print("l1:",l1)
print("li: ",l1)

l1.sort()
print(l1,'\n')



print('=============리스트 컴프리헨션================')
#=============리스트 컴프리헨션 ()================

# 예제1 ---- <0~10까지 숫자를 가지는 list 작성 >
#방법1) for 문 사용
l3=[0,1,2,3,4,5,6,7,8,9,10]
l3=[]
for i in range(11) :
    l3.append(i)
print(l3)

#방법2) 리스트 컴프리 헨션 사용
# 리스트 컴프리헨션
'''리스트 변수명 = [i for i in range()]'''
l3 = [i for i in range(11)] # 0~10까지 있는 range i를 i 에 넣어라
print(l3)

# 예제 2 ---- <0~10까지 숫자의 제곱을 원소로 가지는 리스트 작성>
l3 = [ i*i for i in range(11)] # -----> i*i == i**2
print(l3)

# 예제 3 ---- <0~10까지 숫자의 3배를 원소로 가지는 리스트 작성>
l3 = [i*3 for i in range(11)]
print(l3)

# 예제 4 ---- < hello 를 10개 가지는 리스트 작성>
l4 = ['hello']
l4 = [ 'hello' for i in range(10)] #----> for문을 적고 그 앞에 넣고 싶은 리스트 입력
print(l4)

''' <str 다른 방법>
l4=[]
for i in range(10)
    l4.apeend("hello") '''

# 예제 5 ---- < 0~10 까지의 숫자의 제곱을 리스트로 작성  -> 짝수의 제곱만 넣기>
'''if i in range(11):
    if i %2 ==0 :
        l3.append(i**2)
print(l3) '''

l3 = [ i**2 for i in range(11) if i%2==0]
print(l3)






#=========shallow copy==========

wishlist= food
print("food:   ", food)
print("wishlist:  ",wishlist)

food.pop()
print("after food.pop()")
print("food:   ",food)
print("wishlist:  ", wishlist)

print(food is wishlist)


#=========deep copy=============
food2 = food[:]
food3= list(food)

print('deep copy')
print('food:   ',food)
print('food2:  ', food2)
print(food is food2)
food2.append("bulgogi")
print('food:   ', food)
print('food2:  ',food2)

food.append('steak')
print('food:   ', food)
print('wishlist: ',wishlist)
print('food2:  ',food2)