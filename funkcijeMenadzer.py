import funkcije
import datetime
import time
import os


''' Funkcija za unos brisanje i izmenu entiteta.
Trazi se izbor entiteta i salje dalje na ostale odgovarajuce funkcije'''

def ubi_entiteta():
	opcija = ""
	while opcija not in ['1', '2', '3', '4']:
		print('1. Bioskopska projekcija')
		print('2. Sala za projekcije')
		print('3. Film')
		print('4. Termin projekcije')
		opcija = input("Izaberite entitet: \n")
		if opcija == '1':
			bioskopskaProjekcija()
		elif opcija == '2':
			salaProjekcije()
		elif opcija == '3':
			film_ubi()
		elif opcija == '4':
			terminProjekcije()

''' Trazi se izbor da menadzer odluci da li zeli da dodaje, brise
ili izmeni postojecu projekciju. Poziva dalje odgovarajuce funkcije.'''

def bioskopskaProjekcija():
	odg = ''
	while odg not in ['1', '2', '3']:
		print('1. Dodati bioskopsku projekciju. ')
		print('2. Brisanje projekcije. ')
		print('3. Izmena postojece projekcije.')
		odg = input('Izaberite operaciju: \n')
		if odg == '1':
			novaProjekcija()
		elif odg == '2':
			obrisiProjekciju()
		elif odg == '3':
			izmeniProjekciju()

''' Trazi se izbor da menadzer odluci da li zeli da dodaje, brise
ili izmeni postojecu salu za projekcije. Poziva dalje odgovarajuce funkcije.'''

def salaProjekcije():
	odg = ''
	while odg not in ['1', '2', '3']:
		print('1. Dodati bioskopsku salu. ')
		print('2. Brisanje sale za projekcije. ')
		print('3. Izmena sale za projekcije.')
		odg = input('Izaberite operaciju: \n')
		if odg == '1':
			novaSala()
		elif odg == '2':
			obrisiSalu()
		elif odg == '3':
			izmeniSalu()

''' Trazi se izbor da menadzer odluci da li zeli da dodaje, brise
ili izmeni postojeci film. Poziva dalje odgovarajuce funkcije.'''

def film_ubi():
	odg = ''
	while odg not in ['1', '2', '3']:
		print('1. Dodati novi film. ')
		print('2. Brisanje postojeceg filma. ')
		print('3. Izmena filma.')
		odg = input('Izaberite operaciju: \n')
		if odg == '1':
			novFilm()
		elif odg == '2':
			obrisiFilm()
		elif odg == '3':
			izmeniFilm()

''' Trazi se izbor da menadzer odluci da li zeli da dodaje, brise
ili izmeni postojeci termin projekcije. Poziva dalje odgovarajuce funkcije.'''

def terminProjekcije():	
	odg = ''
	while odg not in ['1', '2', '3']:
		print('1. Dodati termin projekcije. ')
		print('2. Brisanje termina projekcije. ')
		print('3. Izmena termina projekcije.')
		odg = input('Izaberite operaciju: \n')
		if odg == '1':
			novTermin()
		elif odg == '2':
			obrisiTermin()
		elif odg == '3':
			izmeniTermin()








''' Trazi se unos oznake sale, koja se kao argument daje drugoj funkciji.
Ako ta funkcija vrati vrednost True, imamo ispis da je nova sala dodata'''


def novaSala():
	sifra = input(" Unesite sifru sale: \n")
	s = dodajeSalu(sifra)
	if s == True:
		print(" Nova sala za projekcije je dodata! \n")


''' Sifra se proverava da li je velicine 3 znaka.
Ako nije dobija se ispis da mora biti odredjene velicine.
Trazi se unos broja redova i oznaka sedista. Zatim se nova sala appenduje u tekstualni fajl salezaprojekcije. '''

def dodajeSalu(sifra):
	if len(sifra) == 3:
		red = input("Unesite broj redova(numeracija 1,2,3...)")
		kol = input("Oznaku sedista u svakom redu (numeracija A,B,C...)")
		with open('salezaprojekcije.txt', 'a') as f:
			l = sifra.capitalize() + '|' + red + '|' + kol + '\n'
			f.write(l)
			return True
	else:
		print("Sifra sale mora biti u obliku troslovne oznake\n")
		return False

