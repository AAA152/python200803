# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:29:08 2020

@author: AE401
"""
number = input("請輸入分數")
number = int(number)
if number>=0 and number<=100:
    print("分數")
    if number>=90:
        print("A")
    elif number>=80:
        print("B")
    elif number>=70:
        print("C")
    elif number>=60:
        print("D")
    else:
        print("E")
else:
    print("錯誤")
             
    