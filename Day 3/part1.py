def main():
    output = 0
    data = []
    number_locations = []  # a list of tuples (number, row, column)
    symbol_locations = []  # a list of tuples (row, column)
    # read in input.txt is a NxM matrix of characters
    with open('input.txt', 'r') as f:
        for line_number, line in enumerate(f):
            line = line.strip()
            data.append(list(line))
            # find all whole numbers in the line
            col_i = 0
            while col_i < len(line):
                if line[col_i].isdigit():
                    # find the whole number
                    col_j = col_i
                    while col_j < len(line) and line[col_j].isdigit():
                        col_j += 1
                    # add to number_locations
                    number_locations.append((int(line[col_i:col_j]), line_number, col_i))
                    # continue on from col_j
                    col_i = col_j
                else:
                    col_i += 1
            # find all the symbols
            for character_number, char in enumerate(line):
                # if not a period or a digit, append it to symbol_locations
                if char != "." and not char.isdigit():
                    symbol_locations.append((line_number, character_number))
    # find any number_locations that are vertically or horizontally adjacent to any symbol_locations
    for number, number_row, number_column in number_locations:
        # Bounding box for number
        top_bound = number_row - 1
        bottom_bound = number_row + 1
        left_bound = number_column - 1
        right_bound = number_column + len(str(number))
        # Find if any symbol inside or touching bounding box
        for symbol_row, symbol_col in symbol_locations:
            if top_bound <= symbol_row <= bottom_bound:
                if left_bound <= symbol_col <= right_bound:
                    output += number
                    break
    print(output)
    # write to output.txt
    with open('output.txt', 'w') as f:
        f.write(str(output))


if __name__ == '__main__':
    main()
