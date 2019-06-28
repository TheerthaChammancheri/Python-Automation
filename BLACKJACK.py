def blackjack(x,y,z):
    if x+y+z<=21:
        return x+y+z
    elif x+y+z>21 and (x==11 or y==11 or z==11):
        return x+y+z-10
    elif x+y+z>21:
        return "BUST"



x=blackjack(5, 6, 7)
print x
y=blackjack(9,9,9)
print y
z= blackjack(9,9,11)
print z