
start_zone = input(f'Enter start zone: ')
billetpris = 30
pris_stigning_per_zone = 30
slut_zone = billetpris




if start_zone == 1:
    print(billetpris)


else:
    y=10
    x= billetpris+pris_stigning_per_zone
    #x er lige med billetpris
    x -= (x * y)/100
    print(f'Din rabat er {x} kr')