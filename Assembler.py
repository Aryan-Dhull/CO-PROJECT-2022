import sys                                    
lines = sys.stdin.read().splitlines()

# with open ('input.txt',"r") as f:
# 	lines=f.read().splitlines()

regaddress = {"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101", "R6":"110","FLAGS":"111"}

symbol=["add","sub","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt"]

reg = [ "R0", "R1" , "R2" , "R3" , "R4" , "R5" , "R6"]

reg_flag= [ "R0", "R1" , "R2" , "R3" , "R4" , "R5" , "R6" , "FLAGS"]

label=["hlt"]
labels=[]
nested_label=[]
labels_add=[]
var=[]

check=[]

error=False

def type_a(line):
    words=line.split()
    global error
    if(len(words))!=4:
        error=True
        print("Error in line number",line_no,"Invalid Syntax")
    if(not error):
        for i in range(1,len(words)):
            if words[i] not in reg:
                error=True
                print("Error in line number",line_no,"Invalid Register")
                break
		
def type_b(line):
    words=line.split()
    global error
    if(len(words))!=3:
        error=True
        print("Error in line number",line_no, "Invalid Syntax")
    if(not error):
        if words[1] not in reg:
            error=True
            print("Error in line number",line_no,"Invalid Register")
        if not (words[2][1:]).isdigit():
            error=True
            print("Error in line number ",line_no,"Inavlid immediate")
        if '$' not in words[2]:
            error=True
            print("Error in line number",line_no, "Invalid Syntax")
    if(not error):
        if int(words[2][1:])>255 or int(words[2][1:])<0:
            error=True
            print("Error in line number ",line_no,"Inavlid immediate")
		
def type_c(line):
    words=line.split()
    global error
    if(len(words))!=3:
        error=True
        print("Error in line number",line_no, "Invalid Syntax")
    if(not error):
        for i in range(1,len(words)):
            if words[i] not in reg:
                error=True
                print("Error in line number",line_no,"Invalid Register")
                break
		
def type_d(line):
    words=line.split()
    global error
    if(len(words)!=3):
        error=True
        print("Error in line number",line_no, "Invalid Syntax")
    if(not error):
        for i in range(1,len(words)-1):
            if words[i] not in reg:
                error=True
                print("Error in line number",line_no,"Invalid Register")
                break
    if(not error):
        if(words[2] not in var):
            print("Error in line number",line_no, "Undefined Variable")
            error=True
    if(not error):
        if(words[2] in labels):
            print("Error in line number",line_no, "Cannot use label in place of variable")
            error=True
		
def type_e(line):
    words=line.split()
    global error
    if(len(words)!=2):
        error=True
        print("Error in line number",line_no, "Invalid Syntax")
    if(not error):
        if(words[1] in var):
            print("Error in line number",line_no, "Cannot use variable in place of label")
            error=True
    if(not error):
        if(words[1] not in labels):
            print("Error in line number",line_no, "Undefined Label")
            error=True
		
def type_f(line):
    words=line.split()
    global error
    if(len(words)!=1):
        error=True
        print("Error in line number",line_no, "Invalid Syntax")
    if(not error):
         if(words[0]!="hlt"):
            print("Error in line number",line_no, "Invalid Syntax")
    if(T!=line_no):
        print("Error in line number",line_no, "hlt must be at the end")
        error=True
	
def type_flag(line):
    words=line.split()
    global error
    if(len(words))!=3:
        error=True
        print("Error in line number",line_no, "Invalid Syntax")
    if(not error):
        for i in range(1,len(words)):
            if words[i] not in reg_flag:
                error=True
                print("Error in line number",line_no,"Invalid Register or Invalid Flag")
                break
	
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
        result += figures*[i]*2**i
    return result

line_no=1 #Starting from line zero
line1=1
line2=0
vcount=0
ecount=0
inscount=-1

for i in lines:
    c=i.split()
    if i!="":
	    if c[0]=='var':
			vcount+=1
			s=i.split()
			if(len(s)>1):
				if(s[1] in var):
				error=True
				print("Error in line number",line1,"Invalid syntax- same variable declared again")
			else:
				var.append(s[1])
    else:
        ecount+=1
    line1+=1

var_add=[]
v_c=vcount

for j in var:
    binary=dec_binary(len(lines)-vcount-ecount)
    binary='0'*(8-len(binary))+binary
    var_add.append(binary)
    vcount-=1

