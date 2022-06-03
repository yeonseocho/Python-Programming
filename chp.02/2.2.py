#2.2.1 산술연산자

num1=100 #피연산자1
num2=20 #피연산자2

add=num1+num2
print('add=', add) #덧셉
sub=num1-num2
print('sub=', sub) #뺄셈
mul=num1*num2
print('mul=', mul) #곱셈
div=num1/num2
print('div=', div) #나눗셈
div2=num1%num2
print('div2=', div2) #나머지 연산
square=num1**2
print(square) #제곱 계산

#2.2.2 관계연산자

#1) 동등비교
bool_result=num1==num2
print(bool_result)

bool_result=num1 !=num2
print(bool_result)

#2) 크기비교
bool_result=num1>num2
print(bool_result)

bool_result=num1>=num2
print(bool_result)

bool_result=num1<num2
print(bool_result)

bool_result=num1<=num2
print(bool_result)

#2.2.3 논리 연산자

#두 관계식이 같은지 판단
log_result=num1>=50 and num2<=10
print(log_result)

#도 관계식 중 하나라도 같은지 판단
log_result=num1>=50 or num2<=10
print(log_result)

log_result=num1>=50
print(log_result)

log_result=not(num1>=50)
print(log_result)

#2.2.4 대입 연산자
#1)변수에 값 할당
i=tot=10 #i=10; tot=10
i+=1 #i=i+1
tot += i #tot=tot+i
print(i, tot)

#같은 줄에 중복 출력
print('출력1', end=',') # end=구분자
print('출력2')

v1, v2=100, 200
#2)변수 교체
v2, v1=v1, v2
print(v1,v2)

#3) 패킹(packing)할당
lst=[1,2,3,4,5]
v1, *v2=lst
print(v1, v2)

*v1, v2=lst
print(v1, v2)

