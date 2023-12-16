from itertools import product
N = int(input())

repunits = [1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111, 11111111111, 111111111111]
#           1,  4,   10,   20,    35,    56,     84,      120,       165,        220,         286,         364
#           1,  3,    6,   10,    15,    21,     28,       36,        45,         55,          66,          78

# (n * (n + 1)) / 2

def sum_patterns(numbers: list[int]):
    return sorted(list(set([sum(combination) for combination in product(numbers, repeat=3)])), reverse=True)

if N == 1:
    print(3)
elif N <= 4:
    usable = repunits[:2]
    result = sum_patterns(usable)
    index = 4 - N
    print(result[index])
elif N <= 10:
    usable = repunits[:3]
    result = sum_patterns(usable)
    index = 10 - N
    print(result[index])
elif N <= 20:
    usable = repunits[:4]
    result = sum_patterns(usable)
    index = 20 - N
    print(result[index])
elif N <= 35:
    usable = repunits[:5]
    result = sum_patterns(usable)
    index = 35 - N
    print(result[index])
elif N <= 56:
    usable = repunits[:6]
    result = sum_patterns(usable)
    index = 56 - N
    print(result[index])
elif N <= 84:
    usable = repunits[:7]
    result = sum_patterns(usable)
    index = 84 - N
    print(result[index])
elif N <= 120:
    usable = repunits[:8]
    result = sum_patterns(usable)
    index = 120 - N
    print(result[index])
elif N <= 165:
    usable = repunits[:9]
    result = sum_patterns(usable)
    index = 165 - N
    print(result[index])
elif N <= 220:
    usable = repunits[:10]
    result = sum_patterns(usable)
    index = 220 - N
    print(result[index])
elif N <= 286:
    usable = repunits[:11]
    result = sum_patterns(usable)
    index = 286 - N
    print(result[index])
elif N <= 364:
    result = sum_patterns(repunits)
    index = 364 - N
    print(result[index])
