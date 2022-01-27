#입장객 수에 따른 줄수 계산
customer = int(input("입장객 수 : "))
col = int(input("열의 수 : "))

if customer % col == 0:
    #row = int(customer / col)
    row = customer // col
else:
    row = int(customer / col) + 1

