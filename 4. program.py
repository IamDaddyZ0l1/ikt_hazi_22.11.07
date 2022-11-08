print("Ebben a programban kiszámoljuk hogy hány éves vagy!")

ev = 2022

szulev = int(input("Add meg a születési évedet: "))

kor = ev - szulev

print(kor, "éves vagy!")

felnott = 18


if kor > felnott:
  print("Már felnőtt vagy!")
  
if kor < felnott:
  print("Még gyerek vagy!")
  
if kor == felnott:
  print("Még nemrég lettél felnőtt!")
