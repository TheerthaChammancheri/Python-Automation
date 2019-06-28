dict=[{'name':"aswathy",'employeeid':1234,'age':23},{'name':"sandeep",'employeeid':5678,'age':24},{'name':"theertha",'employeeid':1591,'age':25}]
print sorted(lambda d: d['age'], dict)
#print(sorted(dict ,key = lambda d: d['age']))
