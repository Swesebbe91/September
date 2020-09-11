#funktion 5
def search_forletters (phrase:str, letters:str='aeiou') -> set: #Om inte "letters fylls i funktionen används AEIOU
    """return a set of letters found in phrase""" #beskriver vad funktionen gör
    return set(letters).intersection(set(phrase)) #Skapa en set av phrase/letter och jämför samma bokstäver
print(search_forletters(input('Ord 1: '), input('Ord2 '))) #Skriv ut string som ska jämföras för "set" A + B
# print(search_forletters('Hejsan'))