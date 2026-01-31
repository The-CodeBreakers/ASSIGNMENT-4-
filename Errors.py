try:
    file = open("sample.txt", "r")
    for line in file:
        print(line.strip())
    file.close()
except FileNotFoundError:
    print("Error: sample.txt file does not exist.")
