from math import log2

def minbits(length,a):
    return len(bin(int(length/a)))-2
print("It is a command line program to solve questions related to memory organization")
print("1.Type 1: ISA and instruction related")
print("2.Type 2: System enhancement")
a=int(input("Enter which type you want to choose (1 or 2): "))
if(a==1):
    b=input("Enter the space in memory (for eg:- 16mb or 16MB) : ")
    print("1. Bit Addressable Memory")
    print("2. Nibble Addressable Memory")
    print("3. Byte Addressable Memory")
    print("4. Word Addressable Memory")
    c=int(input("Enter How the memory is addressed(1/2/3/4): "))
    le=len(b)
    if(b[-2]=="M" or b[-2]=="m"):
        if(b[-1]=="B"):
            lengthinbits=int(b[0:le-2])*(2**23)
        else:
            lengthinbits=int(b[0:le-2])*(2**20)
    elif(b[-2]=="G" or b[-2]=="g"):
        if(b[-1]=="B"):
            lengthinbits=int(b[0:le-2])*(2**33)
        else:
            lengthinbits=int(b[0:le-2])*(2**30)
    elif(b[-2]=='K' or b[-2]=='k'):
        if(b[-1]=="B"):
            lengthinbits=int(b[0:le-2])*(2**13)
        else:
            lengthinbits=int(b[0:le-2])*(2**10)
    elif(b[-1]=='B'):
        lengthinbits=int(b[0:le-1])*(2**3)
    else:
        print("Error - Invalid Memory unit ")

    l_instruction=int(input("length of one instruction in bits: "))
    l_register=int(input("length of register in bits: "))

    if(c==1):
        leng=minbits(lengthinbits,1)
        print("minimum bits are needed to represent an address: ",leng-1)
        length_opcode=l_instruction-l_register-leng
        print("Number of bits needed by opcode: ",length_opcode)
        print("Number of filler bits in Instruction type 2: ",l_instruction-length_opcode-(2*l_register))
        print("Maximum numbers of instructions this ISA can support: ",(2**length_opcode)-1)
        print("maximum number of registers this ISA can support: ",(2**l_register)-1)

    elif(c==2):
        leng=minbits(lengthinbits,4)
        print("minimum bits are needed to represent an address: ",leng-1)
        length_opcode=l_instruction-l_register-leng
        print("Number of bits needed by opcode: ",length_opcode)
        print("Number of filler bits in Instruction type 2: ",l_instruction-length_opcode-(2*l_register))
        print("Maximum numbers of instructions this ISA can support: ",(2**length_opcode)-1)
        print("maximum number of registers this ISA can support: ",(2**l_register)-1)        
    elif(c==3):
        leng=minbits(lengthinbits,8)
        print("minimum bits are needed to represent an address: ",leng-1)
        length_opcode=l_instruction-l_register-leng
        print("Number of bits needed by opcode: ",length_opcode)
        print("Number of filler bits in Instruction type 2: ",l_instruction-length_opcode-(2*l_register))
        print("Maximum numbers of instructions this ISA can support: ",(2**length_opcode)-1)
        print("maximum number of registers this ISA can support: ",(2**l_register)-1)
    elif(c==4):
        cpu_bits=int(input("how many bits the cpu is: "))
        leng=minbits(lengthinbits,cpu_bits)
        print("minimum bits are needed to represent an address: ",leng-1)
        length_opcode=l_instruction-l_register-leng
        print("Number of bits needed by opcode: ",length_opcode)
        print("Number of filler bits in Instruction type 2: ",l_instruction-length_opcode-(2*l_register))
        print("Maximum numbers of instructions this ISA can support: ",(2**length_opcode)-1)
        print("maximum number of registers this ISA can support: ",(2**l_register)-1)
    else:
        print("wrong type chosen")

elif(a==2):
    print("1.Type 1")
    print("2.Type 2")
    type=int(input("Enter the choice type: "))
    if(type==1):
        b=input("Enter the space in memory (for eg:- 16mb or 16MB) : ")
        print("1. Bit Addressable Memory")
        print("2. Nibble Addressable Memory")
        print("3. Byte Addressable Memory")
        print("4. Word Addressable Memory")
        c=int(input("Enter How the memory is addressed(1/2/3/4): "))
        le=len(b)
        if(b[-2]=="M" or b[-2]=="m"):
            if(b[-1]=="B"):
                lengthinbits=int(b[0:le-2])*(2**23)
            else:
                lengthinbits=int(b[0:le-2])*(2**20)
        elif(b[-2]=="G" or b[-2]=="g"):
            if(b[-1]=="B"):
                lengthinbits=int(b[0:le-2])*(2**33)
            else:
                lengthinbits=int(b[0:le-2])*(2**30)
        elif(b[-2]=='K' or b[-2]=='k'):
            if(b[-1]=="B"):
                lengthinbits=int(b[0:le-2])*(2**13)
            else:
                lengthinbits=int(b[0:le-2])*(2**10)
        elif(b[-1]=='B'):
            lengthinbits=int(b[0:le-1])*(2**3)
        else:
            print("Error - Invalid Memory unit ")

        cpu_bits=int(input("how many bits the cpu is: "))
        print("1. Bit Addressable Memory")
        print("2. Nibble Addressable Memory")
        print("3. Byte Addressable Memory")
        print("4. Word Addressable Memory")
        convert=int(input("Enter the choice to which you have to change: "))
        if(c==1):
            length_b=minbits(lengthinbits,1)
        elif(c==2):
            length_b=minbits(lengthinbits,4)
        elif(c==3):
            length_b=minbits(lengthinbits,8)
        else:
            length_b=minbits(lengthinbits,cpu_bits)
        if(convert==1):
            print((minbits(lengthinbits,1))-length_b)
        elif(convert==2):
            print((minbits(lengthinbits,4))-length_b)
        elif(convert==3):
            print((minbits(lengthinbits,8))-length_b)
        elif(convert==4):
            print((minbits(lengthinbits,cpu_bits))-length_b)
    elif(type==2):
        cpu_bits=int(input("how many bits the cpu is: "))
        address_pin=int(input("how many address pin it has: "))
        print("1. Bit Addressable Memory")
        print("2. Nibble Addressable Memory")
        print("3. Byte Addressable Memory")
        print("4. Word Addressable Memory")
        convert=int(input("Enter the choice what type of addressable memory it has: "))
        if(convert==1):
            reallength=address_pin-3
        elif(convert==2):
            reallength=address_pin-1
        elif(convert==3):
            reallength=address_pin
        elif(convert==4):
            reallength=address_pin+log2(cpu_bits//8)
        else:
            print("Wrong type chosen")
        if(reallength>=30):
            print(f'{2**reallength/(2**30)}GB')
        elif((20)<=reallength<(30)):
            print(f'{2**reallength/(2**20)}MB')
        elif((10)<=reallength<(20)):
            print(f'{2**reallength/(2**20)}KB')
        else:
            print(f'{2**reallength/8}B')
    else:
        print("Wrong type chosen")
else:
    print("Wrong type chosen")
