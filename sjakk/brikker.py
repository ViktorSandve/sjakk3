
def sjekk_stor (r):
    try:
        return r.isupper()
    except:
        return False

def sjekk_liten (r):
    try:
        return r.islower()
    except:
        return False


def hent_brikke(r, k, brett):
    try:
        if k >= 0 and r >= 0:
            return brett [k][r]
        else:
            return 0
    except:
        return 0


def bonde (r, k, brett, brikke):
    liste = []
    if brikke.islower(): #hvit
        if hent_brikke (r+1, k, brett) == None:
            liste.append([k, r+1])
            if r == 1 and hent_brikke (r+2, k, brett) == None:
                liste.append([k, r+2])
        if sjekk_stor(hent_brikke (r+1, k+1 , brett)):
            liste.append([k+1, r+1])
        if sjekk_stor(hent_brikke (r+1, k-1 , brett)):
            liste.append([k-1, r+1])

    else: #sort
        if hent_brikke (r-1, k, brett) == None:
            liste.append([k, r-1])
            if r == 6 and hent_brikke (r-2, k, brett) == None:
                liste.append([k, r-2])
        if sjekk_liten(hent_brikke(r-1, k+1 , brett)):
            liste.append([k+1, r-1])
        if sjekk_liten(hent_brikke(r-1, k-1 , brett)):
            liste.append([k-1, r-1])
    return liste



def tårn (r, k, brett, brikke):
    liste = []
    for x in range (1,7):
        if hent_brikke(r+x, k, brett) == None:
            liste.append ([k, r+x])
        else:
            if (brikke.islower() and sjekk_stor(hent_brikke(r+x, k, brett))) or (brikke.isupper() and sjekk_liten(hent_brikke(r+x, k, brett))):
                liste.append([k, r+x])
            break
    
    for x in range (1,7):
        if hent_brikke(r-x, k, brett) == None:
            liste.append ([k, r-x])
        else:
            if (brikke.islower() and sjekk_stor(hent_brikke(r-x, k, brett))) or (brikke.isupper() and sjekk_liten(hent_brikke(r-x, k, brett))):
                liste.append([k, r-x])
            break
    
    for x in range (1,7):
        if hent_brikke(r, k+x, brett) == None:
            liste.append ([k+x, r])
        else:
            if (brikke.islower() and sjekk_stor(hent_brikke(r, k+x, brett))) or (brikke.isupper() and sjekk_liten(hent_brikke(r, k+x, brett))):
                liste.append([k+x, r])
            break
    
    for x in range (1,7):
        if hent_brikke(r, k-x, brett) == None:
            liste.append ([k-x, r])
        else:
            if (brikke.islower() and sjekk_stor(hent_brikke(r, k-x, brett))) or (brikke.isupper() and sjekk_liten(hent_brikke(r, k-x, brett))):
                liste.append([k-x, r])
            break
            
    return liste
                     
 
def løper (r, k , brett, brikke):   
    liste = []
    for x in range (1,7):
        if hent_brikke(r+x, k+x, brett) == None:
            liste.append ([k+x, r+x])
        else:
            if (brikke.islower() and sjekk_stor(hent_brikke(r+x, k+x, brett))) or (brikke.isupper() and sjekk_liten(hent_brikke(r+x, k+x, brett))):
                liste.append([k+x, r+x])
            break
    
    for x in range (1,7):
        if hent_brikke(r-x, k-x, brett) == None:
            liste.append ([k-x, r-x])
        else:
            if (brikke.islower() and sjekk_stor(hent_brikke(r-x, k-x, brett))) or (brikke.isupper() and sjekk_liten(hent_brikke(r-x, k-x, brett))):
                liste.append([k-x, r-x])
            break
    
    for x in range (1,7):
        if hent_brikke(r-x, k+x, brett) == None:
            liste.append ([k+x, r-x])
        else:
            if (brikke.islower() and sjekk_stor(hent_brikke(r-x, k+x, brett))) or (brikke.isupper() and sjekk_liten(hent_brikke(r-x, k+x, brett))):
                liste.append([k+x, r-x])
            break
    
    for x in range (1,7):
        if hent_brikke(r+x, k-x, brett) == None:
            liste.append ([k-x, r+x])
        else:
            if (brikke.islower() and sjekk_stor(hent_brikke(r+x, k-x, brett))) or (brikke.isupper() and sjekk_liten(hent_brikke(r+x, k-x, brett))):
                liste.append([k-x, r+x])
            break
            
    return liste

