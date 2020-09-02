import datetime

''' Stampaju se svi filmovi koji se prikzuju.'''

def pregled_filmova():
	with open('filmovi.txt', 'r') as f:
		for l in f.readlines():
			film = l.split('|')[0]
			zanr = l.split('|')[1]
			vreme = l.split('|')[2]
			reziser = l.split('|')[3]
			glumci = l.split('|')[4]
			zemlja = l.split('|')[5]
			godina = l.split('|')[6]
			opis = l.split('|')[7]
			print("")
			print ("Naziv filma: " + str(film) + "\n"
				"Zanr: " + str(zanr) + "\n"
				"Trajanje: " + str(vreme) + "\n"
				"Reziser/i: " + str(reziser) + "\n"
				"Glumci: " + str(glumci) + "\n"
				"Zemlja: " + str(zemlja) + "\n"
				"Godina: " + str(godina) + "\n"
				"Opis: " + str(opis))
			print("")
			print ("=" * 30)
			print ("=" * 30)
			print("")

''' Pretraga filmova po raznim parametrima'''

def pretraga_filmova():
	odg= "sss"
	i = 0
	while odg not in ['1','2','3','4','5','6','7']:
		odg = input("Izaberite nacin pretrage filma: \n\
			1. Naziv \n\
			2. Zanr \n\
			3. Vreme trajanja(min/max) \n\
			4. Reziser \n\
			5. Glavne uloge \n\
			6. Zemlja porekla \n\
			7. Godina proizvodnje \n\
			")
		with open('filmovi.txt', 'r') as f:
			if odg == '1':
				a = input("Unesite naziv filma: ")
				for t in f.readlines():
					naziv = t.split('|')[0]
					if a.lower() in naziv.lower():
						print(t.split('|')[0])
						print("")
						i = i + 1

			elif odg =='2':
				b = input("Unesite zanr filma: ")
				for t in f.readlines():
					if b.capitalize() == t.split('|')[1]:
						print(t.split('|')[0])
						print("")
						i = i + 1

			elif odg =='3':
				c1 = input("Unesite minimalno trajanje: ")
				c2 = input("Unesite maksimalno trajanje: ")
				try:
					for t in f.readlines():
						if int(c1) <= int(t.split('|')[2]) and int(t.split('|')[2]) <= int(c2):
							print(t.split('|')[0])
							print("")
							i = i + 1
				except ValueError:
					print("Morate uneti brojeve.")

			elif odg =='4':
				d = input("Unesite ime rezisera: ")
				for t in f.readlines():
					if d.title() == t.split('|')[3]:
						print(t.split('|')[0])
						print("")
						i = i + 1

			elif odg =='5':
				e = input("Unesite imena glavnih glumaca: ")
				for t in f.readlines():
					if e.title() == t.split('|')[4]:
						print(t.split('|')[0])
						print("")
						i = i + 1

			elif odg =='6':
				n = input("Unesite zemlju porekla: ")
				for t in f.readlines():
					if n.upper() == t.split('|')[5]:
						print(t.split('|')[0])
						print("")
						i = i + 1

			elif odg =='7':
				g = input("Unesite godinu proizvodnje: ")
				for t in f.readlines():
					if g == t.split('|')[6]:
						print (t.split('|')[0])
						print("")
						i = i + 1
	brojac(i)


''' Pretraga filmova po raznim parametrima'''

def pretraga_projekcija():
	odg = "aaa"
	i = 0
	while odg not in ['1', '2', '3', '4']:
		odg = input("Izaberite nacin pretrage projekcije: \n\
			1. Film \n\
			2. Sala \n\
			3. Vreme i datum pocetka i kraja projekcije \n\
			Vas izbor: ")

		with open('terminprojekcije.txt', 'r') as f:

			if odg == '1':
				a = input("Unesite naziv filma:   ")

				for t in f.readlines():
					if a.lower() in t.split('|')[6].lower():
						print ("Naziv filma:  " + t.split('|')[6] + "\n"
						"Oznaka sale:  " + str(t.split('|')[5]) + "\n"
						"Datum i vreme pocetka projekcije:  " + str(t.split('|')[1]) + "   " + str(t.split('|')[2]) + "\n"
						"Datum i vreme kraja projekcije:  " + str(t.split('|')[1]) + "   " +str(t.split('|')[3]) + "\n"
						"Sifra projekcije: " + str(t.split('|')[0]))
						print("")
						i = i + 1

			elif odg == '2':
				b = input("Unesite naziv sale: ")

				for t in f.readlines():
					if b.capitalize() == t.split('|')[5]:
						print ("Naziv filma:  " + str(t.split('|')[6]) + "\n"
						"Oznaka sale:  " + str(t.split('|')[5]) + "\n"
						"Datum i vreme pocetka projekcije:  " + str(t.split('|')[1]) + "   " + str(t.split('|')[2]) + "\n"
						"Datum i vreme kraja projekcije:  "+ str(t.split('|')[1]) + "   " +str(t.split('|')[3]) + "\n"
						"Sifra projekcije: " + str(t.split('|')[0]))
						print("")
						i = i + 1

			elif odg == '3':
				vreme1 = input("Unesite vreme pocetka projekcije [hh:mm] :   ")
				vreme2 = input("Unesite vreme kraja projekcije [hh:mm] :   ")
				datum = input("Unesite datum projekcije [dd.mm.gggg.] :  ")

				for t in f.readlines():
					if [vreme1, vreme2, datum] == [t.split('|')[2],t.split('|')[3],t.split('|')[1]]:
						print ("Naziv filma:  " + str(t.split('|')[6]) + "\n"
						"Oznaka sale:  " + str(t.split('|')[5]) + "\n"
						"Datum i vreme pocetka projekcije   :  " + str(datum) + "   " + str(vreme1) + "\n"
						"Datum i vreme kraja projekcije:  " + str(datum) + "   " +str(vreme2) + "\n"
						"Sifra projekcije: " + str(t.split('|')[0]))
						print("")
						i = i + 1
	brojac(i)

