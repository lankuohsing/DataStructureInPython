# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 21:50:29 2021

@author: lankuohsing
"""

import math

def golomb_encode(x,m):
    c=int(math.ceil(math.log(m,2)))
    remainder=x%m
    quotient=int(math.floor(x/m))
    div=int(math.pow(2,c)-m)
    first=""
    for i in range(quotient):
        first=first+"1"
    if(remainder<div):
        b=c-1
        a="{0:0"+str(b)+"b}"
        bi=a.format(remainder)
    else:
        b=c
        a="{0:0"+str(b)+"b}"
        bi=a.format(remainder+div)
    final=first+"0"+str(bi)
    return final
if __name__=="__main__":
    m=16
    v=18
    golomb_encode_result=golomb_encode(v,m)
    print("golomb encoding result for ",v," with parameter m equals ",m," is ", golomb_encode_result)