''' Trazi se unos oznake sale, koja se kao argument daje drugoj funkciji.
Ako ta funkcija vrati vrednost True, imamo ispis da je sala obrisana'''

def obrisiSalu():
	sifra = input("Unesite sifru sale koju zelite obrisati: \n")
	a = briseSalu(sifra)
	if a == True:
		print("Sala uspesno obrisana. \n")


'''funkcija koja brise salu. dobija oznaku sale kao argument.
Sve sale se citaju iz fajla i upisuju u listu osim one ciju smo sifru uneli.
Uz pomoc brojaca 'i' proveravamo da li trazena sala postoji. Ako postoji sve sale iz liste se upisuju u fajl'''

def briseSalu(sifra):
	sale = []
	i = 0
	with open('salezaprojekcije.txt', 'r') as f:	
		for l in f.readlines():
			if l.split('|')[0] == sifra.capitalize():
				i = 1
			elif l.split('|')[0] != sifra.capitalize():
				sale.append(l)
	with open('salezaprojekcije.txt', 'w') as f:		
		if i == 0:
			print(" Ne postoji sala. \n")
			return False
		else:
			for a in sale:
				f.write(a)
			return True


''' Unosimo oznaku sale koju zelimo obrisati. Uz pomoc funkcije briseSalu() koju vec imamo mozemo obrisati salu,
zatim uz pomoc funkcije dodajeSalu() mozemo uneti nove podatke za salu sto ce izgledati kao da smo izmenili postojecu. '''

def izmeniSalu():
	naziv = input("Unesite sifru sale koju zelite izmeniti: ")
	if len(naziv) == 3:
		b = briseSalu(naziv)
		if b == True:
			dodajeSalu(naziv)
			print("Izmena izvrsena\n")


''' Trazi se unos naziva filma, koji se kao argument daje drugoj funkciji.
Ako ta funkcija vrati vrednost True, imamo ispis da je nov film  dodat'''

def novFilm():
	naziv = input("Unesite naziv filma: \n")
	dodajeFilm(naziv)
	print(" Dodali ste novi film.")

''' Funkcija sluzi za upisivanje novog filma u tekstualni fajl filmovi.
Zahteva unos svih podataka o filmu osim naziva koji dobija kao argument'''

def dodajeFilm(naziv):
	zanr = input("Zanr filma: \n")
	vreme = input("Trajanje u minutima: \n")
	reziser = input(" Rezisera: \n")
	uloge = input("Glavne uloge: \n")
	zemlja = input("Zemlju porekla: \n")
	god = input("Godinu proizvodnje: \n")
	opis = input("Skraceni opis filma: \n")
	with open('filmovi.txt', 'a') as f:
		l = (naziv + '|' + zanr + '|' + vreme + '|' + reziser + '|' + uloge + '|' + zemlja + '|' + god + '|' + opis + '\n')
		f.write(l)

''' Trazi se unos naziva filma, koji se kao argument daje drugoj funkciji.
Ako ta funkcija vrati vrednost True, imamo ispis da je film obrisan '''


def obrisiFilm():
	naziv = input("Unesite naziv filma koji zelite obrisati: ")
	b = briseFilm(naziv)
	if b == True:
		print("Film je obrisan.")

'''Funkcija koja brise film. Svi filmovi se citaju iz fajla i upisuju u listu
osim onog ciju smo naziv uneli. Uz pomoc brojaca 'i' proveravamo da li trazen film postoji.
Ako postoji svi filmovie iz liste se upisuju u fajl'''


def briseFilm(naziv):
	filmovi = []
	i = 0
	with open('filmovi.txt', 'r') as f:
		for l in f.readlines():
			if ''.join((l.split('|')[0]).split()).lower() == ''.join(naziv.split()).lower():
				i = 1
			elif ''.join((l.split('|')[0]).split()).lower() != ''.join(naziv.split()).lower():
				filmovi.append(l)
	with open('filmovi.txt', 'w') as f:
		if i == 0:
			print("Film ne postoji.")
			return False
		else:
			for a in filmovi:
				f.write(a)
			return True

