from datetime import datetime, timedelta, date
import random
import os

print("                                 _               ____  _____ ____  _____ _     ")
print("  __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __  |  _ \| ____/ ___|| ____| |    ")
print(" / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__| | |_) |  _| \___ \|  _| | |    ")
print("| (_| |  __/ | | |  __/ | | (_| | || (_) | |    |  __/| |___ ___) | |___| |___ ")
print(" \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|    |_|   |_____|____/|_____|_____|")
print(" |___/\n\n")
# Generated on http://www.network-science.de/ascii/ (font: standard)

# Generuje losową datę urodzenia z zakresu 1900-01-01 do dnia dzisiejszego
start_date = date(1900, 1, 1).toordinal()
end_date = date.today().toordinal()
random_date = date.fromordinal(random.randint(start_date, end_date))
data = int(random_date.strftime('%Y%m%d'))
data = list(map(int, str(data)))
if int(data[0]) == 2:   # Zmaina wartości miesiaca dla urodzonych po 1999 roku
    data[4] = data[4] + 2

# Zapisanie daty do numeru PESEL
pesel = data[2:]

# Dodanie 4 kolejnych cyfr
while len(pesel) < 10:
    pesel.append(random.randint(0, 9))

# Obliczenie sumy kontrolnej i dodanie jej do numeru PESEL
suma_kontrolna = (9*pesel[0]+7*pesel[1]+3*pesel[2]+pesel[3]+9*pesel[4]+7*pesel[5]+3*pesel[6]+pesel[7]+9*pesel[8]
                  + 7*pesel[9]) % 10
pesel.append(suma_kontrolna)
pesel = ''.join(map(str, pesel))

print("Wygenerowany numer PESEL to (numer został skopiowany do schowka): \n{}".format(pesel))
os.system("echo '%s' | clip" % pesel)
