# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:00:59 2016

@author: AnaVicki
"""

def digit_sum(n):
    total = 0
    a = 1
    while (a == 1):
        total = 0
    while n > 0:
        last_digit = n % 10
        if n / 10 == 0:
            print (str(last_digit), end ='')
        else:
            print (str(last_digit) + '+' , end='')
        total = total + last_digit
        n = n // 10
        if (total /10 == 0):
            a = 0
        else:
            n = total
            print ("")
    return total

n = int(input("please enter a positive integer:"))
print(digit_sum(n))
