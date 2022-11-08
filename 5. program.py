print("Üdvözöllek a súlyemelők számológépében!")

sets = int(input("Mennyi ismétlésed lesz? "))

for x in range(0,sets,1):
  rud = float(input("Add meg kg-ban a súlyát annak a rúdnak, amit használni fogsz: ")) 

  suly = float(input("Add meg kg-ban azt a súlymennyiséget, amit rá szeretnél rakni a rúdra: "))

  rud_es_suly = rud + suly

  print("Ez összesen ", rud_es_suly, "kg")
 
print("Tartsd fent a kemyén munkát, találkoznk a következő edzésnél!")
