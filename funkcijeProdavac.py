import funkcije

''' Prodavcu se stampaju sve rezervisane karte.'''

def pregled_rezervacijaProdavac():
	i = 0
	with open('karte.txt', 'r') as f:
		for l in f.readlines():
			if l.split('|')[13] == 'R\n':
				print(l.split('|')[3])
				print(l.split('|')[0] + " " + (l.split('|')[1]))
				print(l.split('|')[2])
				print(l.split('|')[9])
				print(l.split('|')[4] + " " + l.split('|')[5])
				print(l.split('|')[4] + " " + l.split('|')[6])
				print(l.split('|')[11])
				print(l.split('|')[13])
				print("")
				i = i + 1
	if i == 0:
		return i

''' Prodavcu se stampaju sve rezervisane karte.
Zahteva se unos sedista i termina projekcije za kartu koju zeli ponisiti.
Kad se rezervacija ponisti moze da ponisti jos ili da se vrati u meni'''

def ponistavanje_rezervisanihProdavac():
	r = pregled_rezervacijaProdavac()
	if r != 0:
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
			
		if i == 0:
			print("Pogresan unos sifre termina ili oznake sedista.")

		print("")
		print("Da li zelite da: ")
		print("1. Nastavite ponistavanje rezervacija ")
		print("2. Nastavite sa radom")
		odg = input(">>>   ")

		if odg == '1':
			ponistavanje_rezervisanihProdavac()
		elif odg == '2':
			print("Nastavljamo sa radom!")
			print()

	else:
		print('Nema rezervisanih karata.\n')

''' Pretraga karata za prodavca. Moze pretrazivati karte po vise razlicitih parametara'''

def pretraga_karata():
	i = 0
	odg = ''
	while odg not in ['1', '2', '3', '4', '5', '6', '7']:
		odg = input("Izaberite nacin pregrage karata po: \n\
			1. Sifri projekcije. \n\
			2. Imenu kupca\n\
			3. Prezimenu kupca\n\
			4. Korisnickom imenu kupca\n\
			5. Datumu i vreme pocetka/kraja projekcije\n\
			6. Rezervisane karte \n\
			7. Prodate karte\n\
			>>>>>> ")
		with open('karte.txt', 'r') as f:
				if odg == '1':
					a = input("Unesite sifru projekcije: ")
					for l in f.readlines():
						if a.upper() == l.split('|')[3]:
							print(l)
							print()
							i = i + 1

				elif odg == '2':
					b = input("Unesite ime kupca: ")
					for l in f.readlines():
						if b.lower() == l.split('|')[0].lower():
							print(l)
							print()
							i = i + 1

				elif odg == '3':
					c = input("Unesite prezime kupca: ")
					for l in f.readlines():
						if c.lower() == l.split('|')[1].lower():
							print(l)
							print()
							i = i + 1

				elif odg == '4':
					d = input("Unesite korisnicko ime kupca: ")
					for l in f.readlines():
						if d.lower() == l.split('|')[2].lower():
							print(l)
							print()
							i = i + 1

				elif odg == '5':
					vreme1 = input("Unesite vreme pocetka projekcije [hh:mm] :   ")
					vreme2 = input("Unesite vreme kraja projekcije [hh:mm] :   ")
					datum = input("Unesite datum projekcije [dd.mm.gggg.] :  ")
					for l in f.readlines():
						if vreme1 == l.split('|')[5] and vreme2 == l.split('|')[6] and datum == l.split('|')[12]:
							print(l)
							print()
							i = i + 1

				elif odg == '6':
					print("Rezervisane karte su: ")
					print()
					for l in f.readlines():
						if l.split('|')[13] == 'R\n':
							print(l)
							print()
							i = i + 1

				elif odg == '7':
					print("Kupljene karte su: ")
					print()
					for l in f.readlines():
						if l.split('|')[13] == 'P':
							print(l)
							print("")
							i = i + 1

	funkcije.brojac(i)


