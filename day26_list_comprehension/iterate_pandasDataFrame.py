import pandas

student_dict = {
    "student" : ["Ricardo","Axel","Yadira"],
    "score" : [98,78,67]
}

# Looping through dictionaries:
# for (key,value) in student_dict.items():
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Ricardo":
        print(row.score)