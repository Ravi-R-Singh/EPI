import sys

def isPowerOf2 (x: int) -> bool:
    return not x&(x-1)

print(isPowerOf2(int(sys.argv[1])))
