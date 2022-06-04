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

#2.4.2 슬라이싱
#문자열[시작색인:끝색인:증감값]
#1)왼쪽기준
print(oneLine)
print("문자열 길이: ", len(oneLine))
print(oneLine[0:4])
print(oneLine[:4])
print(oneLine[:])
print((oneLine[::2]))

#2)오른쪽 기준
print(oneLine[0:-1:2])
print(oneLine[-6:-1])
print(oneLine[-6:])

#3)부분 문자열 생성
subString=oneLine[-11: ]
print(subString)

##2.4.3 문자열 처리 함수
#1) 특정 글자수 반환
oneLine="this is one line string"
print('t 글자 수 : ', oneLine.count('t'))

#2) 접두어 문자 비교 판단
print(oneLine.startswith('this'))
print(oneLine.startswith('that'))

#3) 문자열 교체
print(oneLine.replace('this', 'that'))

#4) 문자열 분리(split): 문단>>문장
multiLine="""this is
multi line
string"""
sent=multiLine.split('\n')
print('문장: ', sent)

#5) 문자열 분리2: 문장>>단어
words=oneLine.split(' ')
print('단어: ', words)

#6) 문자열 결합: join
sent2=','.join(words)
print(sent2)

#2.4.4 이스케이프 문자

#1) escape 문자 적용
print('escape 문자 차단')
print('\n 출력 이스케이프 문자')

#2)escape 문자 기능 차단
print('\\n출력 이스케이프 기능 차단1')
print(r'\n출력 이스케이프 기능 차단2')

#3) 경로 표현: C:\Python\test
print('path=', 'C:\Python\test')
print('path=', 'C:\\Python\\test')
print('path=', r'C:\Python\test')


