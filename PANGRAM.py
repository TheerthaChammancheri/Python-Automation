import string
def pangram(x):
    alphabet=string.ascii_lowercase
    a=''.join(sorted(set(x.lower()))).strip()
    if a==alphabet:
        print("pangram")
    else:
        print("not pangram")

pangram("The quick brown fox jumps over the lazy dog")