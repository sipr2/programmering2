import datetime
 
def berakna_kostnad(start_datum, slut_datum, matar_start, matar_slut, kwh_pris, daglig_kostnad):
    start_datum = datetime.datetime.strptime(start_datum_str, "%Y-%m-%d")
    slut_datum = datetime.datetime.strptime(slut_datum_str, "%Y-%m-%d")
   
    dagar_diff = (slut_datum - start_datum).days
   
    
    mätinställning_diff = matar_slut - matar_start
   
    
    moms = 1.25  
    total_kostnad = ((dagar_diff * daglig_kostnad) + (mätinställning_diff * kwh_pris)) * moms
   
    print(f"Total kostnad: {total_kostnad:.2f} öre")


start_datum_str = input("Ange startdatum (YYYY-MM-DD): ")
slut_datum_str = input("Ange slutdatum (YYYY-MM-DD): ")
try:
    matar_start = int(input("Ange mätarinställning vid startdatum (i kWh): "))
except:
    print("Är du dum, skriv siffra")
    exit()

matar_slut = int(input("Ange mätarinställning vid slutdatum (i kWh): "))
kostnad_per_kwh = int(input("Ange kostnad i öre/kWh: "))
daglig_avgift = int(input("Ange daglig stående avgift i öre: "))
 
berakna_kostnad(start_datum_str, slut_datum_str, matar_start, matar_slut, kostnad_per_kwh, daglig_avgift)
