#!/bin/env python

Operate=['+','-','-','+','-','-','+','+','+','-','+','+','+','+','-','-','+','+','+','-','+','-','-','+','-','+','-','-']
Table1=[0x9,0x2,0x7,0xF,0x7,0x7,0x9,0x4,0xE,0x8,0x13,0x6,0x1,0x1,0x3,0x1,0x9,0x0,0x9,0x9,0x9,0x2,0x1,0xA,0x5,0x6,0,0]
Table2=[0x39,0x61,0x6D,0x75,0x74,0x66,0x39,0x5A,0x6D,0x41,0x48,0x65,0x75,0x56,0x75,0x30,0x57,0x39,0x68,0x5A,0x39,0x4E,0x30,0x4F,0x6F,0x39,0x21,0x7D]
flag=[]

for i,j,o in zip(Table1,Table2,Operate):
    c=j-i if o=='+' else j+i
    flag.append(chr(c))

print len(Operate)
print len(Table1)
print len(Table2)

print ''.join(flag)


