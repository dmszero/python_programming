print("식당에서 계산하고 거스름돈 돌려받기 78000원이 나왔는데 5만원권, 1만원권, 5천원 지폐를 몇개 씩 지불할까?")

a = 78000 // 50000
print("5 만원권", a ,"장 냅니다")
result = 78000 % 50000
print(result , "원 남았습니다.")
b= result // 10000
print("만원짜리 지폐",b , "장 냅니다.")
c= result // 5000
print("오천원짜리 지폐",c,"장 냅니다")