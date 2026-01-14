# BSA Calculator
# Version 5

from math import *
from ti_system import *

while True:
    disp_clr()
    print("BSA Calculator v5 for Myeloma")
    print("CAR-T Cell Lymphodepletion\n")
    print("1 = Metric (cm & kg)")
    print("2 = English (inches & pounds)\n")
    unit=int(input("Units? "))

    disp_clr()
    if unit==1:
        h=float(input("Height (cm): "))
        w=float(input("Weight (kg): "))
    else:
        hi=float(input("Height (inches): "))
        wp=float(input("Weight (pounds): "))
        h=hi*2.54
        w=wp/2.20462

    disp_clr()
    # Du Bois
    bsa_du=0.007184*w**0.425*h**0.725
    # Mosteller
    bsa_mo=sqrt(h*w/3600)
    # % difference
    pct=0
    if bsa_du>0:
        pct=(bsa_mo-bsa_du)/bsa_du*100

    print("Du Bois BSA   = ",round(bsa_du,3)," m²")
    print("Mosteller BSA = ",round(bsa_mo,3)," m²")
    print("Delta %       = ",round(pct,2),"%\n")
    print("Press any key to continue...")
    wait_key()
    disp_clr()

    # BSA capping
    bsa_use=bsa_mo
    if bsa_mo>2:
        print("Cap BSA Question:")
        print("1 = No Cap")
        print("2 = Cap at 2.0 m²")
        print("3 = Cap at 2.2 m²")
        capc=int(input("Cap BSA? "))
        if capc==2:
            bsa_use=min(bsa_mo,2.0)
        elif capc==3:
            bsa_use=min(bsa_mo,2.2)
        else:
            bsa_use=bsa_mo

    disp_clr()
    print("Mosteller BSA used:",round(bsa_use,3),"m²\n")
    print("Fludarabine 30 mg/m²:")
    print("  Daily       =",int(30*bsa_use+0.5),"mg")
    print("  3 Day Total =",int(90*bsa_use+0.5),"mg")
    print("Cyclophosphamide 300 mg/m²:")
    print("  Daily       =",int(300*bsa_use+0.5),"mg")
    print("  3 Day Total =",int(900*bsa_use+0.5),"mg\n")

    # Repeat or exit prompt
    again=int(input("Run again (1 = Yes, 2 = No)? "))
    if again != 1:
        disp_clr()
        print("Goodbye!")
        break