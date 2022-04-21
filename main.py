import exercise2
from extras import run as e_run

choice = 0

if __name__ == '__main__':
    
    print("\n(Ievadiet '-1' lai beigtu!)")

    while True:
        try:
            choice = input("Lūdzu izvēlieties uzdevuma nr. (1-2 vai extra): ")
            if choice == "1":
                exercise2.fun_01()
                
            if choice == "2":
                exercise2.fun_04()

            if choice == "extra":
                e_run()

            if choice == "-1":
                break
        except:
            pass