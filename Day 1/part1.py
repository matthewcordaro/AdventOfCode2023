def main():
    output_sum = 0
    # read in input.txt
    with open('input.txt', 'r') as f:
        for line in f:
            # get first (10s place) and last (1s place) character that is a number in line and add to sum
            for char in line:
                if char.isdigit():
                    output_sum += int(char) * 10
                    break
            for char in reversed(line):
                if char.isdigit():
                    output_sum += int(char)
                    break
    print(output_sum)
    # write sum to output.txt
    with open('output.txt', 'w') as f:
        f.write(str(output_sum))


if __name__ == '__main__':
    main()
