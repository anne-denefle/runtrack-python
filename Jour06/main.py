
import re
import hashlib
import json
import os






def quefaire():

    while True :
        quoi = input(''' Bonjour, que voulez vous faire?
                * Ajouter un code : tapez A
                * Consulter les codes : tapez C
                * Rien : Tapez R :        ''')
        
        if quoi == "A" :
            saisie_code()
            break
        elif quoi == "C" :
            consulter()
            break
        elif quoi == "R" :
            print("Merci de votre visite et à bientôt")
            break
        
        else:
            print("Merci d'indiquer un A, C ou R")

def saisie_code():

    while True :

            saisie = input('''veuillez saisir votre code :
                ● Il doit contenir au moins 8 caractères
                ● Il doit contenir au moins une lettre majuscule
                ● Il doit contenir au moins une lettre minuscule
                ● Il doit contenir au moins un chiffre
                ● Il doit contenir au moins un caractère spécial ( !  @  #  $  %  ^  & * )
                ''')

            if len(saisie) < 8:
                print("il faut au moins 8 caracteres")
            elif not re.search ("[a-z]",saisie):
                print ("il faut au moins une minuscule")
            elif not re.search ("[A-Z]", saisie):
                print (" il faut au moins une majuscule")
            elif not re.search ("[0-9]", saisie):
                print ("il faut au moins un nombre")
            elif not re.search ("[!@#$%^&()*]", saisie):
                print ("il faut l'un des caractères suivants : ()!@#$%^&*")

            else: 
                print ("votre code est parfait")
                
            cryptage(saisie)
            
            quefaire()
           
            break
    
def cryptage(saisie):

    crypte = hashlib.sha256(saisie.encode())
    code_final = crypte.hexdigest()

    print ("le code encrypté est :", code_final) 


                # Stockage
                # Vérifier si le fichier existe
    if not os.path.exists('mdp_cryptes.json'):
        # Créer le fichier s'il n'existe pas
        # Écrire un objet JSON vide pour commencer
        with open('mdp_cryptes.json', 'w') as f:
            f.write('{"code_final": []}')
                            
        # Lire les données existantes dans le fichier
    with open('mdp_cryptes.json', 'r') as file:
        data = json.load(file)
        if 'code_final' not in data:
            data['code_final'] = [code_final]
        else:
            data['code_final'].append(code_final)

        # Ajouter le code encrypté à la liste des codes encryptés
    data['code_final'].append(code_final)

        # Écrire les données mises à jour dans le fichier
    with open('mdp_cryptes.json', 'w') as file:
        json.dump(data, file)
    quefaire()

def consulter():
    with open('mdp_cryptes.json', 'r') as f:
        # Charger les données JSON
        data = json.load(f)

        # Afficher les données JSON
    print(data)
    quefaire()

quefaire()




