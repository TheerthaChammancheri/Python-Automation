def lower_upper(sample):
    lower,upper=0,0
    for n in sample:
        if n.islower():
            lower+=1
        elif n.isupper():
            upper+=1
    print lower,upper
lower_upper('Hello Mr. Rogers, how are you this fine Tuesday?')