''' korisnik bira termin projekcije.
Moze da pogleda prvo termine projekcije
ili da direktno unosom sifre projekcije izabere projekciju'''

def odabir_termina():
	s = ""
	while s not in ['1','2']:
		print("Da li zelite da: ")
		print("1. Pogledate termine projekcija")
		print("2. Unesete sifru zeljene projekcije")
		s = input(" >>>  ")
		print("")
		if s == '1':
			rez = pretraga_projekcija()
		print(" Unesete sifru termina projekcije za film koji zelite kupiti kartu, ")
		print(" ili pritisnite enter da se vratite u glavni meni")
		k = input(">>> ")
		return k


''' Korisnik bira sediste za izabranu projekciju filma koju dobija
Ispisuje slobodna sedista i trazi unos izabranog sedista
Sediste se brise iz fajla sedista za tu projekciju'''

def sediste(termin):
	sif = termin
	fajl = sif + '.txt'
	lista = []
	sed = ''
	try:
		with open(fajl, 'r') as f:
			for l in f.readlines():
				lista = l.split(',')
		print("Slobodna sedista za izabranu projekciju su " + str(lista))
		print("")
		sed= input("Izaberite sediste: ")
		print("")
		try:
			lista.remove(str(sed))
			with open(fajl,'w') as f:
				for a in lista:
					f.write(a + ',')
				return sed
		except ValueError:
			print("Sediste koje ste uneli je zauzeto ili ne postoji")
	except FileNotFoundError:
		print("Ne postoji trazena projekcija\n")


''' Dobija termin projekcije i sediste.
Na osnovu njih pise rezervaciju karte  u fajl karte.'''

def pisanje_rezervacije(termin,sed):
		kupac = ""
		i = 0
		with open('ulogovan.txt', 'r') as f:
			for l in f.readlines():
				a = l.split('|')[4]
				if a == 'kupac\n':
					kupac = l.split('|')[0]
					i = 1
				elif a == 'prodavac\n':
					kupac = input("Unesite korisniko ime kupca: ")

		ime = ""
		prezime = ""
		datum = vreme()
		projekcija = ""

		with open('terminprojekcije.txt', 'r') as f:
			for l in f.readlines():
				if termin == l.split('|')[0]:
					projekcija = l.rstrip()
					break

		with open('korisnici.txt', 'r') as f:
			for l in f.readlines():
				if kupac == l.split('|')[0]:
					ime = l.split('|')[2]
					prezime  = l.split('|')[3]
					i = i + 1
					break

		if i != 0:
			with open('karte.txt', 'a') as f:
				f.write(str(ime) + '|' + str(prezime)  + '|' + str(kupac) + '|' + str(projekcija) + '|' + str(sed) + '|' + str(datum) + '|' + 'R\n')
				print("Karta je rezervisana.")
		else:
			print("Pogresno korisnicko ime kupca.\n")


''' danasnji datum pise u obliku d.m.g
koristi se za prodaju karata da pisemo datum prodaje'''

def vreme():
	a = datetime.date.today()
	datum = str(a.day) + '.' + str(a.month) + '.' + str(a.year) + '.'
	return datum


''' korisnik bira termin karte koju zeli da rezervise
ako je izabrao termin moze da izabere seidste, zatim mu se pise rezervacija
nudi se da nastavi da rezervise karte za istu ili drugu projekciju'''

def rezervacija_karata():
	pro = str(odabir_termina())
	if pro != '':
		sed = sediste(pro)
		if sed != None:
			pisanje_rezervacije(pro,sed)
			print("Da li zelite da rezervisete jos karata")
			print("1. Da")
			print("2. Ne")
			pitanje=input(">>> ")
			print()
			if pitanje == '1':
				print("Da li zelite da rezervisete kartu za:")
				print ("1. Istu projekciju ")
				print("2. Drugu projekciju ")
				odgovor = input(">>> ")
				print()
				if odgovor == '1':
					sed = sediste(pro)
					pisanje_rezervacije(pro,sed)
				elif odgovor == '2':
					rezervacija_karata()
			elif pitanje == '2':
				print("Hvala na rezervacijama")


''' prima dva argumenta, i na osnovu njih ponistava rezervisanu kartu'''

def ponistavanje_rezervacije(termin,sediste):
	lista = []
	with open('karte.txt', 'r') as f:
		for l in f.readlines():
			try:
				if [termin,sediste] != [l.split('|')[3],l.split('|')[11]]:
					lista.append(l)
			except IndexError:
				print()

	with open('karte.txt', 'w') as f:
		for a in lista:
			f.write(a)

	pro= termin + '.txt'
	with open(pro,'a') as f:
		f.write(sediste + ',')
		print("Karta uspesno ponistena")

''' Koristimo je kao brojac u drugim funkcijama da pise greske ako nema rezultata pretrage'''

def brojac(i):
	if i == 0:
		print("Greska prilikom unosa ili nema rezultata pretrage")
		print("")