d={}
n=int(input())
for i in range(n):
    input1=list(map(str, input().split(",")))
    studentId=int(input1[0])
    studentName=input1[1]
    d[studentId]=studentName
inputId=int(input())
print(d[inputId])