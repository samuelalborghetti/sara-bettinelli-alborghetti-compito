


































































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
            # Controllo che la data non sia nel futuro
            if data > datetime.now():
                print("Errore: la data di nascita non può essere nel futuro. Riprova.")
                continue
            return data
        except ValueError:
            print("Errore: formato data non valido. Usa GG/MM/AAAA (es. 15/03/1990).")


def calcolaCodiceComune(comune):
    # Dizionario di esempio con alcuni comuni italiani
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