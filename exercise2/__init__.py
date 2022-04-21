def fun_01():

    print("\n(Ievadiet '-1' lai beigtu!)")
    print("Izveido savas kūkas datus:")

    while True:
        try:
            cena = str(input("Ievadiet cenu (euro.centi: 3.45): "))
            if cena == '-1': 
                break

            euro, centi = cena.split(".")
            break
        except:
            print("\nIevadītais nav pieņemts!")

    while True:
        try:
            skaits = int(input("Ievadiet skaitu par cenu: "))
            if skaits == '-1': 
                break

            break
        except:
            print("\nIevadītais nav pieņemts!")
        
    print(f'\nPar {skaits} kūkām ir jamaksā {euro} eiro un {centi} centi\n')

def fun_02():
    while True:
        try:
            data = input("\nievadiet realu skaitli ar diviem decimal cipariem\n(3.12):")
            if data == '-1':
                break
                
            deci = float(data)

            print(f'\nDecimala dala ir {deci:.2f}')
        except:
            pass

def fun_03():
    pass
    # while True:
    #     try:
    #         data = input("\nVai papagailis runā: ")
    #         if data == '-1':
    #             break
            
    #     except:
    #         pass
        
def fun_04():
    pass