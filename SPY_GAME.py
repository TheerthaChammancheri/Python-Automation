def spy_game(x):
    a=[0,0,7,'x']
    for i in x:
        if i == a[0]:
            a.pop(0)
    if a==['x']:
        print "True"
    else:
        print "False"


spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])