def chiediNome() :
    controllo = True
    while controllo:
        nome = input("Inserisci il nome: ").strip()
        if nome.isalpha():
            #nome = rimuoviLettereAccentate(nome)
            #nome = rimuoviSpazi(nome)
            return nome
        else:
            print("Nome non valido. Inserisci solo lettere.")
   
def chiediSesso() :
    controllo = True
    while controllo:
        sesso = input("Inserisci il sesso (m/f): ").strip().lower()
        if sesso in ['m', 'maschio', 'uomo']:
            return 'm'
        elif sesso in ['f', 'femmina', 'donna']:
            return 'f'
        print(" Valore non valido. Inserisci 'm' per maschio o 'f' per femmina.")

def calcolaCodiceGiorno(data_nascita, sesso):
    giorno = data_nascita.day
    if sesso == 'f':
        giorno += 40
    if giorno < 10:
        return "0" + str(giorno)
    else:
        return str(giorno)


def calcolaCodiceControllo(cf_parziale):
    valori_dispari = {
        '0':1,  '1':0,  '2':5,  '3':7,  '4':9,  '5':13, '6':15, '7':17, '8':19, '9':21,
        'A':1,  'B':0,  'C':5,  'D':7,  'E':9,  'F':13, 'G':15, 'H':17, 'I':19, 'J':21,
        'K':2,  'L':4,  'M':18, 'N':20, 'O':11, 'P':3,  'Q':6,  'R':8,  'S':12, 'T':14,
        'U':16, 'V':10, 'W':22, 'X':25, 'Y':24, 'Z':23
    }
    lettere = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
               'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    cf_parziale = cf_parziale.upper()
    somma = 0
    posizione = 1
    for carattere in cf_parziale:
        if posizione % 2 == 1:
            somma += valori_dispari[carattere]
        else:
            if carattere.isdigit():
                somma += int(carattere)
            else:
                somma += lettere.index(carattere)
        posizione += 1
    return lettere[somma % 26]


def calcolaCodiceFiscale(cognome, nome, data_nascita, sesso, comune):
    cf = ""
    #cf += calcolaCodiceCognome(cognome)
    #cf += calcolaCodiceNome(nome)
    #cf += calcolaCodiceAnno(data_nascita)
    #cf += calcolaCodiceMese(data_nascita)
    #cf += calcolaCodiceGiorno(data_nascita, sesso)
    #cf += calcolaCodiceComune(comune)
    #cf += calcolaCodiceControllo(cf)
    return cf