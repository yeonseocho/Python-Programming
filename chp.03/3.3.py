### 반복문

##3.3.1 while

#1) 카운터와 누적변수
cnt=tot=0
while cnt<5:
    cnt+=1
    tot+=cnt
    print(cnt, tot)

#1 ~100 사이의 3의 배수 합과 원소 추출하기
cnt=tot=0
dataset=[] #빈 list

while cnt<100:
    cnt+=1
    if cnt % 3==0:
        tot+=cnt #누적변수
        dataset.append(cnt)
print('1-100 사이의 3의 배수 합=%d' %tot)
print('dataset=',dataset)

#무한루프
numData=[]
while True:
    num=int(input("숫자 입력: "))

    if num % 10==0:
        print("프로그램 종료")
        break
    else:
        print(num)
        numData.append(num)

#3.3.2 random 모듈
#1)random module 추가
import random
help(random)
#2)random 모듈의 함수 도우말
help(random.random())

#3)0-1사이 난수 실수
r=random.random()
print('r=', r)

#난수 0.01 미만이면 종료 후 난수 개수 출력
cnt=0
while True:
    r=random.random()
    print(random.random())
    if r<0.01:
        break
    else:
        cnt+=1
print('난수 개수=', cnt)

#1)random 모듈 관련 함수 도움말
help(random.randint)
help(random.choices)

#2)이름 list에 전체 이름, 특정 이름 출력
names=['홍길동', '이순신', '유관순']
print(names)
print(names[2])
#3)list에서 자료 유무 확인하기
if '유관순' in names:
    print('유관순 있음')
else:
    print('유관순 없음')

#4)난수 정수로 이름 선책하기
idx=random.randint(0,2)
print(names[idx])

#3.3.3 break, continue

i=0
while i<10:
    i+=1
    if i==3:
        continue
    if i==6:
        break
    print(i, end=' ')

#3.3.4 for
#1)문자열 열거형객체 이용
string="홍길동"
print(len(string))
for s in string:
    print(s)

#2)list 열거형객체 이용
lstset=[1,2,3,4,5] #5개원소를 갖는 열거형 객체
for e in lstset:
    print('원소: ', e)


#3.3.5 for & range
help(range)

#1)range 객체 생성
num1=range(10) #range(start)
print('num1: ',num1)
num2=range(1,10)
print('num2: ', num2)
num3=range(1,10,2)
print('num3', num3)

#2)range 객체 활용
for n in num1:
    print(n, end=' ')
print()
for n in num2:
    print(n, end='')
print()
for n in num3:
    print(n, end=' ')

#3.3.6 for&list
#1)list에 자료 저장하기
lst=[]
for i in range(10):
    r=random.randint(1,10)
    lst.append(r)
print('lst=',lst)

#2)list에 자료 참조하기
for i in range(10):
    print(lst[i]*0.25)
