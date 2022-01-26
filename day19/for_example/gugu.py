#구구단 출력
#print("단 입력 : ")
dan = int(input("단 입력 : "))
for i in range(1, 10):
    #print(dan, * "x", i, "=", (dan * i))
    print("{0} x {1} = {2}".format(dan, i, dan * i))
