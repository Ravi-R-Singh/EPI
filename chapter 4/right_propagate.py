import sys

def rightProp (x: int) -> int: 
    x |= x-1
    return x
print(rightProp(int(sys.argv[1])))
