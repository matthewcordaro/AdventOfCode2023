from collections import Counter


def main():
    output = 0  # the output to be written to output.txt
    number_locations: list[tuple[int, int, int, int]] = []  # (number, row, col_left, col_right)
    gear_locations: list[tuple[int, int]] = []  # (row, column)
    # read in input.txt is a NxM matrix of characters
    with open('input.txt', 'r') as f:
        for row, line in enumerate(f):
            line = line.strip()

            # find all whole numbers in the line
            col_left = 0
            while col_left < len(line):
                if not line[col_left].isdigit():
                    col_left += 1
                else:
                    # find the whole number
                    col_right = col_left
                    while col_right < len(line) and line[col_right].isdigit():
                        col_right += 1

                    # add to number_locations
                    number = int(line[col_left:col_right])
                    number_locations.append((number, row, col_left, col_right - 1))

                    # continue on from col_right
                    col_left = col_right + 1
            # find all the '*' gear symbols in the line
            for col, char in enumerate(line):
                if char == "*":
                    gear_locations.append((row, col))

    # find any number_locations that are vertically, horizontally, or diagonally adjacent to any gear_locations and
    # put them in the gear_touching_list
    gear_touching_list: set[tuple[tuple[int, int], int]] = set()
    for number, row, col_left, col_right in number_locations:
        # Bounding for number
        row_top = row - 1
        row_bottom = row + 1
        col_left -= 1
        col_right += 1

        # Find if a gear is on the bounds
        for gear_row, gear_col in gear_locations:
            if row_top <= gear_row <= row_bottom and col_left <= gear_col <= col_right:
                gear_touching_list.add(((gear_row, gear_col), number))

    # find the number of numbers touching each gear
    quantity_of_numbers_touching_gears = Counter(x[0] for x in gear_touching_list)

    pair_dict: dict[tuple[int, int], int] = {}  # a dictionary of gear_location: number
    for gear_location, number in gear_touching_list:
        # only add to output if there are two numbers touching the gear
        if quantity_of_numbers_touching_gears.get(gear_location) == 2:
            # if the gear_location is not in the pair_dict, add it
            if gear_location not in pair_dict:
                pair_dict[gear_location] = number
            # if the gear_location is in the pair_dict, add the two numbers together and remove the gear_location
            else:
                output += number * pair_dict.pop(gear_location)
    # make sure there are only two of each gear number
    # write to output.txt
    with open('output.txt', 'w') as f:
        f.write(str(output))


if __name__ == '__main__':
    main()
