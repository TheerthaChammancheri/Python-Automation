from itertools import permutations
str_lst=['cat','tac','dog','god','act','strings']
x=(list(permutations(str_lst,r=2)))
for y in x:
    if sorted(y[0])==sorted (y[1]):
        print y
