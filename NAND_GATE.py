def NAND_GATE(a, b):
    if a and b:      # als a en b True zijn
        return 0     # return het tegenover gestelde
    return 1         # als a en b False zijn return True

def main():
    print(NAND_GATE(0, 0))
    print(NAND_GATE(0, 1))
    print(NAND_GATE(1, 0))
    print(NAND_GATE(1, 1))

main()
