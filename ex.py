from datetime import datetime
#import math
from math import sqrt
#from math import *

def felicitare():
	print("Sa fii sanatos!")

print("Mihalevschi")
my_int = 16
my_float = 6.89043
my_bool = True 
my_string = "Cine știe carte, are patru ochi"
# Schimbare
my_int = 263
my_string = "De fapt, nu intotdeauna..."
#operatii matematice
suma = 3 + 3
diferenta = 10 - 3
inmultirea = 2 * 3
impartirea = 6 / 2
print(int(impartirea))
varsta = 'Are zece ani'
print(varsta)
litera_cinci = "informatica"[5]
print(litera_cinci)
print("litera "+str(70)+" exista?")
print(int("70"))
p = "Programare"
w = "Web"
print("%s    %s" % (w, p))

#Primul este 			not
#Al doilea este 		and
#Al treilea este 		or

print(True or not False and False)

if my_int == int(my_float):
	print("Da!")
elif my_int < int(my_float):
	print("Poate?")
else:
	print("Nu!")

# Important! scriem sus     from datetime import datetime
print(datetime.now())

acum = datetime.now()
anul_curent = acum.year
luna_curenta = acum.month
ziua_curenta = acum.day

print(anul_curent, " ", luna_curenta, " ", ziua_curenta)
print("%s %s %s" % (str(acum.year), str(acum.month), str(acum.day)))
print("%s:%s:%s" % (acum.hour, acum.minute, acum.second))"""

"""felicitare()

def patratul_perfect(n):
	patrat = n ** 2
	print(patrat, "este patratul perfect al lui", n)
	return 0

patratul_perfect(n = 2)

felicitare()

#____________________________________________________________________

def putere(baza, exponent):  # adaugati aici parametrii
    rezultat = baza**exponent
    print("%s la puterea %s este %s." % (baza, exponent, rezultat))

putere(2, 3)

#____________________________________________________________________

def o_afisare (n):
	return n + 1

def merita_alta_afisare(n):
	return o_afisare(n) + 2

print(merita_alta_afisare(3))

#____________________________________________________________________

def cub(numar):
	return numar ** 3

def mai_mare(numar):
	if numar > 100:
		return cub(numar)
	else:
		return False

print(mai_mare(3))

#_____________________________________________________________________

print(sqrt(25))

def shut_down(s):
	if s == "yes":
		return "Shutting down ..."
	elif s == "no":
		return "Shutdown abborted ..."
	else:
		return "Sorry ..."

print(shut_down("my hommies"))

#_____________________________________________________________________

print(sqrt(13689))

#_____________________________________________________________________

numere = [1, 2, 3, 4]
print(numere[1]+numere[2])
zoo_animale = ["urs", "vulpe", "tigru", "elefant"]
zoo_animale[3] = "fenec"
zoo_animale.append("elefant")
print(zoo_animale)

#_____________________________________________________________________

meniu = {
	'Clatite cu ciocolata' : 35.00,
	'Alfabet' : ["a", "b", "c"]
}

meniu['Supa cu ciuperci'] = 40.00
meniu['Pizza cu pepperoni'] = 62.00
meniu['Cheesecake'] = 56.00
meniu['Ramen'] = 70.00

print(meniu)

del meniu['Cheesecake']
print(meniu)
print(meniu['Alfabet'][1])

for i in meniu:
	if meniu[i] = 40.00:
		print("Yes!")

#_____________________________________________________________________

liceu = {
    'elevi' : 500,
    'olimpici' : ['matematica', 'informatica', 'geografie'], # am atribuit o lista la cheia 'olimpici'
    'premii' : ['sport', 'teatru', 'dans', 'pictura']
}

# sortam lista cu cheia 'olimpici'
liceu['olimpici'].sort()

# adaugam o cheie noua 'cursuri' si ii atribuim o lista
liceu['cursuri'] = ['programare', 'antreprenoriat', 'engleza']

print(liceu)

liceu['festivitati'] = ['halloween', 'revelion' , 'ultimul sunet']
liceu['premii'].sort()
liceu['premii'].remove('teatru')

#_____________________________________________________________________