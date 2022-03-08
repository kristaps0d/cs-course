import exercise2

choice = 0

if __name__ == '__main__':
    
    print("\n(Ievadiet '-1' lai beigtu!)")

    while True:
        try:
            choice = int(input("Lūdzu izvēlieties uzdevuma nr. (1-2): "))
            if choice == 1:
                exercise2.fun_01()
                
            if choice == 2:
                exercise2.fun_02()

            if choice == -1:
                break
        except:
            pass