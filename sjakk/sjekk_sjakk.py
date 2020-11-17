
import brikker as b
import lovlig as l

def hent_konge(tur, brett):
    if tur == 1: #hvit
        for k in range(len(brett)):
            for r in range(len(brett[k])):
                if brett[k][r] == "k":
                    return r, k
    else : #sort
        for k in range(len(brett)):
            for r in range(len(brett)):
                if brett[k][r] == "K":
                    return r, k
    return None
        
def sjakk (tur, brett):
    r, k = hent_konge(tur, brett)
    for f_k in range(len(brett)):
        for f_r in range(len(brett[f_k])):
            if l.sjekk_lovlig (f_r, f_k, r, k, brett):
                return True
    return False

def sjakk_etter_trekk (f_r, f_k, t_r, t_k, tur, brett):
    nytt = []
    for x in brett:
        kolonne = []
        for y in x:
            kolonne.append(y)
        nytt.append(kolonne)
    brikke = b.hent_brikke(f_r, f_k, nytt)
    nytt[f_k][f_r] = None
    nytt [t_k][t_r] = brikke
    return sjakk(tur, nytt)

     

def sjakk_matt(tur, brett):
    if tur == 1:
        for x in range (len(brett)):
            for y in range (len(brett)):
                brikke = b.hent_brikke(y, x, brett)
                if b.sjekk_liten(brikke):
                    mulige_trekk = l.hent_trekk (y, x, brett)
                    for trekk in mulige_trekk:
                        if not sjakk_etter_trekk(y, x, trekk[1], trekk[0], tur, brett):
                            return False
    else:
        for x in range (len(brett)):
            for y in range (len(brett)):
                brikke = b.hent_brikke(y, x, brett)
                if b.sjekk_stor(brikke):
                    mulige_trekk = l.hent_trekk (y, x, brett)
                    for trekk in mulige_trekk:
                        if not sjakk_etter_trekk(y, x, trekk[1], trekk[0], tur, brett):
                            return False
    
    return True

