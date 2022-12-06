test1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
test2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
test3 = "nppdvjthqldpwncqszvftbrmjlhg"
test4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
test5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

with open("input.txt") as f:
    data = f.read().strip()

#data = test5

def search_start(marker_size):
    for i in range(marker_size, len(data)):
        if len(set(data[i - marker_size : i])) == marker_size:
            return i

print("Part 1:", search_start(4))
print("Part 2:", search_start(14))

