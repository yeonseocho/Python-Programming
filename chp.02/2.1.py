###변수의 자료형

var1='Hello python'
print(var1)
print(id(var1))

var1=100
print(var1)
print(id(var1))

var2=150.25
print(var2)
print(id(var2))

var3=True
print(var3)
print(id(var3))

###식별자 작성규칙

##예약어 확인
import keyword #모듈 임포트
python_keyword=keyword.kwlist
print(python_keyword)
print(type(python_keyword))
print(len(python_keyword))

#2.1.2. 자료형
var1="Hello Python"
print(var1)
print(type(var1))

var1=100
print(var1)
print(type(var1))

var2=150.25
print(type(var2))

var3=True
print(type(var3))

#(2)자료형 변환

#실수-->정수
a=int(10.5)
b=int(20.42)
add=a+b
print('add=', add)

#정수-->실수
a=float(10)
b=float(20)
add2=a+b
print('add2=',add2)

#논리형-->정수
print(int(True))
print(int(False))

#문자형-->정수
st='10'
print(int(st)**2)