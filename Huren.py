import time
def fiets_huren():
    vnaam = input('d')
    checkhuur = 0
    file = open('Huurgegevens', 'r')
    lines = file.readlines()

    for line in lines:
        x = line.split(';')
        if checkhuur == 0:
            if vnaam in x:
                print('U heeft al een fiets gehuurd')
                checkhuur = 1
    if checkhuur == 0:
        tijdH = time.strftime('%H')  # uren
        tijdM = time.strftime('%M')  # minuten
        tijdS = time.strftime('%S')  # seconden
        datumd = time.strftime('%d')  # dag
        datumm = time.strftime('%m')  # maand
        datumY = time.strftime('%Y')  # jaar
        tijddatum = tijdH + ':' + tijdM + ':' + tijdS + ' ' + datumd + '/' + datumm + '/' + datumY
        print('De fiets is gehuurd vanaf', tijddatum)
        huurfile = open('Huurgegevens', 'a')
        huurfile.write(vnaam + ';' + str(tijdH) + ';' + str(tijdM) + ';' + str(tijdS) + ';' + str(datumd) + ';' + str(datumm) + ';' + str(datumY) + '\n')
    huurfile.close()


fiets_huren()