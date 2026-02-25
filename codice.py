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
    controllo=True
    while controllo:
        try:
            dataNascita=input("Inserici la data di nascita del nuovo atleta (formato: gg/mm/aaaa): ")
            giorno, mese, anno = map(int, dataNascita.split('/'))
            if 1 <= giorno <= 31 and 1 <= mese <= 12 and anno > 1900:
                controllo=False
                return dataNascita
            else:
                print("Data di nascita non valida.")
        except:
            print("Errore nell'inserimento dei dati. Riprova.")


def chiediDataNascita():
    while True:
        data_input = input("Inserisci la data di nascita (GG/MM/AAAA): ")
        
        try:
            data = datetime.strptime(data_input, "%d/%m/%Y")
            return data
        
        except ValueError:
            print("Data non valida. Usa il formato GG/MM/AAAA.")


def calcolaCodiceComune() -> str:
    comuni = {
        "ROMA": "H501",
        "MILANO": "F205",
        "TORINO": "L219",
        "NAPOLI": "F839",
        "FIRENZE": "D612"
    }
    
    while True:
        nome_comune = input("Inserisci il comune di nascita: ").strip().upper()
        
        if nome_comune in comuni:
            return comuni[nome_comune]
        else:
            print("Comune non trovato. Riprova.")