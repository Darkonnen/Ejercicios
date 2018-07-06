"""
string = "Mi nombre es Aedel Darko"
yoda = reversed(string)
yodaString = ''.join(yoda)

print(yodaString)
"""

string2 = "Mi nombre es Aedel Darko"
string2 = string2.split(' ') # IMPORTATE: split convierte el string en lista
reversed2 = reversed(string2)
reversed2 = ' '.join(reversed2)
print(reversed2)