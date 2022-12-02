fname = "input-test.txt"
fname = "input.txt"

with open(fname) as f:
    data = [sum([int(cal) for cal in cals.split("\n")]) for cals in f.read().strip().split("\n\n")]

print("Part 1:", max(data))
data.sort()
print("Part 2:", sum(data[-3:]))

