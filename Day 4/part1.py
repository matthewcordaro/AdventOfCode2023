def main():

    # a game is a tuple containing a card number, a tuple of 5 winning numbers, and a tuple of 8 player numbers
    games: list[tuple[int, set[int, int, int, int, int], set[int, int, int, int, int, int, int, int]]] = []
    # for each line in the input.txt file, insert into games list
    with open('input.txt') as f:
        for card_num, card in enumerate(f):
            # remove the text before the colon
            card = card.split(':')[1]

            # split at the loc of the pipe
            winning_numbers_str, player_numbers_str = card.split('|')

            # convert both winning and player numbers to set of ints
            winning_numbers = set(map(int, winning_numbers_str.split()))
            player_numbers = set(map(int, player_numbers_str.split()))

            # insert the game into the games list
            games.append((card_num, winning_numbers, player_numbers))

    points: int = 0
    for card_num, winning_numbers, player_numbers in games:
        # get the intersection of matching numbers
        matching_numbers = winning_numbers.intersection(player_numbers)
        # get 2x points per matching number if there are matching numbers
        if len(matching_numbers) > 0:
            points += 2 ** (len(matching_numbers)-1)

    # write points to output.txt
    with open('output.txt', 'w') as f:
        f.write(str(points))


if __name__ == '__main__':
    main()
