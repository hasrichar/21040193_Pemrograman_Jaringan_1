big_tail = int(input("apakah berang berang memiliki ekor besar? (yes=1/no=0): "))
glasses = int(input("apakah memakai kacamata? (yes=1/no=0): "))
blue_trousers = int(input("Apakah memakai celana biru? (yes=1, no=0): "))
yellow_hat = int(input("Apakah memakai topi kuning? (yes=1, no=0): "))

if big_tail == 1 and glasses == 1 and blue_trousers == 1 and yellow_hat == 1:
    print("Berang-berang memakai baju yang benar yaitu \n big tail, glasses, blue trousers, yellow hat.")
else:
    print("Berang-berang tidak memakai baju yang benar.")
