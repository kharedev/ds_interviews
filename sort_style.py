import ast
import sys

input_str = sys.stdin.read()
inp = ast.literal_eval(input_str)

def get_iterations(num):
    seq=[]
    first=0
    last=num-1
    i=0
    while(first<=last):
        if i%2==0:
            seq.append(first)
            first=first+1
            i=i+1
        else:
            seq.append(last)
            last=last-1
            i=i+1
    return seq

def get_bigger(st1, st2):
    if (len(st1) != len(st2)):
        if len(st1)>len(st2):
            return st1
        else:
            return st2

    l=len(st1)
    sequence=get_iterations(l)
    st1_="".join([st1[i].lower() for i in sequence])
    st2_="".join([st2[i].lower() for i in sequence])
    if st1_<st2_:
        return st1
    else:
        return st2


length=len(inp)
for i in range(length):
    for j in range(length-1, i-2, -1):
        if inp[j] == get_bigger(inp[j], inp[j-1]):
            temp=inp[j]
            inp[j]=inp[j-1]
            inp[j-1]=temp

print(inp)
