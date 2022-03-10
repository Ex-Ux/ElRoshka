log = 'Turik'
pas = 'Tur'

bol = False
cehd = 0

while bol != True:

	if cehd == 3:
		print()
		print('	Cehd sayi limiti kechdi!')
		print()
		break
	cehd += 1

	login = input('Login: ')
	logPas = input('Password: ')

	print()
	print('	cehd sayi: ' , cehd)

	
	if login.lower() != log.lower() and logPas != pas:
		print()
		print('	Login ve Parol sehvdir!')
		print()

	elif login.lower() != log.lower():
		print()
		print("	Login sehvdir!")
		print()

	elif logPas != pas:
		print()
		print("	Parol sehvdir")
		print()

	elif login.lower() == log.lower() and logPas == pas:
		print()
		print('	Xosh geldiniz ' + log+ '!' )
		print()
		bol = True

	else:
		print("	Error verdi!")


