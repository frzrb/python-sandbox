# input_file: string path of the input file for data
# data_array: target data array from input_file, for parr 1
# sets_of_three: array for the sets of sums of 3 elements from data_array, for part 2 
# data_count: use this as a counter during the for each loop over the lines in input_file, will total the data_array count
input_file = "advent-of-code/2021/day-01-input.txt"
data_array = []
sets_of_three = []
data_count = 0

# data_file: open input_file as read-only
with open(input_file, 'r') as data_file:
    # for each line in data_file
    # cast the line as integer, append to data_array
    # increment data_count by 1
    for line in data_file:
        data_array.append(int(line))
        data_count += 1

# for loop from the beginning to the index of the last possible set of three (end of the list - 2)
for y in range(0, (data_count - 2)):
    # add current number with the next two numbers, append the sum to the sets_of_three list
    sets_of_three.append(data_array[y] + data_array[y+1] + data_array[y+2])

# up_down_finder(list): function to find if the next number in a list has increased or decreased
def up_down_finder(data_set):
    # down_count: decrement counter
    # up_count: increment counter
    # equal_count: counter when compared numbers are equal
    down_count = 0
    up_count = 0
    equal_count = 0

    # for loop from the second element of array (starting at 1) to the end of the array
    for x in range(1, len(data_set)):
        # if the previous number is greater than the current number, increment down_count
        if data_set[x-1] > data_set[x]:
            # print("decreased from " + str(data_array[x-1]) + " to " + str(data_array[x]))
            down_count += 1
        # if the previous number is less than the current number, increment up_count
        elif data_set[x-1] < data_set[x]:
            # print("increased from " + str(data_array[x-1]) + " to " + str(data_array[x]))
            up_count += 1
        # if it doesn't go up or down, it must be equal. increment equal_count
        else:
            # print("equal")
            equal_count += 1

    # output counts
    print("down count: " + str(down_count) + ". up count: " + str(up_count) + ". equal count: " + str(equal_count))

# part 1
up_down_finder(data_array)
# part 2
up_down_finder(sets_of_three)