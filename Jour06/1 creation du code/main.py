
import re



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
    

          
            

    



