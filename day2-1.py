# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:53:35 2020

@author: AE401
"""
import random
a = random.randint(1,10)
b = input("請於1到10中猜一個數字")
b = int(b)
if b>10 or b<1:
    print("打錯了")
elif a == b:
    print("猜中了")
else:
    print("猜錯了")

    

