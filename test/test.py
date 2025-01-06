True 
if(True):
    print("sksnrlehgkjdkladljfa;jk")

students = [('철수',92), ('영미', 77), ('동수',85)]

for (i, j) in students:
    if j>=90:
        print(i,"A")
    elif j>= 80:
        print(i, "B")
    else:
        print(i,"C")

start = int(input("시작하는 단: "))
end = int(input("끝나는 단: "))

for i in range(start,end+1):
    print(i,'단')
    for j in range(1, 10):
        print(i,'X', j, "=", i*j)
    print(' ')

class Student:
    count = 0

    def __init__(self, n, a):
        self.name = n
        self.age = a
        Student.count += 1

    def hello(self):
        print("Hi, my name is %s, " % self.name)

    def myage(self):
        print("My age is %d. " % self.age)

a = Student('Adam', 20)
a.hello()
a.myage()
print("학생 수 = %d " % Student.count)
b= Student('Smith', 32)
b.hello()
b.myage()
print(" 학생 수 = %d"%Student.count)
