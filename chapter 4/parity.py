import sys
def parity(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result

print(parity(int(sys.argv[1])))
