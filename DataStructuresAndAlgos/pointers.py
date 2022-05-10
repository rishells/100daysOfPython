# num1 = 11
# num2 = num1

# print("Before num2 value is updated:")
# print("num1 =", num1)
# print("num2 =", num2)

# print("\nnum1 points to:", id(num1))
# print("num2 points to:", id(num2))



# num2 = 22

# print("After num2 value is updated:")
# print("num1 =", num1)
# print("num2 =", num2)

# print("\nnum1 points to:", id(num1))
# print("num2 points to:", id(num2))


# Integers are immutable , once you create one you cannot modify in that space of memory


# Example with dictionaries, dictionaries are mutable, so it means once you reference one value in memory you can change that value that has the reference

dict1 = {
            'value' : 11
        }

dict2 = dict1

print("Before values are updated:")
print(f"dict1 = {dict1}")
print(f"dict2 = {dict2}")

print(f"\ndict1 points to: {id(dict1)}")
print(f"\ndict2 points to: {id(dict2)}")

dict2['value'] = 22

print("After values are updated:")
print(f"dict1 = {dict1}")
print(f"dict2 = {dict2}")

print(f"\ndict1 points to: {id(dict1)}")
print(f"\ndict2 points to: {id(dict2)}")

    