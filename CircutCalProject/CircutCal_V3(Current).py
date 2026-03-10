
#Lommeregner til at udregne R_total

keep_going = 'j'
while keep_going == 'j':
    valg = float(input("Beregning af Samlet Modstand. Vælg mellem:\n"
                       "1 Serieforbindelse:\n"
                       "2 Parallelforbindelse:\n"
                       "3 Kombination af Serie og Parallelforbindelse:\n"
                       "Skriv svar her:\n"))

    if valg == 1:
        SF_1 = float(input("Beregn den samlede modstand R_total\n"
                           "2 modstande i Serieforbindelse:\n"
                           "3 modstande i Serieforbindelse:\n"
                           "4 modstande i Serieforbindelse:\n"
                           "Hvad vil du beregne?\n"))
        NUMS_1 = float(input("R1\t"))
        # NUMS er modstand Ω (ohm)
        NUMS_2 = float(input("R2:\t"))

        if SF_1 == 2:
            print("R_total=\t", NUMS_1 + NUMS_2)

        elif SF_1 == 3:
            NUMS_3 = float(input("R3\t"))
            print("R_total=\t", NUMS_1 + NUMS_2 + NUMS_3)

        elif SF_1 == 4:
            NUMS_3 = float(input("R3\t"))
            NUMS_4 = float(input("R4\t"))
            print("R_total=\t", NUMS_1 + NUMS_2 + NUMS_3+NUMS_4)

    if valg == 2:
        PF_1 = float(input("Beregn den samlede modstand R_total\n"
                           "2 modstande i Parallelforbindelse:\n"
                           "3 modstande i Parallelforbindelse:\n"
                           "4 modstande i Parallelforbindelse:\n"
                           "Hvad vil du beregne?\t"))
        NUMP_1 = float(input("R1=\t"))
        NUMP_2 = float(input("R2=\t"))

        if PF_1 == 2:
            print("R_total=\t", ((1 / NUMP_1) + (1 / NUMP_2) ** -1))

        elif PF_1 == 3:
            NUMP_3 = float(input("R3=\t"))
            print("R_total=\t", ((1 / NUMP_1) + (1 / NUMP_2) + (1 / NUMP_3)**-1))

        elif PF_1 == 4:
            NUMP_3 = float(input("R3=\t"))
            NUMP_4 = float(input("R4=\t"))
            print("R_total=\t", ((1 / NUMP_1) + (1 / NUMP_2) + (1 / NUMP_3)+(1 / NUMP_4)**-1))

    if valg == 3:
        KSP_1 = float(input("Beregn den samlede modstand R_total\n"
                           "2 modstande i Serie- og Parallelforbindelse:\n"
                           "3 modstande i Serie- og Parallelforbindelse:\n"
                           "4 modstande i Serie- og Parallelforbindelse:\n"
                           "Hvad vil du beregne?\t"))

        NUMK_1 = float(input("R1=\t"))
        NUMK_2 = float(input("R2=\t"))

        if KSP_1 == 2:
            R_total=(1 / NUMK_1) + (1 / NUMK_2) ** -1
            print("R_total=\t", NUMK_1 + R_total)

        elif KSP_1 == 3:
            NUMK_3 = float(input("R3=\t"))
            R_total=(1 / NUMK_1) + (1 / NUMK_2)+(1 / NUMK_3) ** -1
            print("R_total=\t", NUMK_1 + R_total)



    keep_going = input('Udregn flere R_total:' + '(tryk Enter j for ja eller n for nej):\t')

