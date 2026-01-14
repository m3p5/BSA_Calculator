from math import *
from ti_system import *

disp_clr()
print("BSA Calculator v3 for")
print("Myeloma CAR-T Lymphodepletion")
print("")
print("1 = Metric (cm & kg)")
print("2 = SAE (inches & pounds)")
print("")
print("Units?")
unit=int(input())

disp_clr()
if unit==1:
    print("Height (cm):")
    h=float(input())
    print("Weight (kg):")
    w=float(input())
else:
    print("Height (inches):")
    hi=float(input())
    print("Weight (pounds):")
    wi=float(input())
    h=hi*2.54
    w=wi/2.20462

disp_clr()
# Du Bois
bsa_du=0.007184*w**0.425*h**0.725
# Mosteller
bsa_mo=sqrt(h*w/3600)
# % difference
pct=0
if bsa_du>0:
    pct=(bsa_mo-bsa_du)/bsa_du*100

print("Du Bois BSA   = ",round(bsa_du,4)," m²")
print("Mosteller BSA = ",round(bsa_mo,4)," m²")
print("Delta %       = ",round(pct,3),"%")
print("")
print("Press any key to continue...")
wait_key()
disp_clr()

# BSA capping
bsa_use=bsa_mo
if bsa_mo>2:
    print("Cap BSA?")
    print("1 = No Cap")
    print("2 = Cap at 2.0 m²")
    print("3 = Cap at 2.2 m²")
    capc=int(input())
    if capc==2:
        bsa_use=min(bsa_mo,2.0)
    elif capc==3:
        bsa_use=min(bsa_mo,2.2)
    else:
        bsa_use=bsa_mo

disp_clr()
print("Mosteller BSA used:",round(bsa_use,3),"m²")
print("")
print("Fludarabine 30 mg/m²:")
print("  Daily       =",int(30*bsa_use+0.5),"mg")
print("  3 Day Total =",int(90*bsa_use+0.5),"mg")
print("Cyclophosphamide 300 mg/m²:")
print("  Daily       =",int(300*bsa_use+0.5),"mg")
print("  3 Day Total =",int(900*bsa_use+0.5),"mg")
print("")
print("Done!")
