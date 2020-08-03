# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:02:00 2020

@author: AE401
"""
weight = int(input("請輸入體重(公斤):\n"))
t = int(input("請輸入身高(公分):\n"))
t=t/100
bmi = weight//t**2
if bmi<18.5:
    print("體重不足")
elif bmi<24:
    print("正常")
elif bmi<27:
    print("過重")
elif bmi<30:
    print("輕度肥胖")
elif bmi<35:
    print("中度肥胖")
else:
    print("過度肥胖")   

            
