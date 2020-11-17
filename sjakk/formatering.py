
def nytt_brett():
    return [["t","r",None,None,None,None,"R","T"],["n","r",None,None,None,None,"R","N"],["b","r",None,None,None,None,"R","B"],["q","r",None,None,None,None,"R","Q"],["k","r",None,None,None,None,"R","K"],["b","r",None,None,None,None,"R","B"],["n","r",None,None,None,None,"R","N"],["t","r",None,None,None,None,"R","T"]]


def velkomstmelding ():
    print('Velkommen til sjakk. Skriv "avslutt" for å avslutte.')
    
def print_tur(tur):
    if tur == 1:
        print ("Hvit sin tur")
    if tur == 2:
        print ("Sort sin tur")

def print_rute(r, k):
    if r[k] == None :
        print ("\u2009\u2009", end = " ")
    elif r[k] == "r":
        print ("♙", end = " ")
    elif r[k] == "R":
        print ("♟", end = " ")
    elif r[k] == "t":
        print ("♖", end = " ")
    elif r[k] == "T":
        print ("♜", end = " ")
    elif r[k] == "n":
        print ("♘", end = " ")
    elif r[k] == "N":
        print ("♞", end = " ")
    elif r[k] == "b":
        print ("♗", end = " ")
    elif r[k] == "B":
        print ("♝", end = " ")
    elif r[k] == "q":
        print ("♕", end = " ")
    elif r[k] == "Q":
        print ("♛", end = " ")
    elif r[k] == "k":
        print ("♔", end = " ")
    elif r[k] == "K":
        print ("♚", end = " ")
    

def print_brett(brett):
    print ("  --------------------------------------")
    for k in range (8):
        print (8-k, end = " ")
        for r in brett:
            print ("|", end = " ")
            print_rute (r, 7-k)
                
        print("|")
        print ("  --------------------------------------")
    print ("    A    B    C   D    E    F   G    H")
        


