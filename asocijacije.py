import csv

#ucita podatke iz csv i napravi listu listi lista_podataka
with open('podatci.csv', 'r') as f:
  	reader = csv.reader(f)
  	lista_podataka = list(reader)

#izdvoji svaku listu zasebno
lista_1 = lista_podataka[0]
lista_2 = lista_podataka[1]
lista_3 = lista_podataka[2]
lista_4 = lista_podataka[3]
lista_5 = lista_podataka[4]

bodovi = 0
rijec = 0

#prikaze rijeci za asocijaciju
print("{}, {}, {}, {}".format(lista_1[0],lista_1[1],lista_1[2],lista_1[3]))

#provjera unesenih rijeci kod pogadanja
while rijec != lista_1[4]:
	#unos rijeci
	rijec = input()
	#provjera rijeci
	if(rijec == lista_1[4]):
		#ako je tocno ispisi i dodaj bodove
		print("Tocno!")
		bodovi += 5
		print("Broj bodova: {}".format(bodovi))
	else:
		#ako je netocno ispisi i pokusaj opet
		print("Netocno!")

#prikaze rijeci za asocijaciju
print("{}, {}, {}, {}".format(lista_2[0],lista_2[1],lista_2[2],lista_2[3]))

#provjera unesenih rijeci kod pogadanja
while rijec != lista_2[4]:
	#unos rijeci
	rijec = input()
	#provjera rijeci
	if(rijec == lista_2[4]):
		#ako je tocno ispisi i dodaj bodove
		print("Tocno!")
		bodovi += 5
		print("Broj bodova: {}".format(bodovi))
	else:
		#ako je netocno ispisi i pokusaj opet
		print("Netocno!")

#prikaze rijeci za asocijaciju
print("{}, {}, {}, {}".format(lista_3[0],lista_3[1],lista_3[2],lista_3[3]))

#provjera unesenih rijeci kod pogadanja
while rijec != lista_3[4]:
	#unos rijeci
	rijec = input()
	#provjera rijeci
	if(rijec == lista_3[4]):
		#ako je tocno ispisi i dodaj bodove
		print("Tocno!")
		bodovi += 5
		print("Broj bodova: {}".format(bodovi))
	else:
		#ako je netocno ispisi i pokusaj opet
		print("Netocno!")

#prikaze rijeci za asocijaciju
print("{}, {}, {}, {}".format(lista_4[0],lista_4[1],lista_4[2],lista_4[3]))

#provjera unesenih rijeci kod pogadanja
while rijec != lista_4[4]:
	#unos rijeci
	rijec = input()
	#provjera rijeci
	if(rijec == lista_4[4]):
		#ako je tocno ispisi i dodaj bodove
		print("Tocno!")
		bodovi += 5
		print("Broj bodova: {}".format(bodovi))
	else:
		#ako je netocno ispisi i pokusaj opet
		print("Netocno!")

#provjera zavrsnog pojma
print("Pogodene rijeci su: {}, {}, {}, {}. Koje je rjesenje?".format(lista_1[4],lista_2[4],lista_3[4],lista_4[4]))

#provjera unesenih rijeci kod pogadanja
while rijec != lista_5[0]:
	#unos rijeci
	rijec = input()
	#provjera rijeci
	if(rijec == lista_5[0]):
		#ako je tocno ispisi i dodaj bodove
		print("Tocno!")
		bodovi += 10
		print("Cestitamo, zavrsili ste igru s {} bodova".format(bodovi))
	else:
		#ako je netocno ispisi i pokusaj opet
		print("Netocno!")