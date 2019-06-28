def animal_crackers(two_word):
    if (two_word.split()[0][0].lower()== two_word.split()[1][0].lower()):
        return (True)
    else:
        return (False)

x= animal_crackers('Levelheaded Llama')
print x