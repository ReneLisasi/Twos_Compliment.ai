#author: RLisasi
#assignment 1: two's compliment
#CS3406-01

print("enter a binary")
input=input()
stack=[]
#preprocess
for n in input:
    stack.append(n)

print(stack)
#define state 1
def copy(stack):
    print('copy')
    return stack
#define state 2
def flip(stack,n):
    for n in range(n,len(stack)):
        if stack[n]=='1':
            stack[n]='0'
        else:
            stack[n]='1'
        print('flip')
    return stack

#initialize the state    
state='copy'
stack.reverse()#reverse the stack becasue I can't figure out how to  do a reverse for loop in python :)
for n in range(len(stack)):
    if stack[n]=='1':#sensor1
       state='flip'#declare state change
       n+=1#skip the first 1
       stack=flip(stack,n)#state change method call
       break
        
    else:#sensor2
        if state=='flip':#check state status
            break
        else:
            stack=copy(stack)
    
stack.reverse()
print(stack)

#add one
# bin1=''.join(stack)
# print(bin1)
# bin2='1'
# sum=bin(int(bin1,2)+int(bin2,2))
# print(sum[2:])