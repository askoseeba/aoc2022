fname = "input-test.txt"
fname = "input.txt"

def priorities(items):
    return [ord(item) - ord("a") + 1 if item.islower() else ord(item) - ord("A") + 27 for item in items]

with open(fname) as f:
    data = [rs for rs in f.read().strip().split("\n")]

rucksacks = [list(set(rs[:int(len(rs) / 2)]) & set(rs[int(len(rs) / 2):]))[0] for rs in data]
print("Part 1:", sum(priorities(rucksacks)))

groups = [list(set(data[i * 3]) & set(data[i * 3 + 1]) & set(data[i * 3 + 2]))[0] for i in range(int(len(data) / 3))]
print("Part 2:", sum(priorities(groups)))

