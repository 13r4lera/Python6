def recursion(n) :
    if n == 1:
        return 1

    return n + recursion(n - 1)


def main():
    print(recursion(3))
    print(recursion(7))

if __name__ == '__main__':
    main()