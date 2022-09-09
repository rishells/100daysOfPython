#file = open("day24_files\my_file.txt") # Relative path
# with open("G:\\My Drive\\rcdev\Python\\100daysOfPython\\day24_files\\my_file.txt") as file# Path
#     contents = file.read()
#     print(contents)
#     #file.close() With "with" you can avoid using close

PLACEHOLDER = "[name]"

with open("./day24_files/Mail Merge Project/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines() # readlines return as a list
    print(names)

with open("day24_files/Mail Merge Project/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        #print(new_letter)
        with open(f"day24_files/Mail Merge Project/Output/ReadyToSend/letter_for{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)



