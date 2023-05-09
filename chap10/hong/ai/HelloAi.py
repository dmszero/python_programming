#hello.py
def helloworld():
    print("hello world!!")

#import했을 때 작동하지 않도록 name 짓기
if __name__=="__main__":
    print("오늘 날씨는 24도 입니다.")
    print("오늘은 모듈 처음 배운 날")
    helloworld()
else:
    print("hello.py __name__")