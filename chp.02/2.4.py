### 뮨자열

#문자열 유형
oneLine="this is one line string"
print(oneLine)

multiLine="""this is 
multi line
string"""
print(multiLine)

multiLine2="this is \nmulti line\nstring"
print(multiLine2)

#2.4.1 문자열 특징
#1) 문자열 색인
string="PYTHON"
print(string[0])
print(string[5])
print(string[-1])
print(string[-6])

#2) 문자열 연산
print("python"+"program") #결합연산자
#print("python-"+3.7+".exe") #error
print("python-" +str(3.7)+".exe")

print("-"*30)
