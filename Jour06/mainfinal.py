
import re
import hashlib
import json
import os

saisie = ""
code_final = ""



def quefaire():

    while True :
        quoi = input(''' Bonjour, que voulez vous faire?
                * Ajouter un code : tapez A
                * Consulter les codes : tapez C
                * Rien : Tapez R :        ''')
        
        if quoi == "A" :
            saisie_code()
            cryptage(saisie)
            stockage(code_final)
            
            break
        elif quoi == "C" :
            consulter_crypt(code_final)
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
            break
def consulter_crypt(code_final):
    if not "mdp_cryptes.json":
        print ("il n'y a pas de code")
        quefaire()
    else:
        for code_final in "mdp_cryptes.json" :
            print(code_final)
            quefaire()   

def cryptage(saisie):

    crypte = hashlib.sha256(saisie.encode())
    code_final = crypte.hexdigest()

    print ("le code encrypté est :", code_final) 

def stockage(code_final):

    filename = "mdp_cryptes.json"
                    #stockage
                    #Création d'un fichier et écriture
                        # Vérifier si le fichier existe
    if not os.path.exists(filename):
                        # Créer le fichier s'il n'existe pas
                # Écrire un objet JSON vide pour commencer
        with open(filename, 'w') as f:
            json.dump([], f) 
                            # Lire les données existantes dans le fichier
    with open(filename, 'r') as f:
        check = json.load(f)
        saisie = saisie_code()
        code_final = cryptage(saisie)
    check.append([code_final])
    with open(filename,"w") as f:
        json.dump(check, f)
    print("mot de passe enregistré avec succès") 

quefaire()
