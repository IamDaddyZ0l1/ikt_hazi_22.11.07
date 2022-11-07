print("Üdvözöllek a programban!")

mehet = input("Készen állsz a kérdések megválaszolására? (Igen/Nem): ")

a = "Igen"
b = "Nem"

ev = 2022

if mehet == a:
    kernev = input("Hogy hívnak? ")
    print("Üdvözöllek", kernev)
    kerszulev = int(input("Melyik évben születtél? "))
    print(ev - kerszulev,"éves vagy!" )
    kermagass = float(input("Milyen magas vagy?"))
    print("A magasságod: ",kermagass, "cm")
    kersuly = float(input("Mennyi a súlyod?"))
    print("A súlyod: ",kersuly,"kg")
    kerjatek = input("Akarsz játszani egy játékot? (Igen/Nem) ")
    
    if kerjatek == a:
        hanytol = int(input("Melyik egész számtól kezdődjön a számolás? "))
        hanyig = int(input("Melyik egész számíg tartson a számolás? "))
        hanyasaval = int(input("Hanyasával számoljon a program? "))
        
        for x in range(hanytol,hanyig + 1,hanyasaval):
            print(x)
        
    if kerjatek == b:
        print("Akkor majd legközelebb.")
        
    if kerjatek != a and kerjatek != b:
        print("Nincs ilyen választási lehetőség!")
        
    kerelvezted = input("Élvezted a program kitöltését? (Igen/Nem) ")
    
    if kerelvezted == a:
        print("Örülök hogy élvezted a programomat! :)")
        print("Köszönöm a kitöltötést! További jó reggelt/napot/estét!")
        
    if kerelvezted == b:
        print("Ez van.")
        
    if kerelvezted != a and kerelvezted != b:
        print("Nincs ilyen választási lehetőség!")
        
    
    
    
if mehet == b:
    print("Térj vissza, ha úgy érzed, hogy készen állsz!")
    
if mehet != a and mehet != b:
    print("Nincs ilyen választási lehetőség! Indítsd újra a programot, az újrakezdéshez!")
    