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