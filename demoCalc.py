# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 22:41:28 2019

@author: sudhanshu kumar sinh
"""

def Operations(a,b,opCode):
    switch={1:a+b,2:a-b,3:a*b,4:a/b}
    return switch.get(opCode)

while True:
    print("1 for Addition")
    print("2 for Substraction")
    print("3 for Multiplication")
    print("4 for Division")
    print("5 for Exit")
    print("-----------------------")
    print("Choose Operation: ")
    lis=[1,2,3,4,5]
    op=int(input())
    if op in lis:
        if op==5:
            break
        else:
            print("Enter 1st Input:")
            a=int(input())
            print("Enter 2nd Input:")
            b=int(input())
            print("-----------------------")
            print("Ans is: ",Operations(a,b,op))
            print("-----------------------")
    else:
        print("-----------------------")
        print("Choose right Operation!!!!!!!")
        print("-----------------------")


