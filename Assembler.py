with open ('input.txt',"r") as f:
	lines=f.read().splitlines()

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