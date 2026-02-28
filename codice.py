from datetime import datetime

def rimuoviLettereAccentate(testo):
    testo = testo.replace("à", "a").replace("è", "e").replace("é", "e")
    testo = testo.replace("ì", "i").replace("ò", "o").replace("ù", "u")
    testo = testo.replace("À", "A").replace("È", "E").replace("É", "E")
    testo = testo.replace("Ì", "I").replace("Ò", "O").replace("Ù", "U")
    return testo

def rimuoviSpazi(testo):
    return testo.replace(" ", "")

def chiediCognome():
    while True:
        cognome = input("Inserisci il cognome: ").strip()
        cognome = rimuoviLettereAccentate(cognome)
        cognome = rimuoviSpazi(cognome)
        
        if cognome.isalpha() and len(cognome) > 0:
            return cognome.upper()
        else:
            print("Cognome non valido. Inserisci solo lettere.")

def chiediDataNascita():
    while True:
        data_str = input("Inserisci la data di nascita (GG/MM/AAAA): ").strip()
        try:
            data = datetime.strptime(data_str, "%d/%m/%Y")
            if data > datetime.now():
                print("Errore: la data di nascita non può essere nel futuro. Riprova.")
                continue
            return data
        except ValueError:
            print("Errore: formato data non valido. Usa GG/MM/AAAA (es. 15/03/1990).")

def calcolaCodiceComune(comune):
    CODICI_COMUNI = {
        "ROMA": "H501",
        "MILANO": "F205",
        "NAPOLI": "F839",
        "TORINO": "L219",
        "PALERMO": "G273",
        "GENOVA": "D969",
        "BOLOGNA": "A944",
        "FIRENZE": "D612",
        "BARI": "A662",
        "CATANIA": "C351",
        "VENEZIA": "L736",
        "VERONA": "L781",
        "MESSINA": "F158",
        "PADOVA": "G224",
        "TRIESTE": "L424",
        "BRESCIA": "B157",
        "TARANTO": "L049",
        "PRATO": "G999",
        "REGGIO CALABRIA": "H224",
        "MODENA": "F257",
        "REGGIO EMILIA": "H223",
        "PERUGIA": "G478",
        "RAVENNA": "H199",
        "LIVORNO": "E625",
        "CAGLIARI": "B354",
        "BERGAMO": "A794",
        "STEZZANO": "I951",
        "BREMBATE": "B137",
        "VERDELLINO": "L752",
        "VERDELLO": "L753",
        "DALMINE": "D245",
        "GESSATE": "D995",
        "MOZZO": "F791",
        "CURNO": "D221",
        "TREVIOLO": "L404",
    }

    comune_normalizzato = comune.strip().upper()
    codice = CODICI_COMUNI.get(comune_normalizzato)

    if codice is None:
        raise ValueError(f"Comune '{comune}' non trovato nel database. Verifica il nome o aggiorna il dizionario.")
    return codice

def calcolaCodiceAnno(data_nascita):
    anno = data_nascita.year
    ultime_due_cifre = anno % 100      
    return f"{ultime_due_cifre:02d}"      


def calcolaCodiceCognome(cognome):
    VOCALI = "AEIOU"
    cognome = cognome.upper()

    consonanti = [c for c in cognome if c.isalpha() and c not in VOCALI]
    vocali     = [c for c in cognome if c.isalpha() and c in VOCALI]

    lettere = consonanti + vocali          

    while len(lettere) < 3:
        lettere.append('X')

    risultato = lettere[0] + lettere[1] + lettere[2]
    return risultato

def chiediComune(comuni):
    fine=False
   
    while not fine:
        comune=input('inserisci il comune nel quale sei nato:').lower().strip()
        if comune not in comuni:
            fine=False
        else:
            return comune

def calcolaCodiceMese(data):
    codice_mesi={
        1:'A',
        2:'B',
        3:'C',
        4:'D',
        5:'E',
        6:'H',
        7:'L',
        8:'M',
        9:'P',
        10:'R',
        11:'S',
        12:'T'
    }
    mese=data.month
    if mese not in codice_mesi:
        raise ValueError("mese inesistente")
    else:
        return codice_mesi[mese]

def calcolaCodiceNome(nome):
    consonante=''
    vocale=''
    nome=nome.upper()
    for c in nome:
        if c in "BCDFGHJKLMNPQRSTVWXYZ":
            consonante += c
        elif c in "AEIOU":
            vocale += c
    if len(consonante) >= 4:
       return consonante[0] + consonante[2] + consonante[3]
    cd = (consonante + vocale)[:3]
    while len(cd) < 3:
            cd += "X"
    return cd

comuni=['bergamo','stezzano','brembate','verdellino','verdello','dalmine','gessate','mozzo','curno','treviolo']

def chiediNome() :
    controllo = True
    while controllo:
        nome = input("Inserisci il nome: ").strip()
        if nome.isalpha():
            nome = rimuoviLettereAccentate(nome)
            nome = rimuoviSpazi(nome)
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
    cf += calcolaCodiceCognome(cognome)
    cf += calcolaCodiceNome(nome)
    cf += calcolaCodiceAnno(data_nascita)
    cf += calcolaCodiceMese(data_nascita)
    cf += calcolaCodiceGiorno(data_nascita, sesso)
    cf += calcolaCodiceComune(comune)
    cf += calcolaCodiceControllo(cf)
    return cf

cognome = chiediCognome()
nome = chiediNome()
data_nascita = chiediDataNascita()
sesso = chiediSesso()
comune = chiediComune(comuni)
codice_fiscale = calcolaCodiceFiscale(cognome, nome, data_nascita, sesso, comune)
print("Il tuo codice fiscale è: " + codice_fiscale)
