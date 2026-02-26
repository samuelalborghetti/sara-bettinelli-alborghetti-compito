from datetime import date
def rimuoviLettereAccentate(parola):
    parola_nuova= parola.replace('à','a').replace('ò','o').replace('ù','u').replace('è','e').replace('é','e').replace('ì','i').replace('ñ','n').replace('ö','o').replace('Ö','o').replace('Ä','a').replace('ä','a')
    return parola_nuova
def chiediComune(comuni):
    fine=False
   
    while not fine:
        comune=input('inserisci il comune nel quale sei nato:').lower()
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
def rimuoviSpazi(elemento):
    elemento=elemento.replace(" ","")
    return elemento
        
    

   
   
 
comuni=['bergamo','stezzano','brembate','verdellino','verdello']
