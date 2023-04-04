#ppt 8차시

#str
var= "python"
ch1= var[0]
print(var[0]," ",var[1]," ",var[2], " ")
print(var[-3]," ",var[-2]," ",var[-1])

print(var[0]," :",var[-6])
print("length of var: ",len(var))

print('PYTHON'[0], 'PYTHON'[2],"\n")

#슬라이싱 양수
print('python'[1:5])
print('python'[2:4])
print('python' [0:3])
print('python' [0:len('python')],"\n")

#슬라이싱 음수(음수를 이용한 문자열 슬라이싱은 복잡해서 시험 안나옴)
print('python'[-5:-1])
print('python'[-4:-2])
print('python' [-6:-3])
print('python' [-len('python'):-1],"\n")

#문자열 다루기 (start,end)
print('python'[:3])
print('python'[:4])
print('python'[1:])
print('python'[2:])
print('python'[:],"\n") #전체 반환

#슬라이싱으로 문자열의 부분 문자열 참조
str = 'Monty Python'
print(len(str))
print(str[0:5],str[6:],str[6:12])
print(str[-12:-7],str[-6:],str[-6:])

#a
print('abcdf'+'\b'+'c')
print('hello\n world')
print('aaaaa\v bbbb\vcccccc' "\n")

#ppt 9차시
#string method
str_var="하하하호호"
#type(str_var) =>str
print(str_var.replace("하",'호'),"\n")

str_var2= '안녕하세요. 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 수업입니다.'
str_var3=str_var2.replace('파이썬','자바',3) #str_var2의 파이썬을 자바로 바꾸는데 3개만8
print('str_var2',str_var2)
print('str_var3', str_var3)
print(str_var2.replace('파이썬','자바'))


#실수를 입력 받음
num_str = ("실수를 입력")
num_str.replace(".","") #-----> 실수의 소수점을 공백으로 바꿈 즉 실수에서 정수로 바뀜
sum = int(num_str[0])+int(num_str[1])+int(num_str[2])+int(num_str[3])+int(num_str[4])
print("sum: ", sum)
