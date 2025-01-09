print("하위위위위")

a = 123
print(a)
a = 1.2
print(a)
a=0o177
print(a)
a=0x8ff
print(a)

# Python에서 반올림 (ROUND_HALF_EVEN)을 쓴다.
print(round(0.5))
round(1.5)
round(2.5)
round(3.5)
round(4.5)
round(5.5)
print(round(6.5))       # 수의 갯수 균형을 맞추기 위해서 짝수 .5의 반올림은 버림. 
print("""그말 인데\n \t 흠흠흠ㄴ\b\b그래
""")

a= 3.5
b= 125
print('%d'%a)
print('%f'%a)
print('%f'%b)
print('%f'%b)

a = 'I eat %d apple'%2
tmp ='world'
b='Hello {}'.format(tmp)

#list
a= [1, 2, 3]
print(a[0])
print(a[0] + a[2])
print(a[-1])

b=[1,2,3,['a','b','c']]
print(b[-1])
print(b[-1][0])

a= [1,2,3,4,5]
print(a[0:2])
print(a+b)
print(a*3)

a[2] = 4
print(a)
a[-1:-5] = b
print(a)

a[1:3] = []
print(a)

del a[1]
print(a)

c = [1,2,3]

c.append(4)
print(c)

c.append([5,6])
print(c)

c = [1, 3, 5, 2, 4]
c.sort()
print(c)

c = [1, 5, 4]
c.reverse()
print(c)

#  터틀쉽에서 linear x와 곡률은 변수로 설정해서 난수로 계속 바뀔 때 벽에 부딪히지 않게 코드를 짤 수 있게 끔 하기. 

marks = [55, 47, 79, 34]

number = 0
for mark in marks:
      if mark >= 50:
            print("%d번 샘플, 정상 수치 (%d)" %(number, marks[number]))
      else:
            print("%d번 샘플, 비정상 수치(%d)" %(number, marks[number]))

      number += 1


def sum(a, b):
      return a+b

print(sum(3, 9))

class Calculator:
      def __init__(self):
            self.result = 0

      def add(self, num):
            self.result += num
            return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(5))
print(cal1.add(8))
print(cal1.add(2))
print(cal1.add(7))


class FourCal:
      def __init__(self):
            self.first = 0
            self.second =0
            self.result = 0
      def setdata(self, first, second):
            self.first = first
            self.second = second

import tenserflow as tf
import numpy as np
import matplotlib.pyplot as plt


# 모듈을 스크립트로 직접 실행 시킬 때 __name_ = if 'main'으로 진행

# 예외 처리 try, except

try:
      4/0
except ZeroDivisionError as e:
      print(e)
# else, finally

enumerate() #리스트, 튜플, 문자열을 받아서, 인덱스와 값을 포함하여 리턴





