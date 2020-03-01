# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 10:48:34 2020

@author: Catalin
"""

import numpy
import csv

def read_input_from_file(pick):
    array=[]
    key_dict={}
    with open("C:\\Users\\Catalin\\Desktop\\Faculty\\AI\\cryptarithmetic"+str(pick)+".txt") as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=',')
        ok=False
        for row in csv_reader:
            #print(row)
            for letter in row[0]:
                if letter not in key_dict.keys():
                    key_dict[letter]=numpy.random.randint(0,16)
            array.append(row[0])
            if ok==False:
                array.append(row[1])
                if row[1]=="=":
                    ok=True
    return (array,key_dict)
def do_op(first_op,second_op,operand):
    if operand=="+":
        return first_op+second_op
    elif operand=="-":
        return first_op-second_op
    elif operand=="/":
        return first_op/second_op
    elif operand=="*":
        return first_op*second_op
    else:
        #print("value:")
        return first_op==second_op
def solve_system(pick):
    arith_tuple=read_input_from_file(pick)
    operations=arith_tuple[0]
    letter_dict=arith_tuple[1]
    i=0
    value=0
    keep=""
    prod=1
    op="+"
    for index in operations:
        if i%2==0:
            j=0
            prod=0
            for letter in index:
                if j==0:
                    if letter_dict[letter]==0:
                        return False
                prod=prod*16+letter_dict[letter]
                #print(prod)
                j+=1
            #print(i)
        else:
            
            #print(value)
            value=do_op(value,prod,op)
            op=index
            keep+=str(value)+op
            
        i+=1
    keep+=str(prod)
    value=do_op(value,prod,op)
    #print("Ending...")
    if value==True:
        print(keep)
    return value
numpy.random.seed()
print("Which problem 1 to 5")
pick=int(input())
ok=False
trials=1
while ok==False and trials<1000000:
    ok=solve_system(pick)
    #print(ok)
    trials+=1
if ok==False:
    print("No solution in 1000000 trials")
