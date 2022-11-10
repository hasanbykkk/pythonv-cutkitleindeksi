
#vücutkitlehesaplama programı

boy =float(input("boyunuzu metre cinsinden giriniz"))
kilo =int(input("kilonuzu giriniz"))
vki = kilo/(boy*boy)

if vki < 18.5:
 print(f"Vücut kitle indeksiniz: {vki}, zayıfsınız")
elif vki < 25:
 print(f"Vücut kitle indeksiniz: {vki}, normal")
elif vki < 30:
 print(f"Vücut kitle indeksiniz: {vki}, kilonuz biraz fazla")
elif vki < 35:
 print(f"Vücut kitle indeksiniz: {vki}, 1.derece obezsiniz")
elif vki < 40:
 print(f"Vücut kitle indeksiniz: {vki}, 2.derece obezsiniz")
else:
 print(f"Vücut kitle indeksiniz: {vki}, 3.derece obezsiniz")

