from liczby_zespolone import ComplexNumber

def main():

    real1= float(input("Wprowadź część rzeczywistą pierwszej liczby: "))
    imag1 = float(input("Wprowadź część urojoną pierwszej liczby: "))
    real2 = float(input("Wprowadź część rzeczywistą drugiej liczby: "))
    imag2 = float(input("Wprowadź część urojoną drugiej liczby: "))

    complex1 = ComplexNumber(real1, imag1)
    complex2 = ComplexNumber(real2, imag2)

    choice = int(input("Proszę wybrać rodzaj operacji: \n"
                       "1 - dodawanie liczb zespolonych\n"
                       "2 - odejmowanie liczb zespolonych\n"
                       "3 - mnożenie liczb zespolonych\n"))
    if choice == 1:
        wynik= complex1+complex2
        print(wynik)
    elif choice == 2:
        wynik = complex1 - complex2
        print(wynik)
    elif choice == 3:
        wynik = complex1 * complex2
        print(wynik)
    else:
        print("Nieprawidłowy wybór!")
        main()

if __name__ == '__main__':
    main()
