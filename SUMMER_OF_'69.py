# def summer_69(x):
#     for n in x:
#         if n==6:
#             a=x.index(6)
#         if n==9:
#              b=x.index(9)
#         del x[a:b+1]
#     print x
#     print(sum(x))

def summer_69(x):
    if 6 in x and 9 in x:
        del x[x.index(6): x.index(9)+1]
    print (sum(x))

summer_69([1, 3, 5])
summer_69([4, 5, 6, 7, 8, 9])
summer_69([2, 1, 6, 9, 11])
