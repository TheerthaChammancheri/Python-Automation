def lesser_of_two_evens(x,y):
    if x%2==0 and y%2==0:
        print(min(x,y))
    elif x%2==0 or y%2==0:
        print(max(x,y))

lesser_of_two_evens(2,5)
lesser_of_two_evens(2,4)