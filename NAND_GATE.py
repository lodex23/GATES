def NAND_GATE(a, b):
    return not (a and b)

def main():
    print(NAND_GATE(0, 0))
    print(NAND_GATE(0, 1))
    print(NAND_GATE(1, 0))
    print(NAND_GATE(1, 1))

main()
