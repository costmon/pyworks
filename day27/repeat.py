# 파일쓰기
f = open("c:/pyfile/repeat.txt", 'w')

for i in range(1, 11):
    f.write("%d번빼 줄입니다. \n" % i)
f.close()

# 파일 읽기
f = open("c:/pyfile/repeat.txt", 'r')
data = f.read()   #읽은 내용을 변수에 저장
print(data)
f.close()