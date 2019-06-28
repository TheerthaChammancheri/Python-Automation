st = 'Print every word in this sentence that has an even number of letters'
for n in st.split():
    if len(n)%2==0:
        print ("{} even".format(n))

