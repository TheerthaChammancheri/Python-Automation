def max(l1,l2,l3):
    l1.sort()
    l2.sort()
    l3.sort()
    maxlist = [l1[-2], l1[-1], l2[-2], l2[-1], l3[-2], l3[-1]]
    print maxlist
    return maxlist

def avg(l):
    average = sum(l) // len(l)
    print(average)

def min(l1,l2,l3):
    l1.sort()
    l2.sort()
    l3.sort()
    minlist = [l1[1], l1[2], l2[1], l2[2], l3[1], l3[2]]
    print minlist
    return minlist

list1=[1,2,3,4,5,6,7]
list2=[11,12,13,14,15,16]
list3=[21,22,23]
l1=max(list1,list2,list3)
avg(l1)
l2=min(list1,list2,list3)
avg(l2)

