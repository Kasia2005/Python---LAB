a = [1,2,12,44]
b = [2,4,2,8]
c = []
def main():
    for i in range(len(a)):
        c.append(a[i]*b[i])

    result = sum(c)
    print(result)
if __name__ == '__main__':
    main()
