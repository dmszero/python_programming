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

