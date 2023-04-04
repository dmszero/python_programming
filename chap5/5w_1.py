#0404 5주차 
#ppt 9차시


str= "파이썬은 파이썬은 파이썬은 파이썬은 파이썬은 파이썬은"
newnewstr ="파이썬은 , 하하하, 호호호,하하하, 파이썬은"

print(newnewstr.split(","))
print(str.find("파이썬"))
print(str.find("파"))
print(str.find("썬"))
print(str.index("파이썬")) #find 와 index 는 비슷하지만, 없는 단어를 입력하면 index는 에러가 뜸. --> 명확하지 않은 단어 찾을 때는 find 가 나음
print(str.index("파"))
print(str.index("썬")) 


print(2,"+",3,"=",5)
print('{}+{}={}'.format(2,3,5))

a,b =5,10.0000
print('{}+{}={}'.format(a,b,a+b))
print('{0:d}+{1:f}={2:f}'.format(a,b,a+b))

#
value = False
print(type(value))
print(int(value)) 

print(bool(0),bool(1),bool(1.12222),bool(-12))
print(bool("dsssdfrd"),bool("-1"),bool(""),bool(-12))  #아무것도 없는 빈칸은 false /string 은 어떤 문자 들어가도 true

