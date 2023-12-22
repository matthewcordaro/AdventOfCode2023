def main():
    max_cubes = {"red": 12, "green": 13, "blue": 14}
    line_number = 0
    game_sum = 0
    # read in input.txt
    with open('input.txt', 'r') as f:
        for line in f:
            line_number += 1
            # get the index of the first ':' character
            index_of_colon = line.find(':')
            # split by ';' character after the index of the first ':' character
            turns = line[index_of_colon + 1:].split(';')
            valid = True
            for turn in turns:
                # split by ',' character
                turn = turn.split(',')
                colors = {"red": 0, "green": 0, "blue": 0}
                for balls in turn:
                    # balls is a string that consists of a number followed by a color, like "12 blue" or "1 red"
                    balls = balls.split()
                    number = int(balls[0])
                    color = balls[1]
                    # insert into colors dictionary
                    colors[color] = number
                # check if any colors in the dictionary is greater than MAX_CUBES[color]
                for color in colors:
                    if colors[color] > max_cubes[color]:
                        valid = False
            if valid:
                print(line_number, "is valid")
                game_sum += line_number
    # write sum to output.txt
    with open('output.txt', 'w') as f:
        f.write(str(game_sum))


if __name__ == '__main__':
    main()
