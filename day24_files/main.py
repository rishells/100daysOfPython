#file = open("day24_files\my_file.txt") # Relative path
# with open("G:\\My Drive\\rcdev\Python\\100daysOfPython\\day24_files\\my_file.txt") as file# Path
#     contents = file.read()
#     print(contents)
#     #file.close() With "with" you can avoid using close


with open("day24_files\my_file3.txt","a") as file:
    for i in range(5000):
        file.write(f"\nNew text written from python line: {i}")


