import funkcije

''' Stampanje rezervisanih karata za ulogovanog kupca'''

def pregled_rezervacijaKupac():
	i = 0
	with open('ulogovan.txt', 'r') as f:
		for l in f.readlines():
			if l.split('|')[4] == 'kupac\n':
				a = l.split('|')[0]
				with open('karte.txt', 'r') as d:
					for r in d.readlines():
						try:
							if a == r.split('|')[2] and r.split('|')[13] == 'R\n':
								print( r.split('|')[3])
								print( r.split('|')[9])
								print( r.split('|')[4] + " " + r.split('|')[5])
								print( r.split('|')[4] + " " + r.split('|')[6])
								print( r.split('|')[11])
								print("")
								i = i + 1
						except IndexError:
							print()
	if i == 0:
		return i

''' Kupcu se prikazuju njegove rezervisane karte.
Trazi se da unese termin projekcije i sediste odstampane karte koju zeli ponistiti.
Izabrana karta se ponistava i nudi se da ponisti jos karata ili da se vati u meni'''

def ponistavanje_rezervisanihKupac():
	p=pregled_rezervacijaKupac()
	if p != 0:
		i = 0
		termin = input("Unesite sifru termina karte koju zelite ponistiti:  ")
		sediste = input("Unesite oznaku sedista:  ")
		if termin != '' and sediste != '':
			with open('karte.txt', 'r') as f:
				for l in f.readlines():
					try:
						if [termin,sediste] == [l.split('|')[3],l.split('|')[11]]:
							i = i + 1
							funkcije.ponistavanje_rezervacije(termin,sediste)
					except IndexError:
						print()
				funkcije.brojac(i)
		else:
			print("Niste uneli termin ili oznaku sedista.")

		print("")
		print("Da li zelite: ")
		print("1. Nastaviti ponistavanje rezervacija ")
		print("2. Vratiti se u glavni meni")
		odg = input(">>>   ")
		if odg == '1':
			ponistavanje_rezervisanihKupac()
		elif odg == '2':
			print()
	else:
		print("Ponistavanje rezervacije nije moguce. Nemate rezervisanih karata.")

