#This will combine all txt files into one result.txt file

import fileinput
import glob

file_list = glob.glob("*.txt")

with open('result.txt', 'w') as file:
    input_lines = fileinput.input(file_list)
    file.writelines(input_lines)
