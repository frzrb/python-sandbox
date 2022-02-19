# input_file: string path of the input file for data
# data_array: target data array from input_file
# cute_counter: use this as a counter during the for each loop over the lines in input_file, will total the length of the array
input_file = "test/test-file.txt"
data_array = []
cute_counter = 0

# data_file: open input_file as read-only
with open(input_file, 'r') as data_file:
    # for each line in data_file
    # cast the line as integer, append to data_array
    # increment cute_counter
    for line in data_file:
        data_array.append(int(line))
        cute_counter += 1

# use the len() function to get the number of elements in the data_array_size array
data_array_size = len(data_array)

# output cute_counter (as a string) and data_array_size (as a string)
print("I count " + str(cute_counter) + " numbers. The array is " + str(data_array_size))

# evaluate if cute_counter is equal to data_array_size (they always should be)
if (cute_counter == data_array_size):
    print("They match!")
else:
    print("Something's wrong!")
    exit()