def varerror(line):
    global error
    words=line.split()
    if len(words)!=2:
        error=True
        print("Error in line number",line_no,"Invalid syntax - insufficient arguments")
    if (words[1][0]).isdigit() and not error:
        error=True
        print("Error in line number",line_no,"Invalid variable name")
    if (words[1]).isdigit() and not error:
        error=True
        print("Error in line number",line_no,"Invalid variable name")

c=-1
for h in range(len(lines)):
    t=True
    line2+=1
    c+=1
    d=lines[h].split()
    if lines[h]=="":
        c-=1
    if lines[h]!="":
	    if d[0]=='var':
			c-=1
    if not error:
        counter=0
        while t and lines[h]!="":
            if lines[h]!="":
                colon=lines[h].split()
                if colon[0][-1]==":":
                    j=lines[h].split()
                    if (j[0][0]).isdigit():
                        error=True
                        print("Error in line number",line2,"Invalid label name")
                        break
                    if (j[0][0:-1]).isdigit() and not error:
                        error=True
                        print("Error in line number",line2,"Invalid syntax - label name cannot be all numbers")
                        break
                    if not error and (j[0][0:-1] in var or j[0][0:-1] in symbol):
                        error=True
                        print("Error on line number",line2,"Invalid label name")
                        break
                    if not error and j[0][0:-1] not in labels and j[0][0:-1] not in nested_label:
                        counter+=1
                        if counter<2:
                            labels.append(j[0][0:-1])
                            ld=c
                            labels_add.append(ld)
                        else:
                            nested_label.append(j[0][0:-1])
                    else:
                        error=True
                        print("Error in line number",line2,"Invalid syntax - Multiple definitions of label",j[0][0:-1])
                        break
                    colon=colon[1:]
                    s=""
                    for i in range(len(colon)):
                        s=s+colon[i]+" "
                    lines[h]=s
					d=lines[h].split()
					if lines[h]!="":
						if d[0]=="var"and not error:
						error=True
						print("Error on line number",line2,"Invalid Syntax- Cannot define variable inside label")
						break
                else:
                    t=False
		
if lines.count("hlt")>1:
    error=True
    print("Multiple hlt instructions")
	
T=len(lines)
if(T>256):
    error=True
    print("Error - Number of lines is greater than 256")
	
