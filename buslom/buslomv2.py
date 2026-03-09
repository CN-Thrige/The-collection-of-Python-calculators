

keep_going = 'j'
while keep_going == 'j':
    DSB_standard_billet_pris = 30
    pris_for_rejsen = 0

    tog_stopper_her = ["ÅRHUS H", "HORSENS", "VEJLE", "FREDERICA", "MIDDELFART", "ODENSE", "ROSKILDE", "KØBENHAVN H", "CPH AIRPORT"]
    # en liste er altid ligemed nul


    stig_paa_tog = input("Indtast din start destination ").upper()
    #.upper input omdanner alt i  upper case

    stig_af_tog = input("indtast din slut destination ").upper()

    x = tog_stopper_her.index(stig_paa_tog) + 1
    y = tog_stopper_her.index(stig_af_tog) + 1
    pris_forskel = y - x + 2


    if stig_paa_tog == pris_forskel:
        pris_for_rejsen = DSB_standard_billet_pris
        print(f'din billet pris {pris_for_rejsen} kr')

    else:
        pris_for_rejsen = DSB_standard_billet_pris*pris_forskel*0.90
        print(f'din billet pris {pris_for_rejsen} kr')

    keep_going = input('udregn flere billet priser:' + '(tryk Enter j for ja eller n for nej):\t')
    # s. 171-172 om The while Loop: A Condition-Controlled Loop