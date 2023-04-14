def quefaire():

    while True :
        quoi = input(''' Bonjour, que voulez vous faire?
                * Ajouter un code : tapez A
                * Consulter les codes : tapez C
                * Rien : Tapez R :        ''')
        
        if quoi == "A" :
            print("A")
            break
        elif quoi == "C" :
            print("C")
            break
        elif quoi== "R" :
            print("Merci de votre visite et à bientôt")
            break
        
        else:
            print("Merci d'indiquer un A, C ou R")


quefaire()






with open('mdp_cryptes.json', 'r') as file:
    data = json.load(file)

    if 'code_final' not in data:
        data['code_final'] = [code_final]
    else:
        data['code_final'].append(code_final)
        

                            # Écrire les données mises à jour dans le fichier
    with open('mdp_cryptes.json', 'w') as file:
        json.dump(data, file)