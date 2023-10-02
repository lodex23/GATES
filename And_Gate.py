def And_Gate(a, b):
    if a == 1 and b == 1:
        return True
    else:
        return False
def main():
    input_1 = int(input("1 or 0: "))
    input_2 = int(input("1 or 0: "))
    c = And_Gate(input_1, input_2)
    print(c)


if __name__ == "__main__":
    main()
