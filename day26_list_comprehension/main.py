numbers = [1,2,3,4,5]
new_list = []
for n in numbers:
    add_1 = n +1
    new_list.append(add_1)

#print(new_list)


#Using list comprehension
#[new_item for item in list/range ]

new_list2 = [n + 1 for n in numbers]

name = "Ricardo"
new_name_list = [letter for letter in name]

# LC using range function
number_list = [num * 2 for num in range(1,5)]

#LC using validation and modification to the return object
names = ['Ricardo','Axel','Yadira','Rac','Toto']
long_names = [name.upper() for name in names if len(name)> 4]

#Exercise # 1 Squared numbers

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num**2 for num in numbers]

#Exercise # 2 Even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

with open("file1.txt","r") as f:
    mylist1 = f.read().splitlines()

with open("file2.txt","r") as f:
    mylist2 = f.read().splitlines()

common_numbers = [int(num) for num in mylist1 if num in mylist2]


