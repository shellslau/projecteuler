import math

def find_triplet(num):
    for a in range(1, num):
        for b in range(1, num - a):
            c = math.sqrt(a*a + b*b)

            if (c.is_integer):
                if (a + b + c) == num:
                    return (a, b, c)

triplet = find_triplet(1000)
print(triplet)
print(triplet[0]*triplet[1]*triplet[2])
