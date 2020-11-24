'''
CreMipsted on Nov 10, 2020

@Mipsuthor: Mipssus

'''
from pip._vendor.distlib.compat import raw_input
from _overlapped import NULL

Rtype ={"add","addu","jr","and"}
Itype ={"addi","beq","bne","lw","sw","addiu","andi","lbu","lhu","lui"}
Jtype ={"j","jal",}
Mips = open("ASM.txt",'r+')
object1= open("out",mode='w')
def findlabel (str,flag):
    i=-1
    t=0
    temp = str +':'
    for line in lineMips:
        if line.find(temp) != -1 :
            a=i 
            print(a)
            break
        if flag==1:
            t=t+1
        i=i+1
    return a-t
def register(str):
    if str == "$zero":
        reg='00000'
    elif str == "$at":
        reg='00001'
    elif str == "$v0":
        reg='00010'
    elif str =="$v1":
        reg='00011'
    elif str =="$a0":
        reg='00100'
    elif str =="$a1":
        reg='00101'
    elif str =="$a2":
        reg='00110'
    elif str =="$a3":
        reg='00111'
    elif str =="$t0":
        reg='01000'
    elif str =="$t1":
        reg='01001'
    elif str =="$t2":
        reg='01010'
    elif str =="$t3":
        reg='01011'
    elif str =="$t4":
        reg='01100'
    elif str =="$t5":
        reg='01101'
    elif str== "$t6":
        reg='01110'
    elif str=="$t7":
        reg='01111'
    elif str=="$s0":
        reg='10000'
    elif str== "$s1":
        reg='10001'
    elif str =="$s2":
        reg='10010'
    elif str =="$s3":
        reg='10011'
    elif str=="$s4":
        reg='10100'
    elif str=="$s5":
        reg='10101'
    elif str=="$s6":
        reg='10110'
    elif str=="$s7":
        reg='10111'
    elif str=="$t8":
        reg='11000'
    elif str=="$t9":
        reg='11001'
    elif str=="$k0":
        reg='11010'
    elif str=="$k1":
        reg='11011'
    elif str=="$gp":
        reg='11100'
    elif str=="$sp":
        reg='11101'
    elif str=="$fp":
        reg='11110'
    elif str=="$ra":
        reg='11111'
    return reg
def Itypeop(str1):
    if str1== "addi":
        opcodetemp = '001000'
    elif str1=="lw":
        opcodetemp = '100011'  
    elif str1== "beq":
        opcodetemp ='000100'
    elif str1 == "bne":
        opcodetemp='000101'
    elif str1== "sw":
        opcodetemp = '101011'
    elif str1== "addiu":
        opcodetemp= '001001'
    elif str1 == "andi":
        opcodetemp ='001100'
    elif str1 =="lbu":
        opcodetemp ='100100'
    elif str1 == "lhu":
        opcodetemp ='100101'
    elif str1 =="lui":
        opcodetemp ='001111'
    return opcodetemp
def Jtypeop(str2):
    if str2== 'j':
        opcodetemp ='000010'
    elif str2 == 'jal':
        opcodetemp = '000011'
    return opcodetemp
def Rtypef(str3):
    if str3 == "add":
        func = '100000'
    elif str3 == "and":
        func ='100100'
    elif str3=="addu":
        func ='100001'
    elif str3=="jr":
        func = '001000' 
    return func

