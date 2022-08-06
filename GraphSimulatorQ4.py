import sys
code = sys.stdin.read().splitlines()
# with open('test01') as f:
#     code = f.read().splitlines()
op_map = {
    "00000": "addf",
    "00001": "subf",
    "00010": "movf",
    "10001": "sub",
    "10000": "add",
    "10010": "mov",
    "10011": "mov",
    "10100": "ld",
    "10101": "st",
    "10110": "mul",
    "10111": "div",
    "11000": "rs",
    "11001": "ls",
    "11010": "xor",
    "11011": "or",
    "11100": "and",
    "11101": "not",
    "11110": "cmp",
    "11111": "jmp",
    "01100": "jlt",
    "01101": "jgt",
    "01111": "je",
    "01010": "hlt"
}
reg_map = {"R0": "000", "R1": "001", "R2": "010", "R3": "011",
                    "R4": "100", "R5": "101", "R6": "110", "FLAGS": "111"}
flags = [0, 0, 0, 0]
reg_vals = [0, 0, 0, 0, 0, 0, 0]
def converter_16_bits(register):
    a=dec_binary(int(register))
    b=(16-len(a))*"0" + a
    return b

def converter_8_bits(register):
    a=dec_binary(int(register))
    b=(8-len(a))*"0" + a
    return b

def dec_binary(num): 
    base_num = ""
    while num>0:
        dig = int(num%2)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10) 
        num //= 2
    base_num = base_num[::-1]
    return base_num

def binary_dec(num):
    figures = [int(i,2) for i in str(num)]
    figures = figures[::-1]
    result = 0

    for i in range(len(figures)):
        result += figures[i]*2**i
    return result

def floating(num):
    overflow=False
    if num>253.0:
        overflow=True
        flags[0]=1
    n=dec_binary(int(num))
    num=str(num)
    ind=num.index('.')
    s='0'+num[ind:]
    s=float(s)
    n=str(n)+'.'
    if(len(num)>8):
        flags[0]=1
        overflow=True
    if(not overflow):
        l=len(num)
        i=0
        while(s>0):
            mul=s*2
            n=n+str(mul)[0]
            if(str(mul)[0]=='0'):
                s=mul
            else:
                s=mul-1
            i+=1
            if(i>(8-l)):
                flags[0]=1
        exp=dec_binary(n.index('.')-1)
        if(binary_dec(exp)>7):
            flags[0]=1
            overflow=True
        if(not overflow):
            exp='0'*(3-len(exp))+exp
            n=n+'0'*(5-len(n)+n.index('.')+1)
            n=n[:n.index('.')]+n[n.index('.')+1:]
            mts=n[1:6]
            le=len(mts)
            mts=mts+'0'*(5-le)
            n=exp+mts
    if(not overflow):
        return n
    else:
        return '11111111'
    
def floating_dec(num):
    exp=binary_dec(num[0:3])
    mant=num[3:]
    dec=binary_dec('1'+mant[0:exp])
    ad=0
    k=-1
    for i in range(5-exp):
        ad+=int(mant[exp])*(2**k)
        k-=1
        exp+=1
    res=dec+ad
    return res
    
def overflow(sum,ind):
    if(sum<0):
        flags[0]=1
        reg_vals[ind]=0
    elif(sum>65535):
        flags[0]=1
        bi=dec_binary(sum)
        reg_vals[ind]=binary_dec(bi[0:16])

def type_a(op,i):
    instruction=op_map[op]
    if(instruction=="add"):
        o1=binary_dec(i[7:10])
        o2=binary_dec(i[10:13])
        ind=binary_dec(i[13:])
        reg_vals[ind]=reg_vals[o1]+reg_vals[o2]
        overflow(reg_vals[ind],ind)

    if(instruction=="addf"):
        o1=binary_dec(i[7:10])
        o2=binary_dec(i[10:13])
        ind=binary_dec(i[13:])
        reg_vals[ind]=float((reg_vals[o1]+reg_vals[o2]))
        a=floating((reg_vals[ind]))
        if flags[0]==1:
            reg_vals[ind]=255

    if(instruction=="subf"):
        o1=binary_dec(i[7:10])
        o2=binary_dec(i[10:13])
        ind=binary_dec(i[13:])
        if reg_vals[o1]>=reg_vals[o2]:
            reg_vals[ind]=float(reg_vals[o1]-reg_vals[o2])
            if(reg_vals[ind]<1):
                reg_vals[ind]=0
                flags[0]=1
        else:
            reg_vals[ind]=0
            flags[0]=1

    if(instruction=="sub"):
        o1=binary_dec(i[7:10])
        o2=binary_dec(i[10:13])
        ind=binary_dec(i[13:])
        if reg_vals[o1]>=reg_vals[o2]:
            reg_vals[ind]=reg_vals[o1]-reg_vals[o2]
            overflow(reg_vals[ind],ind)
        else:
            reg_vals[ind]=0
            flags[0]=1

    if(instruction=="mul"):
        o1=binary_dec(i[7:10])
        o2=binary_dec(i[10:13])
        ind=binary_dec(i[13:])
        reg_vals[ind]=reg_vals[o1]*reg_vals[o2]
        overflow(reg_vals[ind],ind)

    if(instruction=="xor"):
        o1=binary_dec(i[7:10])
        o2=binary_dec(i[10:13])
        ind=binary_dec(i[13:])
        reg_vals[ind]=reg_vals[o1]^reg_vals[o2]
        overflow(reg_vals[ind],ind)

    if(instruction=="and"):
        o1=binary_dec(i[7:10])
        o2=binary_dec(i[10:13])
        ind=binary_dec(i[13:])
        reg_vals[ind]=reg_vals[o1]&reg_vals[o2]
        overflow(reg_vals[ind],ind)

    if(instruction=="or"):
        o1=binary_dec(i[7:10])
        o2=binary_dec(i[10:13])
        ind=binary_dec(i[13:])
        reg_vals[ind]=reg_vals[o1]|reg_vals[o2]
        overflow(reg_vals[ind],ind)
  
