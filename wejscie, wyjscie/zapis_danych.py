# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    for proba in range(1, 4):
        code = "1234"
        szyfr = input("Podaj szyfr: ")
        if szyfr == code:
            print("Poprawny kod")
            break
        else:
            print("Niepoprawny kod")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()