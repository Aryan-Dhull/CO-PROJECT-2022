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
            error=True
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

line_no=1 #Starting from line one
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
