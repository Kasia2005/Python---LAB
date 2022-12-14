from random import randint
from numpy import linalg.det

def main():
    random_dimension = randint(0,10)
    A = []
    row = []

    for i in range(random_dimension):
        for j in range(random_dimension):
            row.append(randint(0,10))
        A.append(row)
        row = []

    determinant = linalg.det(A)

    print(A)
    print(determinant)

if __name__ == '__main__':
    main()