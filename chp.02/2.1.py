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



