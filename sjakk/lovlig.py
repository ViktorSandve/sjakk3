import brikker as b


def hent_trekk(f_r, f_k, brett):
    brikke = b.hent_brikke(f_r, f_k, brett)
    if brikke != None and brikke != 0:
        if brikke.lower() == "r":
            return b.bonde(f_r, f_k, brett, brikke)
        elif brikke.lower() == "t":
            return b.tårn(f_r, f_k, brett, brikke)
        elif brikke.lower() == "n":
            return b.hest(f_r, f_k, brett, brikke)
        elif brikke.lower() == "b":
            return b.løper(f_r, f_k, brett, brikke)
        elif brikke.lower() == "q":
            return b.dronning(f_r, f_k, brett, brikke)
        elif brikke.lower() == "k":
            return b.konge(f_r, f_k, brett, brikke)
    return []


def sjekk_lovlig(f_r, f_k, t_r, t_k, brett):
    brikke = b.hent_brikke(f_r, f_k, brett)
    if brikke != None and brikke != 0:
        if brikke.lower() == "r":
            return [t_k, t_r] in b.bonde(f_r, f_k, brett, brikke)
        elif brikke.lower() == "t":
            return [t_k, t_r] in b.tårn(f_r, f_k, brett, brikke)
        elif brikke.lower() == "n":
            return [t_k, t_r] in b.hest(f_r, f_k, brett, brikke)
        elif brikke.lower() == "b":
            return [t_k, t_r] in b.løper(f_r, f_k, brett, brikke)
        elif brikke.lower() == "q":
            return [t_k, t_r] in b.dronning(f_r, f_k, brett, brikke)
        elif brikke.lower() == "k":
            return [t_k, t_r] in b.konge(f_r, f_k, brett, brikke)
    return False

def riktig_farge(r, k, tur, brett):
    if tur == 1:
        return b.sjekk_liten(b.hent_brikke(r, k, brett))
    else:
        return b.sjekk_stor(b.hent_brikke(r, k, brett))

def flytt_brikke(f_r, f_k, t_r, t_k, brett):
    brikke = b.hent_brikke(f_r, f_k, brett)
    brett[f_k][f_r] = None
    brett[t_k][t_r] = brikke

def sjekk_forfremmelse (r, k, brett):
    if b.hent_brikke(r,k,brett) == "r" or b.hent_brikke(r, k, brett) =="R":
        if b.sjekk_liten(b.hent_brikke(r, k, brett)):
            return r == 7
        else:
            return r == 0

def forfremmelse(r, k, tur, brett):
    ny = input("Hva slags brikke vil du forandre bonden til? ")
    while ny != "tårn" and ny != "hest" and ny != "løper" and ny != "dronning":
        print("Ugyldig input, må være: tårn, hest, løper eller dronning.")
        ny = input("Hva slags brikke vil du forandre bonden til? ")
    if ny == "tårn":
        if tur == 1:
            brett[k][r] = "t"
        else:
            brett [k][r] = "T"
    elif ny == "hest":
        if tur == 1:
            brett[k][r] = "n"
        else:
            brett [k][r] = "N"
    if ny == "løper":
        if tur == 1:
            brett[k][r] = "b"
        else:
            brett [k][r] = "B"
    if ny == "dronning":
        if tur == 1:
            brett[k][r] = "q"
        else:
            brett [k][r] = "Q"

