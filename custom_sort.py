'''
Custom Sort
Description
You have been given a lot of words, all different. You are to sort them as per the following requirements:
Sort the words by length: the longest word first.
If the length of two words is the same, compare the first letter of both the words. The letter that is lower on the lexicographical order is placed above the one that appears higher on the order.
If a tie still exists, then compare the last letters. The letter that is lower on the lexicographical order is placed above the one that appears higher on the order.
If a tie still exists, compare the second letters. The letter that is lower on the lexicographical order is placed above the one that appears higher on the order
If a tie still exists, compare the second last letters. The letter that is lower on the lexicographical order is placed above the one that appears higher on the order
And so on.
Note- Lexicographical order is (A(lowest), B, C, D, … X, Y, Z(highest) )


Input: A list of words.

Output: A list of the same words sorted according to the instructions in the question.


Sample input
['laptop',   'Mobile',   'moaile',   'mobize', 'Car']
Sample output
['laptop', 'moaile', 'Mobile', 'mobize', 'Car']

Please refer to the sample input and output in case of any confusion
'''

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