if not error:
    for i in range (len(lines)):
            inscount+=1
            colon=lines[i].split()
	    if lines[i]=="":
	    	inscount-=1
	    else:
		    if colon[0]=='add':
				type_a(lines[i])
				if error:
					break
				if(not error):
					r1=colon[1]
					r2=colon[2]
					r3=colon[3]
					s="10000"+"00"+regaddress[r1]+regaddress[r2]+regaddress[r3]
					check.append(s)
		    elif colon[0]=='sub':
				type_a(lines[i])
				if error:
					break
				if(not error):
					r1=colon[1]
					r2=colon[2]
					r3=colon[3]
					s="10001"+"00"+regaddress[r1]+regaddress[r2]+regaddress[r3]
					check.append(s)
		    elif colon[0]=='mul':
				type_a(lines[i])
				if(error):
					break
				if(not error):
					r1=colon[1]
					r2=colon[2]
					r3=colon[3]
					s="10110"+"00"+regaddress[r1]+regaddress[r2]+regaddress[r3]
					check.append(s)
		    elif colon[0]=='and':
				type_a(lines[i])
				if error:
					break
				if(not error):
					r1=colon[1]
					r2=colon[2]
					r3=colon[3]
					s="11100"+"00"+regaddress[r1]+regaddress[r2]+regaddress[r3]
					check.append(s)
		    elif colon[0]=='or':
				type_a(lines[i])
				if error:
					break
				if(not error):
					r1=colon[1]
					r2=colon[2]
					r3=colon[3]
					s="11011"+"00"+regaddress[r1]+regaddress[r2]+regaddress[r3]
					check.append(s)
		    elif colon[0]=='xor':
				type_a(lines[i])
				if error:
					break
				if(not error):
					r1=colon[1]
					r2=colon[2]
					r3=colon[3]
					s="11010"+"00"+regaddress[r1]+regaddress[r2]+regaddress[r3]
					check.append(s)
		    elif colon[0]=='ls':
				type_b(lines[i])
				if(error):
					break
				if(not error):
					decimal=int(colon[2][1:])
					binary=dec_binary(decimal)
					zero="0"*(8-len(binary))
					s='11001'+regaddress[colon[1]]+zero+binary
					check.append(s)
		    elif colon[0]=='rs':
				type_b(lines[i])
				if(error):
					break
				if(not error):
					decimal=int(colon[2][1:])
					binary=dec_binary(decimal)
					zero="0"*(8-len(binary))
					s='11000'+regaddress[colon[1]]+zero+binary
					check.append(s)
		    elif colon[0]=='mov' and colon[1][0]=='R' and colon[2][0]=='R':
				type_c(lines[i])
				if error:
					break
				if(not error):
					r1=colon[1]
					r2=colon[2]
					s='1001100000'+regaddress[r1]+regaddress[r2]
					check.append(s)
		    elif colon[0]=='mov' and colon[1][0]=='R' and colon[2]=='FLAGS':
				error=True
				print("Error on line number",line_no,"Invalid use of flags")
				break
		    elif colon[0]=='mov' and colon[1]=='FLAGS' and colon[2][0]=='R':
				type_flag(lines[i])
				if error:
					break
				if(not error):
					r1=colon[1]
					r2=colon[2]
					s='1001100000'+regaddress[r1]+regaddress[r2]
					check.append(s)
		    elif colon[0]=='cmp':
				type_c(lines[i])
				if error:
					break
				if(not error):
					r1=colon[1]
					r2=colon[2]
					s='1111100000'+regaddress[r1]+regaddress[r2]
					check.append(s)
		    elif colon[0]=='not':
				type_c(lines[i])
				if error:
					break
				if(not error):
					r1=colon[1]
					r2=colon[2]
					s='1110100000'+regaddress[r1]+regaddress[r2]
					check.append(s)
		    elif colon[0]=='mov' and colon[2][0]=='$':
				type_b(lines[i])
				if error:
					break
				if not error:
					r1=colon[1]
					decimel=int(colon[2][1:])
					binary=dec_binary(decimel)
					zero="0"*(8-len(binary))
					s='10010'+regaddress[r1]+zero+binary
					check.append(s)
		    elif colon[0]=='div':
				type_c(lines[i])
				if error:
					break
				if(not error):
					s="10111"+"00000"+regaddress[colon[1]]+regaddress[colon[2]]
					check.append(s)
		    elif colon[0]=='ld':
				type_d(lines[i])
				if error:
					break
				if(not error):
					sa=lines[i].split()
					index=var.index(sa[-1])
					varadd=var_add[index]
					s="10100"+regaddress[colon[1]]+varadd
					check.append(s)
		    elif colon[0]=='st':
				type_d(lines[i])
				if error:
					break
				if(not error):
					sa=lines[i].split()
					index=var.index(sa[-1])
					varadd=var_add[index]
					s="10101"+regaddress[colon[1]]+varadd
					check.append(s)
		    elif colon[0]=='jmp':
				type_e(lines[i])
				if error:
					break
				if(not error): 
					j=labels.index(colon[1]) 
					r=labels_add[j]
					b=str(dec_binary(r))   
					g="0"*(8-len(b))         
					s="11111000"+g+b
					check.append(s)
		    elif colon[0]=='jlt':
				type_e(lines[i])
				if error:
					break
				if(not error):
					j=labels.index(colon[1]) 
					r=labels_add[j]
					b=str(dec_binary(r)) 
					g="0"*(8-len(b)) 
					s="01100"+"000"+g+b
					check.append(s)
		    elif colon[0]=='jgt':
				type_e(lines[i])
				if error:
					break
				if(not error):
					j=labels.index(colon[1]) 
					r=labels_add[j]
					b=str(dec_binary(r))
					g="0"*(8-len(b))  
					s="01101"+"000"+g+b
					check.append(s)
		    elif colon[0]=='je':
				type_e(lines[i])
				if error:
					break
				if(not error):
					j=labels.index(colon[1]) 
					r=labels_add[j]
					b=str(dec_binary(r)) 
					g="0"*(8-len(b)) 
					s="01111"+"000"+g+b
					check.append(s)
		    elif colon[0]=='hlt':
				type_f(lines[i])
				if(error):
					break
				if not error:                                                                                                                                                                                                                                                                                                                                 
					s="0101000000000000"
					check.append(s)
		    elif colon[0]=='var':
				varerror(lines[i])
				if inscount>0:
					print("Error on line number",line_no," Variable cannot be declared after instruction")
					error=True
				inscount-=1
				if error:
					break
		    else:
				error=True
				print("Error in line number",line_no,"Invalid instruction or label name")
				line_no+=1

if(not error):
	if lines[-1]!="hlt":
		print("Error in line number",line_no,"Invalid Syntax - No hlt at the end")
        error=True
			
if(not error):
	print(*check,sep="\n")
