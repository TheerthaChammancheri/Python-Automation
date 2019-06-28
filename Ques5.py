rd=open('input.txt','r')
str=rd.readlines()
for i,l in enumerate(str):
    cnt=0
    x=l.split(" ")
    word=len(x)
    print ("No of words in line {0} is {1}".format(i, word))
    for j,y in enumerate(x):
        z=len(y)
        cnt=cnt+z
    print ("No of characters in line {0} is {1}".format(i, cnt))
rd.close()

