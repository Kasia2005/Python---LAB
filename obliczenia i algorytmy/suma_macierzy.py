from random import randint

def main():
    row = []
    A = []
    B = []
    C = []
    for i in range(128):
        for j in range(128):
            row.append(randint(0,100))
        A.append(row)
        row = []

    for i in range(128):
        for j in range(128):
            row.append(randint(0,100))
        B.append(row)
        row = []

    for i in range(128):
        for j in range(128):
            row.append(A[i][j]+B[i][j])
        C.append(row)
        row = []

    print(A)
    print(B)
    print(C)

if __name__ == '__main__':
    main()