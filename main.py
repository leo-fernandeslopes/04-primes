""" Dans main.py, on écrit la fonction isprime(nb) et ses tests automatiques. """

#### Fonction secondaire

def isprime(nb):
    """
    La fonction prend en paramètre un entier nb 
    et renvoie un booléen qui affirme si nb est premier. 
    """
    premier = True

    for d in range(2, nb) :
        if nb % d == 0 :
            premier = False

    if nb in (0, 1) :
        premier = False

    return premier


#### Fonction principale


def main():
    """
    La procédure ne prend pas de paramètre et print les tests de isprime(). 
    """
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
