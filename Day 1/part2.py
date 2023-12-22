def find_all_instances(string, substring):
    start = 0
    while True:
        start = string.find(substring, start)
        if start == -1: return
        yield start
        start += len(substring)


def main():
    output_sum = 0
    list_of_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5",
                       "6", "7", "8", "9"]
    conversion_table = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
                        "nine": 9, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    numbers_each_line = []
    # read in input.txt
    with open('../Day 2/input.txt', 'r') as f:
        for line in f:
            # line never has space characters so split will not work
            # append to list spelled out numbers in the line as a list of tuples (index, word)
            numbers_in_the_line = []
            for word in list_of_numbers:
                # index of word in line
                locations = find_all_instances(line, word)
                value = conversion_table.get(word)
                for index in locations:
                    numbers_in_the_line.append((index, value))
            numbers_in_the_line.sort(key=lambda x: x[0])
            tens = numbers_in_the_line[0][1] * 10
            ones = numbers_in_the_line[-1][1]
            # append to numbers_each_line
            numbers_each_line.append(tens + ones)
    print(numbers_each_line)
    # add up all numbers in numbers_each_line
    for number in numbers_each_line:
        output_sum += number
    print(output_sum)
    # write sum to output.txt
    with open('../Day 2/output.txt', 'w') as f:
        f.write(str(output_sum))


if __name__ == '__main__':
    main()
