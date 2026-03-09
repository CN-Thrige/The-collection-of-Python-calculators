

def main ():
    intro()

    ml_needed = float(input("Enter number of ml needed: "))
    ml_to_dl(ml_needed)

    dl_needed = float(input("Enter number of dl needed: "))
    dl_to_l (dl_needed)

def intro():
    print("this program converts messurement ml to l!")

def ml_to_dl(dl):
    milliliter = dl/100
    print(f'Here the program converts ml to {milliliter} dl')


def dl_to_l(l):
    liter = l/100
    print(f'Here the program converts dl to {liter} l')

main()
