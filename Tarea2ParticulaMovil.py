import random
from random import randint
from random import choice


def main():
    movimiento = randint (50,100)
    l = randint(30,70)
    loc = randint(0,movimiento
                  )


    for x in range (movimiento):
        j = ('o'*(loc-1)+ '֍' + 'o' *(l-loc))
        loc += choice([1,-1])
        if loc > movimiento:
            loc -= movimiento
        elif loc < 0:
            loc += movimiento
        print (j)
if __name__ == "__main__":
    main()
    




