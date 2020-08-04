import random
A=random.randint(1,20)
I=0
while I<5:
    B=input('請輸入1-20中的一個數字') 
    B=int(B)
    I=I+1
    if A<B:
        print('太大 只能猜五次喔')
    if A==B:
        print("猜對了")
        print('你玩了',I,'次')
        break
    if A>B:
        print('太小 只能猜五次喔')  
    elif B<1 or B>20:
        print('打錯了')
    if I==5:
         break