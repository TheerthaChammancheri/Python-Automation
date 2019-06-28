inp=input('Enter the netmask: ')
l=[]
for i in [24, 16, 8, 0]:
    x=str((0xffffffff << (32 - inp) >> i) & 0xff)
    l.append(x)
netmask = '.'.join(l)
print netmask
