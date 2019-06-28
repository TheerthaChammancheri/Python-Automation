def check_vowel(mystring):
    first_char = mystring[0]
    if first_char in 'aeiou':
        print(mystring+'ay')
    else:
        print(mystring[1:]+first_char+'ay')

check_vowel('word')