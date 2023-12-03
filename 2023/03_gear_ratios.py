import re 

def read_input_file(input_path):
    with open(input_path) as file:
        return file.read().splitlines()

def get_numbers_in_line(line):
    numbers = []
    positions = []
    for match in re.finditer("\d+", line):
        numbers.append(match.group())
        positions.append((match.span()))
    return numbers, positions

def is_adjacent_to_a_symbol(line, start, end):
    return re.findall("[^A-Za-z0-9.]", line[start:end])

def get_possible_adjacency_positions(number_position):
    start_position = number_position[0]
    if start_position != 0:
        start_position -= 1
    end_position = number_position[-1] + 1
    return start_position, end_position

def check_for_symbol_in_adjacency_positions(line, check_start, check_end):
    return is_adjacent_to_a_symbol(line, check_start, check_end)

def check_if_symbol_in_adjacency_positions(lines, check_start, check_end):
    is_adjacent = False
    for line in lines:
        is_adjacent = is_adjacent_to_a_symbol(line, check_start, check_end)
        if is_adjacent:
            return True

def get_lines_to_check(i, engine_schematic):
    lines = []
    lines.append(engine_schematic[i])
    if i!=0:
        lines.append(engine_schematic[i-1])
    if i<len(engine_schematic)-1:
        lines.append(engine_schematic[i+1])
    return lines 
       
def part_one(engine_schematic):
    part_numbers = []
    for i, line in enumerate(engine_schematic):
        numbers, positions = get_numbers_in_line(line)
        if numbers:
            for position, number in zip(positions, numbers):
                lines = get_lines_to_check(i, engine_schematic)
                check_start, check_end = get_possible_adjacency_positions(position)
                is_adjacent = check_if_symbol_in_adjacency_positions(lines, check_start, check_end)
                if is_adjacent:
                    part_numbers.append(int(number))
    return sum(part_numbers)

if __name__ == '__main__':
    FILEPATH = "./data/03_gear_ratios.txt"
    
    engine_schematic = read_input_file(FILEPATH)
    part_one_solution = part_one(engine_schematic)
    print(f"Part 1 - {part_one_solution}")

