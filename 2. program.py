print("Kérlek add meg a felhasználóneved és a jelszavadat!")

#A felhasználó által beállított felhasználónév és jelszó legyen:

a = "Név123"
b = "Jelszó123"


nev = input("Felhasználónév: ")
jelszo = input("Jelszó: ")

while nev != a and jelszo != b:
    print("Hibás felhasználónév vagy/és jelszó!")
    nev = input("Felhasználónév: ")
    jelszo = input("Jelszó: ")

print("Sikeres bejelentkezés!")