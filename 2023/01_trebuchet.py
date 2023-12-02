import re 

def read_input_file(input_path):
    with open(input_path) as file:
        return file.read().splitlines()
    
REPLACE_DICTIONARY = {
    "one": "1", 
    "two": "2", 
    "three": "3", 
    "four": "4", 
    "five": "5", 
    "six": "6",
    "seven":"7", 
    "eight":"8",
    "nine": "9"
}

def find_pattern(calibration, pattern):
    match = re.findall(pattern, calibration)
    return match

def string_to_number(string, replace_dictionary=REPLACE_DICTIONARY):
    if not string.isdigit():
        string = replace_dictionary[string]
    return string
    
def get_solution(calibrations, pattern=r"\d"):
    solution = 0
    for calibration in calibrations:
        match = find_pattern(calibration, pattern)
        if match:
            calibration_value = int(string_to_number(match[0])+string_to_number(match[-1]))
        solution += calibration_value
    return solution

if __name__ == '__main__':
    FILEPATH = "data/01_trebuchet.txt"
    calibrations = read_input_file(FILEPATH)

    part_one_pattern = r"\d"
    part_two_pattern = "(?=(one|two|three|four|five|six|seven|eight|nine|\d))"
    
    part_one_solution = get_solution(calibrations, part_one_pattern)
    part_two_solution = get_solution(calibrations, part_two_pattern)

    print(f"Part 1 - {part_one_solution}")
    print(f"Part 2 - {part_two_solution}")