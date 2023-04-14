

def draw_rectangle(L,H):
    print("|",("-"*L),"|")
    
    for i in range(H-2):
        print("|"," "*(L),"|")

    print("|",("-"*L),"|")
          

draw_rectangle(10,3)
