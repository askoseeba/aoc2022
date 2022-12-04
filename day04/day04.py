fname = "input-test.txt"
fname = "input.txt"

with open(fname) as f:
    data = [[list(map(lambda n: int(n), sections.split("-"))) for sections in pair.split(',')] for pair in f.read().strip().split("\n")]

deflated = [(set(range(s1[0], s1[1] + 1)), set(range(s2[0], s2[1] + 1)))for s1, s2 in data]

print("Part 1:", sum([s1.issubset(s2) or s2.issubset(s1) for s1, s2 in deflated]))
print("Part 2:", sum([len(s1 & s2) > 0 for s1, s2 in deflated]))

