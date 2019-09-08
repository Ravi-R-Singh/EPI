import sys
def power(x: float, y: int) -> float:
    temp = x
    for i in range(y-1):
        x *= temp
    return x

print(power(float(sys.argv[1]),int(sys.argv[2])))
