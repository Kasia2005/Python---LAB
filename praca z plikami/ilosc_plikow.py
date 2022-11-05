import os
def main ():
    sciezka = "C:/Users/Kasia/PycharmProjects/pythonProject3"
    katalogi_i_pliki = os.listdir(sciezka)
    print(katalogi_i_pliki)
    print(len(katalogi_i_pliki))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()