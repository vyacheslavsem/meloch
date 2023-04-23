# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 10:47:38 2022

@author: VELES
"""

num=int(input("Enter number:"))
factorial_num = 1

for i in range(1,num+1):
    factorial_num *= i 
    
print("Факториал", num,"! =", factorial_num)