'''
A Ducci sequence is a sequence of lists of integers. Given a starting list of integers, the next list in the sequence is formed by taking the absolute differences of neighboring integers in the previous list.

Start List: [0,653,1854,4063]

Ducci Sequence:[653,1201,2209,4063], [548,1008,1854,3410], ...........,[0,0,0,0]

Assumption: The Ducci sequence ends with a list containing 0s and the starting list contains four elements.

Write a python function that takes a starting list of integers and a number ‘n’ as input, and returns the nth element of the Ducci sequence.
'''
#lex_auth_0127136216235950081185

def ducci_sequence(test_list,n):
    final_list=[]
    for i in range(n+1):
        temp=[]
        for x in range(-1,-5,-1):  #take sub in reverse order and in negative range 
            temp.insert(0,abs(test_list[x]-test_list[x+1]))
        test_list=temp
        final_list.append(temp)
    return final_list[n]

ducci_element=ducci_sequence([0, 653, 1854, 4063] , 6)
print(ducci_element)