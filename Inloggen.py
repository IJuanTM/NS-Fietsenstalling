def inloggen():
    while True:
        naam = input('\n'+'Voornaam: ')
        if naam == 'STOP':
            from NS_Fietsen_Stalling import inlog_menu
            print(inlog_menu())
        ov = input('Laatste 4 cijfers van uw ov: ')
        if ov == 'STOP':
            from NS_Fietsen_Stalling import inlog_menu
            print(inlog_menu())
        wachtwoord = input('Wachtwoord: ')
        if wachtwoord == 'STOP':
            from NS_Fietsen_Stalling import inlog_menu
            print(inlog_menu())
        file = open('Gegevens','r')
        lines = file.readlines()
        for line in lines:
            y = line.strip('\n')
            z = y.split(';')
            if naam == z[0]:
                if ov == z[4]:
                    if wachtwoord == z[2]:
                        file.close()
                        f1 = open('Ingelogd','a')
                        f1.write(line)
                        f1.close()
                        print('\033[32mInlog Succesvol\033[0m\n')
                        return

        print('\033[31mDeze combinatie is incorrect. Ga terug naar menu om te registeren of probeer opnieuw.\033[0m')
        while True:
            reg = input('\033[34mTyp Menu of Opnieuw: \033[0m')
            if reg == 'Menu':
                reg = ''
            if reg == 'Opnieuw':
                break
            else:
                print('Foute input.')