''' Trazi se unos filma. Naziv filma se kao argument prosledjuje funkciji briseFilm(),
ako ta funkcija vrati True vrednost, onda se poziva funkcija dodajeFilm koja upisuje izmenjene
podatke o filmu koji zelimo izmeniti'''

def izmeniFilm():
	naziv = input("Unesite ime filma koji zelite izmeniti: ")
	b = briseFilm(naziv)
	if b == True:
		dodajeFilm(naziv)
		print("Izmena izvrsena.\n")


#Sluzi za pozivanje funkcije koja dodaje novu bioskopsku projekciju

def novaProjekcija():
	sifra = input("Unesite sifru projekcije koji zelite dodati: ")
	p = dodajeProjekciju(sifra)
	if p == True:
		print("Dodali ste novu projekciju.")


#Poziva funkciju koja brise bioskopsku projekciju.

def obrisiProjekciju():
	sifra = input("Unesite sifru projekcije koju zelite obrisati: ")
	p = briseProjekciju(sifra)
	if p == True:
		print("Obrisali ste projekciju.")

#Proverava duzinu sifre koja mora imati 4 znaka. Unose se podatci o filmskoj projekciji i ona se dodaje u txt fajl

def dodajeProjekciju(sifra):
	if len(sifra) == 4:
		naziv = input("Unesite naziv filma: ")
		sala = input("Sala: ")
		vreme1 = input("Vreme pocetka projekcije: ")
		vreme2 = input("vreme kraja projekcije: ")
		dan = input("Kojim danima se prikazuje film (Ponedeljak,Utorak...): ")
		with open('bioskopskaprojekcija.txt', 'a') as f:
			p = (sifra + '|' + sala + '|' + vreme1  + '|' + vreme2 + '|' + dan + '|' + naziv + '|' + "300")
			f.write(p)
			return True
	else:
		print("Sifra projekcije mora biti u obliku cetvorocifrenog broja")
		return False

#Sve projekcije se upisuju u listu osim one koju zelimo obrisati,
# zatim se upisuju nazad iz lista i tako eliminisemo projekciju koju smo zeleli obrisati

def briseProjekciju(sifra):
	if len(sifra) == 4:
		projekcije = []
		i = 0
		with open('bioskopskaprojekcija.txt', 'r') as f:
			for l in f.readlines():
				if sifra == l.split('|')[0]:
					i = 1
				elif sifra != l.split('|')[0]:
					projekcije.append(l)
		if i == 0:
			print("Projekcija ne postoji.")
			return False
		else:
			with open('bioskopskaprojekcija.txt', 'w') as f:
				for p in projekcije:
					f.write(p)
				return True
	else:
		print("Sifra projekcije mora biti u obliku cetvorocifrenog broja")
		return False

''' funkcija koja sluzi za izmenu podataka o zeljenoj projekciji. isto funkcionise
kao i funkcije za izmenu filma, sale itd'''

def izmeniProjekciju():
	sifra = input("Unesite sifru projekcije koju zelite izmeniti: ")
	b = briseProjekciju(sifra)
	if b == True:
		dodajeProjekciju(sifra)
		print("Izmena izvrsena.\n")

#Zahteva unos sifre projekcije i dan projekcije. Spaja sifru sa prva dva slova dana

def novTermin():
	pro = input("Unesite sifru projekcije filma: ")
	dan = input("Unesite dan projekcije: ")
	dan = dan.upper()
	sifra = pro + dan[:2]
	t = dodajeTermin(sifra)
	if t == True:
		print("Uneli ste nov termin projekcije\n")

#

def dodajeTermin(sifra):
	if len(sifra) == 6 and sifra[-2:]in ['PO','UT','SR','CE','PE','SU','NE']:
		datum = input("Datum termina: ")
		vreme1 = input("Vreme pocetka projekcije: ")
		vreme2 = input("Vreme kraja projekcije: ")
		dan = input("Dan projekcije: ")
		sala = input("Sala odrzavanja projekcije: ")
		film = input("Film koji se prikazuje: ")
		with open('terminprojekcije.txt', 'a') as f:
			t = (sifra + '|' + datum + '|' + vreme1 + '|' + vreme2 + '|' + dan + '|' + sala + '|' + film + '|' + "300")
			f.write(t)
			open(sifra + '.txt', 'a').close()
		return True
	else:
		print("Pogresan unos.\n")
		return False



