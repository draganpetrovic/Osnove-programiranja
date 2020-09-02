
import funkcije
import funkcijeKupac
import funkcijeMenadzer
import funkcijeProdavac


# funkcija koju pozivamo u main funkciji, daje nam izbor da se prijavimo ili registrujemo.

def ulaz():
	odg=""
	while odg not in['1','2']:
		odg=input("Izaberite jednu od opcija: \n\
		1. Prijava na sistem \n\
		2. Registracija \n")
		if odg == '1':
			login()
		elif odg == '2':
			registracija()
			

''' kada korisnik izabere da se uloguje u program, pokrece se ova funckija koja trazi unos korisnickog imena i lozinke
funkcija proverava u fajlu korisnici.txt da li su uneti podaci tacni.
Ako jesu upisuje ulogovanog korisnika u dokument ulogovani, i otvara mu meni.'''

def login():
	while True:
		username = input("Unesite korisnicko ime: ")
		password = input("Unesite lozinku: ")
		i = 0
		with open('korisnici.txt', 'r') as f:
			for korisnik in f.readlines():
				if [username, password] == [korisnik.split('|')[0], korisnik.split('|')[1]]:
					print("Dobrodosli ", username + "!")
					print("")
					i = i + 1
					with open('ulogovan.txt', 'w') as u:
						u.write(korisnik)
					meni()
		if i == 0:
			print("Pogresno korisnicko ime ili lozinka.")


''' ako korisnik izabere da se registruje, pokrece se ova funkcija koja trazi unos korisnickog imena, lozinke, imena i prezimena korisnika
funkcija proverava da li korisnicko ime postoji, da li je lozinka duza od 6 karaktera i da li sadrzi cifru x.isdigit()
Ako se uspesno registruje upisujemo u dokument korisnika kao kupca, zatim u dokument ulogovani, na kraju mu otvaramo meni'''

def registracija():
	while True:
		name = input("Unesite korisnicko ime: ")
		passw = input("Unesite lozinku: ")
		ime = input("Unesite vase ime: ")
		prez = input("Unesite vase prezime: ")
		with open('korisnici.txt', 'r') as f:
			for l in f.readlines():
				if name == l.split('|')[0]:
					print("Korisnicko ime vec postoji.")  
		if len(passw) > 6:
			if any (x.isdigit() for x in passw):
				nov = str(name) + '|' + str(passw) + '|' + str(ime) + '|' + str(prez) + '|' + 'kupac\n'
				with open('korisnici.txt', 'a') as r:
					r.write(nov)
				with open('ulogovan.txt', 'w') as g:
					g.write(nov)
				print('Uspesno ste se registrovali ', name + "!")
				print("")
				meni()
			else:
				print("Vasa lozinka mora sadrzati barem jednu cifru.")
		else:
			print("Vasa lozinka mora biti duza od 6 karaktera.")


'''funkcija proverava prvo status ulogovanog korisnika, na osnovu toga da li je kupac, prodavac ili menadzer
stampa mu se meni, zatim se od njega trazi da izabere jednu od ponudjenih opcija
'''

def meni():
	korisnik = provera_korisnika()
	if korisnik == "kupac\n":
		print_kupac()
		kupac_meni()

	elif korisnik == "prodavac\n":
		print_prodavac()
		prodavac_meni()

	elif korisnik == "menadzer\n":
		print_menadzer()
		menadzer_meni()



# Proverava da li je ulogovani korisnik kupac,prodavac ili menadzer

def provera_korisnika():
	with open('ulogovan.txt', 'r') as f:
		for l in f.readlines():
			return l.split('|')[4]


#Trazi se od kupca da izabere jednu opciju u ponudjenom meniju

def kupac_meni():
	opcija = "111"
	while opcija not in ['1', '2', '3', '4', '5', '6', '7']:
		opcija = input("Unesite opciju:")
		print("")
		if opcija == '1':
			funkcije.pregled_filmova()
			print_kupac()
			kupac_meni()
		elif opcija == '2':
			funkcije.pretraga_filmova()
			print_kupac()
			kupac_meni()
		elif opcija == '3':
			funkcije.pretraga_projekcija()
			print_kupac()
			kupac_meni()
		elif opcija == '4':
			funkcije.rezervacija_karata()
			print_kupac()
			kupac_meni()
		elif opcija == '5':
			a = funkcijeKupac.pregled_rezervacijaKupac()
			if a == 0:
				print("Nemate rezervisanih karata.\n")
			print_kupac()
			kupac_meni()
		elif opcija == '6':
			funkcijeKupac.ponistavanje_rezervisanihKupac()
			print_kupac()
			kupac_meni()
		elif opcija == '7':
			print("Uspesno ste odjavljeni.")
			print("")
			main()

