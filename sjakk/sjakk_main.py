import formatering as f
import sjakk_bruker as b
import sjekk_sjakk as s
import lovlig as l


def main():
    
    f.velkomstmelding()
    brett = f.nytt_brett()
    tur = 1
    
    while not s.sjakk_matt(tur, brett):
        
        f.print_brett (brett)
        f.print_tur(tur)
        
        if s.sjakk(tur, brett):
            print ("Du er i sjakk.")
        trekk = b.ta_inn_trekk()
        if trekk == "avslutt":
            break
        fra_k, fra_r, til_k, til_r = b.konverter_trekk(trekk)
        
        while not l.riktig_farge(fra_r, fra_k, tur, brett) or not l.sjekk_lovlig(fra_r, fra_k, til_r, til_k, brett) or s.sjakk_etter_trekk(fra_r, fra_k, til_r,til_k, tur, brett):
            print("Ugyldig trekk.")
            trekk = b.ta_inn_trekk()
            if trekk == "avslutt":
                break
            fra_k, fra_r, til_k, til_r = b.konverter_trekk(trekk)
        
        l.flytt_brikke(fra_r, fra_k, til_r, til_k, brett)
        if l.sjekk_forfremmelse (til_r, til_k, brett):
            l.forfremmelse(til_r, til_k, tur, brett)
        
        if tur == 1:
            tur = 2
        else:
            tur = 1
    
    f.print_brett(brett)
    if s.sjakk_matt(tur, brett):
        print("Sjakk matt")
    if tur == 1:
        print("Sort vant!")
    else:
        print ("Hvit vant!")
      
main()

