st = 'Create a list of the first letters of every word in this string'
print([n[0] for n in st.split() if len(n)%2==0])