#Trazi se od prodavca da izabere jednu opciju u ponudjenom meniju

def prodavac_meni():
	opcija = "111"
	while opcija not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
		opcija = input("Unesite opciju:")
		print("")
		if opcija == '1':
			funkcije.pregled_filmova()
			print_prodavac()
			prodavac_meni()
		elif opcija == '2':
			funkcije.pretraga_filmova()
			print_prodavac()
			prodavac_meni()
		elif opcija == '3':
			funkcije.pretraga_projekcija()
			print_prodavac()
			prodavac_meni()
		elif opcija == '4':
			funkcije.rezervacija_karata()
			print_prodavac()
			prodavac_meni()
		elif opcija == '5':
			a = funkcijeProdavac.pregled_rezervacijaProdavac()
			if a == 0:
				print("Nema rezervisanih karata. \n")
			print_prodavac()
			prodavac_meni()
		elif opcija == '6':
			funkcijeProdavac.ponistavanje_rezervisanihProdavac()
			print_prodavac()
			prodavac_meni()
		elif opcija == '7':
			funkcijeProdavac.pretraga_karata()
			print_prodavac()
			prodavac_meni()
		elif opcija == '8':
			funkcijeProdavac.prodaja_karata()
			print_prodavac()
			prodavac_meni()
		elif opcija == '9':
			print("Uspesno ste odjavljeni.")
			print("")
			main()
		elif opcija == '10':
			print("Dovidjenja!")
			exit()



#Trazi se od menadzera da izabere jednu opciju u ponudjenom meniju

def menadzer_meni():
	opcija = "111"
	while opcija not in ['1', '2', '3', '4', '5', '6', '7', '8']:
		opcija = input("Unesite opciju:")
		print("")
		if opcija == '1':
			funkcije.pregled_filmova()
			print_menadzer()
			menadzer_meni()
		elif opcija == '2':
			funkcije.pretraga_filmova()
			print_menadzer()
			menadzer_meni()
		elif opcija == '3':
			funkcije.pretraga_projekcija()
			print_menadzer()
			menadzer_meni()
		elif opcija == '4':
			funkcijeMenadzer.ubi_entiteta()
			print_menadzer()
			menadzer_meni()
		elif opcija == '5':
			funkcijeMenadzer.registracija_prodavaca()
			print_menadzer()
			menadzer_meni()
		elif opcija == '6':
			funkcijeMenadzer.izvestavanje()
			print_menadzer()
			menadzer_meni()
		elif opcija == '7':
			print("Uspesno ste odjavljeni.")
			print("")
			main()
		elif opcija == '8':
			print("Dovidjenja!")
			exit()


#Stampa izbor opcija u meniju za kupca.

def print_kupac():
	print("1. Pregled dostupnih filmova")
	print("2. Pretraga filmova")
	print("3. Pretraga projekcija")
	print("4. Rezervacija karata")
	print("5. Pregled rezervisanih karata")
	print("6. Ponistavanje rezervacija karata")
	print("7. Odjava sa naloga")


#Stampa izbor opcija u meniju za prodavca.

def print_prodavac():
	print("1. Pregled dostupnih filmova")
	print("2. Pretraga filmova")
	print("3. Pretraga projekcija")
	print("4. Rezervacija karata")
	print("5. Pregled rezervisanih karata")
	print("6. Ponistavanje rezervacija karata")
	print("7. Pretraga karata")
	print("8. Prodaja karata")
	print("9. Odjava sa naloga")
	print("10. Zatvorite program")


#Stampa izbor opcija u meniju za menadzera.

def print_menadzer():
	print("1. Pregled dostupnih filmova")
	print("2. Pretraga filmova")
	print("3. Pretraga projekcija")
	print("4. Unos, brisanje ili izmena entiteta")
	print("5. Registracija novih prodavaca")
	print("6. Izvestaji")
	print("7. Odjava sa naloga")
	print("8. Zatvorite program")


# Pocetak programa. Poziva se funkcija koja daje izbor da se ulogujete ili registrujete.

def main():
	ulaz()

main()