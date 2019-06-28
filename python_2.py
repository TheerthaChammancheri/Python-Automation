def sorts(str):
    str.sort()
    data1=[]
    data2=[]
    for n in str:
        if n[0].lower()=='x':
            data1.append(n)
        else:
            data2.append(n)
    return data1+data2

str=['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
x=sorts(str)
print x