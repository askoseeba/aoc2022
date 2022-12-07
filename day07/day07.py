fname = "input-test.txt"
fname = "input.txt"

with open(fname) as f:
    data = [line for line in f.read().strip().split("\n") if line[:4] not in {"$ ls", "dir "}]

sizes = []

def dir_size(data):
    size = 0
    data.pop(0) # Remove the cd command
    while True:
        if len(data) == 0:
            break
        if data[0][0] != "$":
            size += int(data[0].split(" ")[0])
            data.pop(0)
        elif data[0] == "$ cd ..":
            data.pop(0)
            break
        else: # It is a cd to subdirectory
            size += dir_size(data)
    sizes.append(size)
    return size

sizes.append(dir_size(data))
print("Part 1:", sum([size for size in sizes if size <= 100000]))
print("Part 2:", min([size for size in sizes if size > 30000000 - (70000000 - max(sizes))]))