lineMips = Mips.readlines()
i=1
for line in lineMips:
    print(i)
    flag =0;
    pc=i*4
    b = line.find('#')
    if b!=-1:
        line = line[0:b] # delete command   
    #print(line.strip())
    line =line.lstrip()
    record = line.split(' ',1)
    fomat = record[0]
    if fomat in Rtype :
        reg_command = record[1].replace("\n","")
        reg_command = reg_command.replace(" ","")
        opcode = '000000'
        shamp = '00000'
        funct= Rtypef(fomat)
        #print("r type "+opcode)
        if fomat =="jr":
            rs_t=reg_command
            rs =register(rs_t)
            rd ='00000'
            rt ='00000'
        else:
            reg1=reg_command.split(',',2) # rs, rd ,rt
            rd_t = reg1[0]
            rs_t = reg1[1]
            rt_t = reg1[2]
            rd=register(rd_t)
            rs=register(rs_t)
            rt=register(rt_t)
        bit= opcode + rs + rt + rd + shamp+ funct
    elif fomat in Itype : 
        reg_command = record[1]
        reg_command = reg_command.replace(" ","")
        opcode = Itypeop(record[0])
        if fomat =="lui":
            reg2=reg_command.split(',',1)
            rt = register(reg2[0])
            imm = reg2[1].replace("\n","")
            immediate=bin(int(imm))
            immediate=immediate.replace("0b", "")
            immediate=format(int(immediate,2),'021b')
            bit = opcode + rt +immediate
        elif fomat =="lw" or fomat=="sw" or fomat == "lbu" or format =="lhu":# dang 2 doi so khong co nhan
            reg2=reg_command.split(',',1)
            rt = register(reg2[0])
            rism=reg2[1]
            temp=rism.find("(")
            temp2= rism.find(')')
            a=rism[0:temp]
            rs =register(rism[temp+1 : temp2])
            if a != "" :
                immediate=bin(int(a))
                immediate=immediate.replace("0b", "")
            else : immediate ='000000000000000000000'
            immediate2 = format(int(immediate,2),'016b')
            bit= opcode + rs + rt+immediate2
        elif fomat =="addi" or  fomat =="addiu" or fomat =="andi":
            reg_command = record[1]
            reg_command = reg_command.replace(" ","")
            reg2 =reg_command.split(',',2)
            rt = register(reg2[0])
            rs = register(reg2[1])
            imm = reg2[2].replace("\n","")
            immediate=bin(int(imm))
            immediate=immediate.replace("0b", "")
            immediate2 = format(int(immediate,2),'016b')
            bit= opcode + rs + rt+immediate2
            ##print("I type "+opcode )
        elif fomat =="bne" or fomat=="beq":
            reg_command = record[1]
            reg_command = reg_command.replace(" ","")
            reg2 =reg_command.split(',',2)
            rs = register(reg2[0])
            rt = register(reg2[1])
            label= reg2[2].replace("\n","")
            immediate = findlabel(label,flag)-i
            if immediate < 0:
                immediate = bin(65535+int(immediate))
                print(immediate)
            else:
                immediate =bin(immediate)
            ##print(immediate)
            immediate2 = format(int(immediate,2),'016b')
            bit= opcode + rs + rt+immediate2
           # #print("I type "+opcode )
        
    elif fomat in Jtype :
        reg_command = record[1].replace("\n","")
        reg_command = reg_command.replace(" ","")
        opcode = Jtypeop(record[0])
        jaddress=findlabel(reg_command,flag)
        imm = bin(int(jaddress)*4)
        address = format(int(imm,2),'026b')
        bit = opcode+address
        ##print("J type "+opcode)
    else : 
        #print("donot thing")
        #hang trong hoac lenh chua co
        flag = 1
    
    print(flag) 
    if flag == 0:
        i=i+1
        temp3=hex(int('1000',2)).replace('0x',"")
        #print(temp3)
        hex0=format(hex(int(bit[0:4], 2)))
        ##print(hex0)
        hex1=hex(int(bit[4:8], 2)).replace("0x","")
        hex2=hex(int(bit[8:12], 2)).replace("0x","")
        hex3=hex(int(bit[12:16], 2)).replace("0x","")
        hex4=hex(int(bit[16:20], 2)).replace("0x","")
        hex5=hex(int(bit[20:24], 2)).replace('0x',"")
        hex6=hex(int(bit[24:28], 2)).replace("0x","")
        #print(bit[25:28])
        hex7=hex(int(bit[28:32], 2)).replace("0x","")
        hexa= hex0+hex1+hex2+hex3+hex4+hex5+hex6+hex7
        ##print(hexa)
        #object1.write(bit+ "\n")
        object1.write(hexa+"\n")
    
    
    #object.close()    
        