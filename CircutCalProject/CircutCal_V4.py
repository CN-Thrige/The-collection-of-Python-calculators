


ir1 = float(input("Type 1 to calculate Ir1\t"))
if ir1 == 1:
    v1 = float(input("Type: v1\t"))
    # NUMS er modstand Ω (ohm)
    r1 = float(input("Type: r1\t"))
    r2 = float(input("Type: r2\t"))

    print(f'IR1= {v1 / (r1 + r2)}mA')

ir3 = float(input("Type 2 to calculate Ir3\t"))
if ir3 == 2:

    v1 = float(input("Type: v1\t"))
    r3 = float(input("Type: r3\t"))
    r4 = float(input("Type: r4\t"))

    print(f'IR3= {v1/(r3+r4)}mA')

Vr1 = float(input("Type 1 to calculate Vr1"))
if Vr1 == 1:
    v1 = float(input("Type: v1\t"))
    ir1 = float(input("Type: ir1\t"))
    r1 = float(input("Type: r1\t"))

    print(f'Vr1= {ir1*r1}mA')

