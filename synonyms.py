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
