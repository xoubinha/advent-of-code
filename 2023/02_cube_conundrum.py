
BAG = {"red": 12,
       "green": 13,
       "blue": 14
       }

def read_input_file(input_path):
    with open(input_path) as file:
        return file.read().splitlines()

def parse_game(game):
    game_info, game_sets = game.split(": ")
    _, game_id = game_info.split(" ")
    game_sets = [game_set.split(", ") for game_set in game_sets.split("; ")]
    return int(game_id), game_sets

def check_if_game_set_is_impossible(game_set):
    for cubes in game_set:
        number, color = cubes.split(" ")
        if BAG[color] < int(number):
            return True
    return False

def check_if_game_is_possible(game):
    for game_set in game:
        game_set_is_impossible = check_if_game_set_is_impossible(game_set)  
        if not game_set_is_impossible:
            game_is_possible = True
        else: 
            game_is_possible = False
            break
    return game_is_possible

def part_one(games):
    possible_games_ids = []
    for game in games:
        game_id, game = parse_game(game)
        game_is_possible = check_if_game_is_possible(game)
        if game_is_possible: 
            possible_games_ids.append(game_id)
    return sum(possible_games_ids)


if __name__ == '__main__':
    FILEPATH = "./data/02_cube_conundrum.txt"
    games = read_input_file(FILEPATH)
    part_one_solution = part_one(games)
    print(f"Part 1 - {part_one_solution}")