def obrisiTermin():
	sifra = input("Unesite sifru termina projekcije koji zelite obrisati: ")
	b = briseTermin(sifra)
	if b == True:
		print("Uneti termin projekcije je obrisan.\n")



def briseTermin(sifra):
	if len(sifra) == 6:
		termin = []
		i = 0
		with open('terminprojekcije.txt', 'r') as f:
			for l in f.readlines():
				if sifra.upper() == l.split('|')[0]:
					i = 1
				elif sifra != l.split('|')[0]:
					termin.append(l)
		if i == 0:
			print("Termin ne postoji.\n")
			return False
		else:
			with open('terminprojekcije.txt', 'w') as f:
				for t in termin:
					f.write(t)
				return True
	else:
		print("Sifra termina mora biti u obliku cetiri broja i dva slova koja oznacavaju dan projekcije\n")
		return False



def izmeniTermin():
	sifra = input("Unesite sifru termina projekcije koju zelite da izmenite: ")
	t = briseTermin(sifra)
	if t == True:
		dodajeTermin(sifra)
		print("Izmena izvrsena. \n")



'''Menadzer registruje nogov prodavca ili menadzera. 
Proverava ista pravila kao kada se registruje nov kupac.'''

def registracija_prodavaca():
	print("Unesite podatke za novog menadzera/prodavca>>>  ")
	print("")
	while True:
		username = input('Korisnicko ime:  ')
		lozinka = input('Lozinka:  ')
		ime = input('Ime:  ')
		prezime= input('Prezime:   ')
		uloga= input('Da li je ovo nov prodavac ili menadzer ?   >>>    ')
		with open('korisnici.txt', 'r') as f:
			for l in f.readlines():
				if username == l.split('|')[0]:
					print("Korisnicko ime vec postoji.")  
		if len(lozinka) > 6:
			if any (x.isdigit() for x in lozinka):
				with open('korisnici.txt', 'a') as f:
					f.write(username + '|' + lozinka + '|' + ime + '|' + prezime + '|' + uloga + '\n')
			else:
				print("Lozinka mora sadrzati barem jednu cifru.")
		else:
			print("Lozinka mora biti duza od 6 karaktera.")

''' Menadzeru se stampaju moguce opcije izvestaja.
Trazi se unos dokle god ne izabere jednu od ponudjenih opcija
Svaki uslov trazi unos podatka za pretragu i poziva odgovarajuce funkcije koje nalaze
odgovarajuce rezultate i stampaju u tabeli iste. '''

def izvestavanje():
	odg = ''
	while odg not in ['1', '2', '3', '4', '5', '6', '7', '8']:
		odg = input("1. Lista prodatih karata za odabran datum prodaje.\n\
			2. Lista prodatih karata za odabran datum početka termina projekcije.\n\
			3. Lista prodatih karata za odabran datum prodaje i odabranog prodavca.\n\
			4. Ukupan broj i ukupna cena prodatih karata za izabran dan prodaje.\n\
			5. Ukupan broj i ukupna cena prodatih karata za izabran dan održavanja projekcije.\n\
			6. Ukupna cena prodatih karata za zadati film u svim projekcijama.\n\
			7. Ukupan broj i ukupna cena prodatih karata za izabran dan prodaje i odabranog prodavca.\n\
			8. Ukupan broj i ukupna cena prodatih karata po prodavcima (za svakog prodavca) u poslednjih 30 dana.\n\
			Izaberite izvestaj koji zelite:   ")
		if odg == '1':
			dprodaje = input("Unesite datum prodaje:  ")
			s = nadjiDprodaje(dprodaje,None)
			petljaIzvestajlista(s)

		elif odg == '2':
			dprojekcije = input("Unesite datum pocetka projekcije: ")
			s = nadjiDprojekcije(dprojekcije)
			petljaIzvestajlista(s)

		elif odg == '3':
			dprodaje = input("Unesite datum prodaje:  ")
			prodavac = input("Unesite ime prodavca: ")
			s = nadjiDprodaje(dprodaje,prodavac)
			petljaIzvestajlista(s)

		elif odg == '4':
			dprodaje = input("Unesite datum prodaje: ")
			s = nadjiDprodaje(dprodaje,None)
			petljaIzvestajcena(s)

		elif odg == '5':
			dprojekcije = input("Unesite datum pocetka projekcije: ")
			s = nadjiDprojekcije(dprojekcije)
			petljaIzvestajcena(s)


		elif odg == '6':
			film = input("Unesite film: ")
			s = nadjiFilm(film)
			if s == None:
				print("Nema rezultata pretrage.")
			else:
				ukupno = s * 300
				print(" | Ukupna cena |")
				print(" +-------------+")						# mala tabela, upisujemo ukupnu cenu karata prodate za unesen film.
				print(" | " + str(ukupno))

		elif odg == '7':
			dprodaje = input("Unesite datum prodaje:  ")
			prodavac = input("Unesite ime prodavca: ")
			s = nadjiDprodaje(dprodaje,prodavac)
			petljaIzvestajcena(s)

		elif odg == '8':
			r = osmiIzvestaj()

	print()
	print()
	print()
	print()


