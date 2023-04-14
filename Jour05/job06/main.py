def arrondir_notes(notes):
    notes_arrondies = []
    for n in notes:
        if n < 40:
            notes_arrondies.append(n)
        else:
            multiple_de_5 = n // 5 * 5 + 5
            if multiple_de_5 - n< 3:
                notes_arrondies.append(multiple_de_5)
            else:
                notes_arrondies.append(n)
    print(notes_arrondies)


notes = [67, 43, 45, 99, 23]

arrondir_notes(notes)
