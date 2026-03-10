
#Fuck ohm

valg = float(input("Vælg mellem\n"
                   "1 Serieforbindelse:\t" 
                   "2 Parallelforbindelse:\t"
                   "3 Kombination af Serie og Parallel\t"))

if valg == 1:
   SF_1 = float(input("Beregn den samlede modstand R_total\n"
                      "1.1 Serieforbindelse med 2 modstande:\n"
                      "1.2 Serieforbindelse med 3 modstande:\n"))

   NUMS_1 = float(input("R1\t"))
   # NUMS er modstand Ω (ohm)
   NUMS_2 = float(input("R2:\t"))

   if SF_1 == 1.1:
       print("=\t", NUMS_1 + NUMS_2)

   elif SF_1 == 1.2:
       NUMS_3 = float(input("R3\t"))
       print("=\t", NUMS_1 + NUMS_2 + NUMS_3)

if valg == 2:
    PF_1 = float(input("Beregn den samlede modstand R_total\n"
                       "1.1 Parallelforbindelse med 2 modstande:\n"
                       "1.2 Parallelforbindelse med 3 modstande:\n"))

    NUMP_1 = float(input("R1=\t"))
    NUMP_2 = float(input("R2=\t"))

    if PF_1 == 1.1:
        print("=\t", ((1/NUMP_1)+(1/NUMP_2)**-1))

    elif PF_1 == 1.2:
        NUMP_3 = float(input("R3=\t"))
        print("=\t", ((1/NUMP_1)+(1/NUMP_2)+(1/NUMP_3)**-1))

if valg == 3:
    KSP_1 = float(input("beregn den samlede modstand R_total\n"))
