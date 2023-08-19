S = list(input())

aeiou = set(["a", "e", "i","o", "u"])

print("".join(list(filter(lambda x: x not in aeiou, S))))