''' Prodavcu se nudi da li zeli da proda rezervisanu kartu ili bez rezervacije.
Na osnovu izbora pozivaju se funkcije prodaja rezervacije ili direktna prodaja'''

def prodaja_karata():
	print("Da li zelite da prodate: ")
	print("1. Rezervisanu kartu")
	print("2. Kartu bez rezervacije")
	a = input(" >>>  ")
	if a == '1':
		prodaja_rezervacije()
	elif a == '2':
		direktna_prodaja()

''' Prodaja karte direktno bez prethodne rezervacije. 
Unosi se termin, sediste i korisnicko ime kupca.
Prodavcu nudimo da proda jos karata ili da se vrati u meni'''

def direktna_prodaja():
		termin = funkcije.odabir_termina()
		sediste = funkcije.sediste(termin)
		if sediste != None:
			korime = input("Unesite korisnicko ime kupca:   ")
			with open('korisnici.txt', 'r') as f:
					for l in f.readlines():
						if korime == l.split('|')[0] and l.split('|')[4] == 'kupac\n':
							prodata_stampanje(termin,sediste,korime)
			print("1. Nastavi sa direktnom prodajom karata")
			print("2. Vrati se u glavni meni")
			a = input(">>>   ")
			if a == '1':
				direktna_prodaja()
			elif a == '2':
				print(" Povratak u glavni meni ")
				print("")
		else:
			print("Niste izabrali sediste.")
			print("")


''' Dobija termin,sediste, i korisnicko ime i na osnovu tih podataka dodaje kartu u fajl karte prodatu kartu'''

def prodata_stampanje(termin,sediste,korime):
	datum = funkcije.vreme()
	ime = ""
	prezime = ""
	with open('korisnici.txt', 'r') as f:
		for l in f.readlines():
			if korime == l.split('|')[0]:
				ime = l.split('|')[2]
				prezime  = l.split('|')[3]
				break

	projekcija = ""
	with open('terminprojekcije.txt', 'r') as f:
		for l in f.readlines():
			if termin == l.split('|')[0]:
				projekcija = l.rstrip()
				break

	prodavac = ""
	with open('ulogovan.txt', 'r') as f:
		for l in f.readlines():
			prodavac = l.split('|')[0]

	with open('karte.txt', 'a') as f:
		f.write(ime + '|' + prezime  + '|' + korime + '|' + projekcija + '|' + sediste + '|' + datum + '|' + 'P' + '|' + prodavac + '\n')
		print("Karta je prodata")

''' ucitava rezervisane karte. 
Od prodavca se trazi da unese sifru termina projekcije, sediste i korisnicko ime kupca za kartu koju zeli prodati.
Karti se menja status iz R - rezervisana u P - prodata i pise se korisnicko ime prodavca koji je prodao kartu,
da bi mogli u izvestajima pretrazivati prodate karte po prodavcima'''


def prodaja_rezervacije():
	i = 0
	lista = []
	with open('karte.txt','r') as f:
		for l in f.readlines():
			try:
				if l.split('|')[13] == 'R\n':
					print (l)
					i = i + 1
			except IndexError:
				print("")

	if i > 0:
		sif = input("Unesite sifru termina karte koju zelite da prodate:  ")
		sed = input("Unesite oznaku sedista:  ")
		ime = input("Unesite korisnicko ime kupca:  ")
		with open('karte.txt','r') as f:
			for l in f.readlines():
				try:
					if [sif,sed,ime] == [l.split('|')[3],l.split('|')[11],l.split('|')[2]]:
						i = i + 1
						with open('karte.txt','r') as f:
							for l in f.readlines():
								if [sif,sed,] != [l.split('|')[3],l.split('|')[11]]:
									lista.append(l)
						with open('karte.txt', 'w') as f:
							for r in lista:
								f.write(r)
						prodata_stampanje(sif,sed,ime)
			

				except IndexError:
					print("")

	else:
		print("Nema rezervisanih karata")