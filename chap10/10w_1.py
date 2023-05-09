#0509
import sys #시스템에서 가져오기
import numpy as np  #---> 설치 안되어 있을 때는 pip install numpy(터미널에) 하기 -> Ctrl+shift+p -> python select interpreter ->base 선택
import math #제일 큰 거 먼저 import

#np
np.array([1,2,3,4,5]) 
print(type(np.array([1,2,3,4,5])))

#arrnp
arrA=np.array([1,2,3,4,5])
arrB =np.array([6,7,8,9,10])

print(arrA+arrB)
print(arrA-arrB)
print(arrA*arrB)
print(arrA/arrB)

#math
from math import gcd, fsum #-> 자잘한거 사용시 import
print(math.fsum([1,2,3]))
print(math.gcd(10,20))
print(math.ceil(5.333))

#다른 파일 함수 import하기
#hello.py import 
import Hello as h  #--> 실행됨
h.helloworld()

#특정한 것만 name지어서 print 하기 ->다른 곳에서 import할 때, print문 나오는 것 방지
print("__name__:",__name__,"\n")

#하위 디렉터리가 많아도 import할 수 있음
from hong.ai import HelloData
HelloData.helloworld()