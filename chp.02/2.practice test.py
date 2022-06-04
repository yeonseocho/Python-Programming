# 1
su = 5
dan = 800
price = su * dan
print('su 주소: ', id(su))
print('dan 주소: ', id(dan))
print(price)

# 2
y = 2.5 * 2 ** 2 + 3.3 * 2 + 6
print(y)

# 3
g = int(input('지방의 그램을 입력하세요:'))
t = int(input('탄수화물의 그램을 입력하세요'))
d= int(input('단백질의 그램을 입력하세요'))

total = g * 9 + d * 4 + t * 4
print(total,'cal')

#4)
word1=input('첫번째 단어')
word2=input('두번째 단어')
word3=input('세번째 단어')
addr=word1[0]+word2[0]+word3[0]
print('약자', addr)