def dronning (r, k, brett, brikke):
    liste = tårn (r, k, brett, brikke)
    for i in løper (r,k, brett, brikke):
        liste.append(i)
    return liste

def hest (r, k, brett, brikke):
    liste = []
    if brikke.islower(): #hvit
        for x in range (1,3):
            if x == 1:
                y = 2
            else:
                y = 1
            if hent_brikke(r+x, k+y, brett) == None or sjekk_stor(hent_brikke(r+x, k+y, brett)):
                liste.append ([k+y, r+x])
            if hent_brikke(r+x, k-y, brett) == None or sjekk_stor(hent_brikke(r+x, k-y, brett)):
                liste.append ([k-y, r+x])
            if hent_brikke(r-x, k+y, brett) == None or sjekk_stor(hent_brikke(r-x, k+y, brett)):
                liste.append ([k+y, r-x])
            if hent_brikke(r-x, k-y, brett) == None or sjekk_stor(hent_brikke(r-x, k-y, brett)):
                liste.append ([k-y, r-x])
    else: #sort
        for x in range (1,3):
            if x == 1:
                y = 2
            else:
                y = 1
            if hent_brikke(r+x, k+y, brett) == None or sjekk_liten(hent_brikke(r+x, k+y, brett)):
                liste.append ([k+y, r+x])
            if hent_brikke(r+x, k-y, brett) == None or sjekk_liten(hent_brikke(r+x, k-y, brett)):
                liste.append ([k-y, r+x])
            if hent_brikke(r-x, k+y, brett) == None or sjekk_liten(hent_brikke(r-x, k+y, brett)):
                liste.append ([k+y, r-x])
            if hent_brikke(r-x, k-y, brett) == None or sjekk_liten(hent_brikke(r-x, k-y, brett)):
                liste.append ([k-y, r-x])
    return liste
            

def konge (r, k, brett, brikke):
    liste = []
    if brikke.islower():#hvit
        if hent_brikke(r+1, k, brett) == None or sjekk_stor(hent_brikke(r+1, k, brett)):
            liste.append ([k, r+1])
        if hent_brikke(r+1, k+1, brett) == None or sjekk_stor(hent_brikke(r+1, k+1, brett)):
            liste.append ([k+1, r+1])
        if hent_brikke(r+1, k-1, brett) == None or sjekk_stor(hent_brikke(r+1, k-1, brett)):
            liste.append ([k-1, r+1])
        if hent_brikke(r, k+1, brett) == None or sjekk_stor(hent_brikke(r, k+1, brett)):
            liste.append ([k+1, r])
        if hent_brikke(r, k-1, brett) == None or sjekk_stor(hent_brikke(r, k-1, brett)):
            liste.append ([k-1, r])
        if hent_brikke(r-1, k, brett) == None or sjekk_stor(hent_brikke(r-1, k, brett)):
            liste.append ([k, r-1])
        if hent_brikke(r-1, k+1, brett) == None or sjekk_stor(hent_brikke(r-1, k+1, brett)):
            liste.append ([k+1, r-1])
        if hent_brikke(r-1, k-1, brett) == None or sjekk_stor(hent_brikke(r-1, k-1, brett)):
            liste.append ([k-1, r-1])
    else: #sort
        if hent_brikke(r+1, k, brett) == None or sjekk_liten(hent_brikke(r+1, k, brett)):
            liste.append ([k, r+1])
        if hent_brikke(r+1, k+1, brett) == None or sjekk_liten(hent_brikke(r+1, k+1, brett)):
            liste.append ([k+1, r+1])
        if hent_brikke(r+1, k-1, brett) == None or sjekk_liten(hent_brikke(r+1, k-1, brett)):
            liste.append ([k-1, r+1])
        if hent_brikke(r, k+1, brett) == None or sjekk_liten(hent_brikke(r, k+1, brett)):
            liste.append ([k+1, r])
        if hent_brikke(r, k-1, brett) == None or sjekk_liten(hent_brikke(r, k-1, brett)):
            liste.append ([k-1, r])
        if hent_brikke(r-1, k, brett) == None or sjekk_liten(hent_brikke(r-1, k, brett)):
            liste.append ([k, r-1])
        if hent_brikke(r-1, k+1, brett) == None or sjekk_liten(hent_brikke(r-1, k+1, brett)):
            liste.append ([k+1, r-1])
        if hent_brikke(r-1, k-1, brett) == None or sjekk_liten(hent_brikke(r-1, k-1, brett)):
            liste.append ([k-1, r-1])
    return liste


        
    
        
    