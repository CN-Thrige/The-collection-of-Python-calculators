


keep_going = 'j'
while keep_going == 'j':
    valg = float(input("Beregn den samlede modstand R_total\n"
                       "1. Serieforbindelse med 2 modstande:\n"
                       "2. Serieforbindelse med 3 modstande:\n"
                       "3. Parallelforbindelse med 2 modstande:\n"
                       "4. Parallelforbindelse med 3 modstande:\n"
                       "svar:\t"))

    mod_1 = float(input("Skriv det første tal:\t"))
    #modstand eller mod. o for Ω (ohm)
    mod_2 = float(input("Skriv det andet tal:\t"))

    mod_3 = float(input("Skriv det tredje tal:\t"))

    if valg == 1:
        print("=\t", mod_1+mod_2)

    if valg == 2:
        print("=\t", mod_1+mod_2+mod_3)

    if valg == 3:
        print("=\t", ((1/mod_1)+(1/mod_2)^(-1)))

    if valg == 3:
        print("=\t", ((1/mod_1)+(1/mod_2)+(1/mod_3)^(-1)))


    keep_going = input('Beregn den næste samlede modstand R_total' + '(tryk Enter j for ja eller n for nej):\t')



