from collections import Counter
str="In the following example of using Counter, a list of few elements is created that contains duplicate elements."
s=str.split(" ")
x=Counter(s)
print(x.most_common(5))