''' Cita prodate karte iz fajla.
Kartu salje funkciji koja kartu formira u obliku recnika
zatim je upisuje u globalnu varijablu(listu)'''

def ucitavanje_karata():
	for line in open('karte.txt', 'r').readlines():
		if len(line) > 1 and line.split('|')[13] == 'P':
			kar = str2karta(line)
			listakarte.append(kar)


''' Prima liniju iz fajla karte.
Upisuje elemente karte u recnik'''

def str2karta(line):
	if line[-1] == '\n':
		line = line[:-1]
	ime, prezime, korime, sifra, dprojekcije, vreme1, vreme2, dan, sala, film, cena, sediste, dprodaje, status, prodavac = line.split('|')
	kar = {
	'ime' : ime,
	'prezime': prezime,
	'korime' : korime,
	'sifra': sifra,
	'dprojekcije' : dprojekcije,
	'vreme1' : vreme1,
	'vreme2' : vreme2,
	'dan' : dan,
	'sala' : sala,
	'film' : film,
	'cena' : cena,
	'sediste' : sediste,
	'dprodaje': dprodaje,
	'status' : status,
	'prodavac' : prodavac
	}
	return kar

''' Pretraga karata po datumu projekcije
Vraca listu karata koje zadovoljavaju uslove.'''

def nadjiDprojekcije(dprojekcije):
	i = 0
	lista = []
	for kar in listakarte:
		if kar['dprojekcije'] == dprojekcije:
			lista.append(kar)
			i = i + 1

	if i == 0:
		return None
	else:
		return lista

''' Pretraga karata po datumu prodaje i prodavcima.
Ako za prodavca ne dobijemo vrednost tada se pretraga vrsi samo po datumu prodaje'''

def nadjiDprodaje(dprodaje,prodavac):
	i = 0
	lista = []
	if prodavac == None:
		for kar in listakarte:
			if kar['dprodaje'] == dprodaje:
				lista.append(kar)
				i = i + 1
	else:
		for kar in listakarte:
			if kar['dprodaje'] == dprodaje and kar['prodavac'].lower() == prodavac.lower():
				lista.append(kar)
				i = i + 1

	if i == 0:
		return None
	else:
		return lista
	
''' Kao parametar dobija film.
Trazi ga u recniku karata.
Broji koliko je karata prodato za trazeni film i vraca broj karata'''

def nadjiFilm(film):
	i = 0
	for kar in listakarte:
		if kar['film'] == film:
			i = i + 1
	if i == 0:
		return None
	else:
		return i

''' Tabela koja sluzi za stampanje liste karata'''

def tablaHeader():
	return \
	"Ime       | Prezime    | Film                               | Datum     | Vreme   | Sala | Sediste | Cena | Prodata dana | Prodavac \n"\
	"----------+------------+------------------------------------+-----------+---------+------+---------+------+--------------+----------"

''' Formatira karte za stampanje u tabeli'''

