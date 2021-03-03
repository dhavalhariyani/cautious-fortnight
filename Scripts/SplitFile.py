#Split big file into small files based on lines per file

lines_per_file = input("How many lines to keep in one file? : ")
smallfile = None
file_name = input("Enter Your File Name (Without extension) : ")

with open(file_name+'.txt') as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'file_name_small_file_{}.txt'.format(lineno + lines_per_file)
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()