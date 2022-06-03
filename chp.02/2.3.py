##2.3 표준입출력장치

#input(prompt)

#1)문자형 숫자 입력
num=input('숫자입력: ')
print('num type: ', type(num))
print('num=',num)
print('num=',num*2)

#2)문자형 숫자를 정수형으로 변환
num1=int(input("숫자입력: "))
print('num1=', num1*2)

#3)문자형 숫자를 실수형으로 변환
num2=float(input("숫자입력: "))
result=num1+num2
print('result=',result)

#2.3.2 표준출력장치
help(print)

#1)value 인수
print("value=", 10+20+30+40+50)

#2)sep 인수: 값과 값을 특수문자로 구분
print("010", "1234", "5678", sep="-")

#3)end 인수
print("value=", 10, end=",")
print("value=", 20)

#2.3.3 format과 양식문자