def formatKarte(kar):
	return "{0:10}|{1:12}|{2:36}|{3:11}|{4:9}|{5:6}|{6:9}|{7:6}|{8:14}|{9:10}".format(
		kar['ime'],
		kar['prezime'],
		kar['film'],
		kar['dprojekcije'],
		kar['vreme1'],
		kar['sala'],
		kar['sediste'],
		kar['cena'],
		kar['dprodaje'],
		kar['prodavac'])

''' Tabela koja se stampa kada racunamo broj karata i ukupnu cenu karata
za odabran dan prodaje, projekije ... '''

def malaTabla():
	return\
	"Broj karata | Ukupna cena \n"\
	"------------+------------"

''' Stampa se tabela za listu karata, i stampaju se karte
koje su zadovoljile uslove pretrage'''

def petljaIzvestaj(s):
	if s == None:
		print("Nema rezultata pretrage.")
	else:
		print(tablaHeader())
		for i in s:
			print(formatKarte(i))

''' Funkcija koja broji karte i mnozi ih sa cenom karata .
Dobijamo broj karata i ukupnu cenu karata koji se stampaju u tabeli'''

def petljaIzvestajcena(s):
	if s == None:
		print("Nema rezultata pretrage.")
	else:
		print(malaTabla())
		broj = len(s)
		ukupno = broj * 300
		print("  " + str(len(s)) + "            " + str(ukupno))

''' Sluzi da vrati datum 30 dana ili 1 mesec unazad od danasnjeg dana.
Uzima se danasnji datum, formatira se u oblik d.m.g.
Pretvaramo ga u string. Ako je prvi mesec pisemo da je dvanaesti i oduziammo jednu godinu.
Ako ne zadovoljava taj uslov oduzimamo samo od meseca 1. Vracamo datum u obliku stringa.'''

def datum30():
	a = datetime.datetime.today()
	pre = ''
	if a.month - 1 == 0:
		pre = str(a.day) + '.' + '12' + '.' + str(a.year - 1) + '.'
	else:
		pre = str(a.day) + '.' + str(a.month - 1) + '.' + str(a.year) + '.'
	return pre

''' Brute force funkcija
stampa tabelu za svakog prodavca posebno koliko je prodao karti i koja je ukupna cena'''


def osmiIzvestaj():
	datum = datum30()
	myformat = '%d.%m.%Y.'
	datum1 = datetime.datetime.strptime(datum, myformat)
	datum2 = ''
	lista1 = []
	lista2 = []

	for kar in listakarte:
		datum2 = kar['dprodaje']
		if datetime.datetime.strptime(datum2, myformat) > datum1:      # poredi datume prodatih karata sa danasnjim datumom koji je smanjen za jedan mesec
			lista1.append(kar)

	for a in lista1:
		prodavac = a['prodavac']
		if lista2 == None:
			lista2.append(prodavac)
			lista2.append(1)						#Ako je lista prazna dodajemo prvog prodavca, i belezimo mu prvu kartu.

		j = 0	
		dodato= False
		while j < len(lista2):						# Dok je duzina liste veca od j 
			if lista2[j]==prodavac:					# Ako je j clan liste jednak prodavcu ( pronalazi prodavca)	
				lista2[j+1]=lista2[j+1]+1			# Naredni clan liste se povecava za 1 (dodeljuje prodavcu jednu kartu)
				dodato = True
			j=j+2									#povecava za 2 i tako u listi prelazimo na sledeceg prodavca

		if dodato == False:
			lista2.append(prodavac)					# Dodavanje novog prodavaca u listu prvi put, i belezenje prve karte
			lista2.append(1)


		
	pro = lista2[0::2]
	broj = lista2[1::2]
	novalista1 = pro
	novalista2 = broj
	if not novalista1:
		print("Nema rezultata pregrage.")
	else:
		print("|Prodavac | Broj karata| Zarada |")
		print("----------+------------+--------+")
		for (n,m) in zip(novalista1,novalista2):
			ukupno = m * 300
			print("{0:10}|{1:12}|{2:8}".format(str(n),str(m),str(ukupno)))


listakarte = []  								#globalna varijabla koja sadrzi listu svih karata 
ucitavanje_karata()  							# ucitavanje karata u globalnu varijablu