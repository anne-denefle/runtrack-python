
def cesar(msg="", clef=0): 
	alphabet="abcdefghijklmnopqrstuvwxyz" 
	chiffre="" 
  
	
	for l in msg.lower(): 
		pos=alphabet.find(l) 
  
		chiffre+=alphabet[(pos+clef) % len(alphabet)] if pos != -1 else l 
	
	return chiffre 

  
message="Hello World !!!" 
chiffre=cesar(message, 3) 
dechiffre=cesar(chiffre, -3) 
print(message, "=>", chiffre, "=>", dechiffre)