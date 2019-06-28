def count_string(str):
    c=0
    for n in str:
        if len(n)>=2 and n[0]==n[-1]:
            c=+1
            return c

str=['bab', 'ce', 'cba', 'syanora']
count=count_string(str)
print count

