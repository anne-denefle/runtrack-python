
import re
import hashlib
import json
import os


                

while True :

    code = input('''veuillez saisir votre code :
             ● Il doit contenir au moins 8 caractères
             ● Il doit contenir au moins une lettre majuscule
             ● Il doit contenir au moins une lettre minuscule
             ● Il doit contenir au moins un chiffre
             ● Il doit contenir au moins un caractère spécial ( !  @  #  $  %  ^  & * )
             ''')

    if len(code) < 8:
        print("il faut au moins 8 caracteres")

    elif not re.search ("[a-z]",code):
        print ("il faut au moins une minuscule")
    elif not re.search ("[A-Z]", code):
        print (" il faut au moins une majuscule")
    
    elif not re.search ("[0-9]", code):
        print ("il faut au moins un nombre")

    elif not re.search ("[!@#$%^&()*]", code):
        print ("il faut l'un des caractères suivants : ()!@#$%^&*")
    
    
    else: 
        print ("votre code est parfait")
        break
    

                    #cryptage 

crypte = hashlib.sha256(code.encode())
code_final = crypte.hexdigest()

print ("le code encrypté est :", code_final)

                    #stockage
                    #Création d'un fichier et écriture
                        # Vérifier si le fichier existe
if not os.path.exists('mdp_cryptes.json'):
                        # Créer le fichier s'il n'existe pas
                # Écrire un objet JSON vide pour commencer
    with open('mdp_cryptes.json', 'w') as f:
        f.write('{}')   
                            # Lire les données existantes dans le fichier
with open('mdp_cryptes.json', 'r') as file:
    data = json.load(file)

    if 'code_final' not in data:
        data['code_final'] = [code_final]
    else:
        data['code_final'].append(code_final)
        

                            # Écrire les données mises à jour dans le fichier
    with open('mdp_cryptes.json', 'w') as file:
        json.dump(data, file)

