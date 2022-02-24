input_file = "advent-of-code/2021/day-02-input.txt"
depth = 0
distance = 0
aim = 0

# data_file: open input_file as read-only
with open(input_file, 'r') as data_file:
    # for each line in data_file, split the line into two
    for line in data_file:
        temp_list = line.split(" ")
        if temp_list[0] == "forward":
            distance += int(temp_list[1])
        elif temp_list[0] == "up":
            depth -= int(temp_list[1])
        else:
            depth += int(temp_list[1])

# part 1
print(depth * distance)