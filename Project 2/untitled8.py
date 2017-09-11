# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 16:07:47 2016

@author: AnaVicki
"""

def digit_sum(n):
    total = 0
    flg=1
    while(flg==1):
        total=0
        while n > 0:
            last_digit = n % 10
            if n/10 ==0:
              print (str(last_digit), end='')
            else:
              print (str(last_digit) + "+", end='')
            total = total + last_digit
            n = n / 10
        if (total/10==0):
            flg=0
        else:
            n=total
        print ("")
    return total        

print (digit_sum(1236))