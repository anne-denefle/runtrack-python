def hauteurParcourue(nb, h) :  
    print(f"Pour {nb} marches de {h}cm, il parcourt {nb*h*2*5*7/100.0:.2f}m par semaine !") 
  

nbMarches = int(input("Combien de marches ?"))  
hauteurMarche = int(input("Hauteur d'une marche (cm) ?"))  
  
hauteurParcourue(nbMarches, hauteurMarche)