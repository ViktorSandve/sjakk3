
def ta_inn_trekk():
    trekk = input ("Skriv inn ditt trekk: [fra til] ")
    return trekk

def konverter_trekk(streng):
    try:
        return ord(streng[0].upper())-65, int(streng[1])-1, ord(streng[3].upper())-65, int(streng[4])-1
    except:
        return None, None, None, None
        
