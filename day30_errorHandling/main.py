#FileNotFound


try:
    file = open("/home/rishells/rcdev/100daysOfPython/day30_errorHandling/a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sdsd"])

except FileNotFoundError:
    file = open("/home/rishells/rcdev/100daysOfPython/day30_errorHandling/a_file.txt","w")
    file.write("Something")


except KeyError as error_message:
    print(f"That key {error_message} does not exist.")

else:
    content = file.read()
    print(content)

finally:
    file.close()

#Key Error
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

#IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)

# 4 key words handling exceptions: try, except, else, finally
# try: something that might cause an exception
# except: Do this if there was an exception
# else: Do this if there were no exceptions
# finally: Do this no matter what happens