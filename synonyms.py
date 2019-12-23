'''
Creating a Dictionary
Description
Larry is an immigrant in the USA and has a hard time understanding English there. So he decides to make a software that will tell him the synonyms of the word that he types. He has asked you for help.

Remember, you will first need to choose a data structure that you will use to store the information about the words. You can use lists or dict or tuple or anything else for this purpose.

There will be two actions involved:
Action 1 = Store the following words as synonyms of each other.
Action 2 = Always followed by one word. Print ALL the synonyms of that word in alphabetical order (note: the synonyms printed should not have the query word).


Input:
The input will be one list whose first entry is an int ‘test’ and all other subsequent entries will be lists. ‘test’ will represent the number of lists that follow.
Each of the following lists will consist of a number as its zeroth index (1 or 2) denoting the action to be taken on the words.

Output:
Each action 2 will print the synonyms in the order it is called.


Sample input:
[   7,
    [1,'good','sound','first-class'],
    [1,'enough', 'abundant'],
    [1,'adequate', 'enough', 'ample'],
    [2, 'adequate'],
    [2, 'good'],
    [1, 'bright', 'illuminous'],
    [2, 'cs']  ]

Sample output:
adequate: abundant,ample,enough
good: first-class,sound
cs: 


Explanation:
There are three queries for Action 2 and, hence, the output will have three lines.
Line 1: Adequate has three synonyms (  [1,'enough', 'abundant'],  [1,'adequate', 'enough', 'ample'],). 
So the three synonyms will be printed in alphabetical order:
Enough: abundant,ample,enough
 Line 2: Good has two synonyms (  [1,'good','sound','first-class']  ). 
So the two synonyms will be printed in alphabetical order:
Good: first-class, sound
Line 3: there are no synonyms added for cs and hence no synonyms will be printed, but just “cs:  ”.(Note space after cs: )
Note that the print order is the same as the order in which ACTION2 is called i.e. adequate, good, cs
'''

import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

#start writing your code from here
#input_list has the input 
test=int(input_list[0])
final_list=[] #will be the list of sets

for i in range(1,test+1):
    flag=1
    if input_list[i][0]==1: #ACTION 1

        if not (final_list): 
            final_list.append(set(input_list[i][1:]))
            flag=0
        else:
            for s in range(len(final_list)):
                if (final_list[s].intersection(set(input_list[i][1:]))):
                    #if theres any intersection, add all words to that set
                    final_list[s]=final_list[s].union(set(input_list[i][1:]))
                    flag=0
        if (flag):
            final_list.append(set(input_list[i][1:]))


    if input_list[i][0]==2: #ACTION 2
        #print all synonyms
        show=[]
        print(input_list[i][1], end=': ')
        for s in range(len(final_list)):
                if (final_list[s].intersection(set(input_list[i][1:]))):
                    show=final_list[s].difference(set(input_list[i][1:]))
                    show=sorted(show) 
        show=",".join(show)
        print(show)