def type_b(op,i):
    instruction=op_map[op]
    if(instruction=="mov"):
        ind=binary_dec(i[8:])
        o1=binary_dec(i[5:8])
        reg_vals[o1]=ind

    instruction=op_map[op]
    if(instruction=="movf"):
        ind=(i[8:])
        o1=binary_dec(i[5:8])
        reg_vals[o1]=floating_dec(ind)

    if(instruction=="rs"):
        ind=binary_dec(i[8:])
        o1=binary_dec(i[5:8])
        reg_vals[o1]=reg_vals[o1]//(2**ind)

    if(instruction=="ls"):
        ind=binary_dec(i[8:])
        o1=binary_dec(i[5:8])
        reg_vals[o1]=reg_vals[o1]*(2**ind)

def type_c(op,i):
    instruction=op_map[op]
    if(instruction=="mov"):
        o1=binary_dec(i[10:13])
        o2=binary_dec(i[13:])
        if o1>6:
            fval='0'*12
            for j in flags:
                fval+=str(j)
                # print(fval)
            reg_vals[o2]=binary_dec(fval)
        else:
            reg_vals[o2]=reg_vals[o1]

    if(instruction=="div"):
        o1=binary_dec(i[10:13])
        o2=binary_dec(i[13:])
        reg_vals[0]=reg_vals[o1]//reg_vals[o2]
        reg_vals[1]=reg_vals[o1]%reg_vals[o2]

    if(instruction=="cmp"):
        o1=binary_dec(i[10:13])
        o2=binary_dec(i[13:])
        if(reg_vals[o1]<reg_vals[o2]):
            flags[1]=1
        elif(reg_vals[o1]>reg_vals[o2]):
            flags[2]=1
        else:
            flags[3]=1

    if(instruction=="not"):
        o1=binary_dec(i[10:13])
        o2=binary_dec(i[13:])
        reg_vals[o2]=reg_vals[o1]^((2**16)-1)
        
def type_d(op,i):
    instruction=op_map[op]
    if(instruction=="ld"):
        o1=binary_dec(i[5:8])
        o2=binary_dec(i[8:])
        value=int(memadd[o2],2)
        reg_vals[o1]=value

    if(instruction=="st"):
        o1=binary_dec(i[5:8])
        o2=binary_dec(i[8:])
        reg=reg_vals[o1]
        memadd[o2]=converter_16_bits(reg)

def type_e(op,i):
    global pc
    instruction=op_map[op]
    if(instruction=="jmp"):
        o2=binary_dec(i[8:])
        pc=o2
    if(instruction=="jlt"):
        o2=binary_dec(i[8:])
        if flags[1]==1:
            pc=o2
        else:
            pc+=1
    if(instruction=="jgt"):
        o2=binary_dec(i[8:])
        if flags[2]==1:
            pc=o2
        else:
            pc+=1
    if(instruction=="je"):
        o2=binary_dec(i[8:])
        if flags[3]==1:
            pc=o2
        else:
            pc+=1
     
def printregval(pc):
    pcstr=converter_8_bits(pc)
    print(pcstr,end=' ')
    for i in reg_vals:
        if(isinstance(i,int)):
            print(converter_16_bits(i),end=' ')
        else:
            s='0'*8+floating(i)
            print(s,end=" ")
    fval='0'*12
    for i in flags:
        fval+=str(i)
    print(fval)

def freset(flags):
    for i in range(4):
        flags[i]=0 


memadd=['0'*16]*256
i=0
for l in code:
    if l!="":
        memadd[i]=l
        i+=1

pc=0
pcval=[]
halt=False

cc=0
cycles=[]
x=[]
y=[]
m=[]

while(not halt):
    i=code[pc]
    if i!="":
        op = i[0:5]
        ins = op_map[op]
        prc=pc
        if(ins == 'add' or ins == 'sub' or ins == 'mul' or ins == 'and' or ins == 'xor' or ins=="or"):
            freset(flags)
            type_a(op,i)
        elif((ins == 'mov' and op=='10010') or ins == 'rs' or ins == 'ls'):
            freset(flags)
            type_b(op,i)
        elif(ins == 'mov' or ins == 'div' or ins == 'cmp' or ins == 'not'):
            if(op!='10011'):
                freset(flags)
            # print("aads")
            type_c(op,i)
            if(op=='10011'):
                freset(flags)
        elif(ins =='addf' or ins =='subf'):
            freset(flags)
            type_a(op,i)
        elif(ins =='movf'):
            freset(flags)
            type_b(op,i)
        elif(ins == 'ld' or ins == 'st' or ins == 'mul'):
            freset(flags)
            type_d(op,i)
        elif(ins == 'jmp' or ins == 'jlt' or ins == 'jgt' or ins == 'je'):
            if(ins=='jmp'):
                freset(flags)
            else:
                pass
            type_e(op,i)
            freset(flags)
        elif(ins=='hlt'):
            freset(flags)
            halt=True
        cycles.append(cc)
        cc+=1
        m.append(prc)
        printregval(prc)
        if ins not in ['jmp','jgt','jlt','je']:
            pc+=1

for i in memadd:
    print(i)

import matplotlib.pyplot as plt
import numpy as np
cycles=cycles+x
m=m+y
plt.scatter(np.array(cycles),np.array(m),edgecolor='black',color='yellow',marker="^")
plt.xlabel("CYCLES")
plt.ylabel("MEMORY")
plt.show()
