################################
# https://github.com/TsheringDorj/03230373_BIA101_CAP3
# Tshering Dorji
# BBI"B"
# 
################################
# REFERENCES
###https://stackoverflow.com/questions/14939953/sum-the-digits-of-a-number
##https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-56.php
##https://codereview.stackexchange.com/questions/135392/2-sum-problem-on-a-range-in-python###
################################
# SOLUTION

# Read the input.txt file
def read_input(filename):# code here to read your input file
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

# solution
def calculate_sum(lines):
    total_sum = 0
    for line in lines:
        try:
            first_digit = int(line[0])
            last_digit = int(line[-2])
            number = int(str(first_digit) + str(last_digit))
            total_sum += number
        except ValueError:
            # Skip lines that cannot be converted to integers
            continue
    return total_sum

def print_solution(filename, total_sum):
    # print your solution to output as: 
    # "The total sum of from the given input file <file name> is <your answer>"
    print(f"The total sum from the given input file {filename} is {total_sum}")

# Other parts of code here to run your functions and printing of the required solution.
filename = "373.txt"
lines = read_input(filename)
total_sum = calculate_sum(lines)
print_solution(filename, total_sum)
