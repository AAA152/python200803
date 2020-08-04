import random
A=random.randint(1,20)
while True:
    B=input('請輸入1-20中的一個數字') 
    B=int(B)
    if A==B:
        print('猜中了')
        break
    elif B<1 or B>20:
        print('打錯了')
    elif A>B:
        print('太小了')
    elif B>A:
        print('太大了')
    else:
        print('猜錯了')