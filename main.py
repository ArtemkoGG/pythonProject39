with open("input.txt") as infile, open("output.txt", "w") as outfile:
    outfile.writelines(infile)

print("Файл оброблено.")