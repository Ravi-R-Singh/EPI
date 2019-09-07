import sys

def Mod_power_of_2 (x: int, y: int) -> int:
    return x & ((y|(y-1))>>1)

print(Mod_power_of_2(int(sys.argv[1]), int(sys.argv[2])))
