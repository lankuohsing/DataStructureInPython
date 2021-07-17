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
    quo_code=""
    for i in range(quotient):
        quo_code=quo_code+"1"
    if(remainder<div):
        b=c-1
        a="{0:0"+str(b)+"b}"
        bi=a.format(remainder)
    else:
        b=c
        a="{0:0"+str(b)+"b}"
        bi=a.format(remainder+div)
    remain_code=str(bi)
    golomb_result=quo_code+"0"+remain_code
    code_len=len(remain_code)
    return golomb_result,code_len
def golomb_encode_list(ori_list,m):
    result_list=[]
    sign_list=[]
    len_list=[]
    for i in range(0,len(ori_list)):
        if ori_list[i]<0:
            sign_list.append(1)
            result,code_len=golomb_encode(abs(ori_list[i]),m)
        else:
            sign_list.append(0)
            result,code_len=golomb_encode(ori_list[i],m)
        result_list.append(result)
        len_list.append(code_len)
    return sign_list,result_list,len_list
def golomb_decode(golocode,m):
    q=0
    for c in golocode:
        if c=='0':
            break
        else:
            q+=1
    r=int(golocode[q+1:],2)
    return q*m+r
def golomb_decode_str(encoded_str,m,sign_list,len_list):
    ori_list=[]
    start=0
    for i in range(0,len(len_list)):
        zero_index=0
        for j in range(start,len(encoded_str)):
            if(encoded_str[j]=="0"):
                break;
            else:
                zero_index+=1
        start=start+zero_index+1
        end=start+len_list[i]
        ori_value=zero_index*m+int(encoded_str[start:end],2)
        start=end
        if sign_list[i]==1:
            ori_value*=-1
        ori_list.append(ori_value)
    return ori_list
if __name__=="__main__":
    m=16
    v=18
    golomb_encode_result=golomb_encode(v,m)
#    print("golomb encoding result for ",v," with parameter m equals ",m," is ", golomb_encode_result)
#    print("original value: ",golomb_decode(golomb_encode_result,m))

    ori_list=[-120,-16,-5,-3,-2,-1,-1,0,0,0,1,1,2,3,5,16,120]
    sign_list,result_list,len_list=golomb_encode_list(ori_list,m)
    encoded_str=""
    for s in result_list:
        encoded_str+=s
    decoded_list=golomb_decode_str(encoded_str,m,sign_list,len_list)
    print("golomb encoding result parameter m equals ",m," is ", result_list)
    print("original value: ",decoded_list)