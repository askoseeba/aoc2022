import copy

fname = "input.txt"
#fname = "input-test.txt"

with open(fname) as f:
    sdata, pdata = f.read().split("\n\n")

# Parse stacks of crates:
sdata = sdata.split("\n")
num_stacks = int(sdata[-1].strip().split("   ")[-1])
sdata = sdata[:-1]
sdata.reverse()
stacks = [[] for i in range(num_stacks)]
for layer in sdata:
    for i in range(num_stacks):
        crate = layer[1 + i * 4]
        if crate != " ":
            stacks[i].append(crate)
stacks_backup = copy.deepcopy(stacks) # Needed for part 2

# Rearrange crates:
pdata = [[int(move.split(" ")[i]) for i in [1, 3, 5]] for move in pdata.strip().split("\n")]

for move in pdata:
    for n in range(move[0]):
        stacks[move[2] - 1].append(stacks[move[1] - 1].pop())

print("Part 1:", "".join([stack[-1] for stack in stacks]))

stacks = stacks_backup

for move in pdata:
    stacks[move[2] - 1] += stacks[move[1] - 1][-move[0]:]
    stacks[move[1] - 1] = stacks[move[1] - 1][:-move[0]]

print("Part 2:", "".join([stack[-1] for stack in stacks]))

