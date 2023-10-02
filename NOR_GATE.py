def NOR_GATE(a, b):
    return not (a or b)

def main():
    print(NOR_GATE(0, 0))
    print(NOR_GATE(0, 1))
    print(NOR_GATE(1, 0))
    print(NOR_GATE(1, 1))

main()
