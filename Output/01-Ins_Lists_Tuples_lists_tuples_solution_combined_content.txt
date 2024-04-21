# Create a variable and set it as a list
info_list = ["Samar", 25, "Kyra", 20]
print(info_list)

# Methods for accessing parts of a list

# Return the value of a list at a given index
print(info_list[0])
print(info_list[-1])

# Return the index of the first object with a matching value
print(info_list.index("Kyra"))

# Return a list slice [index_start:index_end]
print(info_list[2:4])
print(info_list[1:])
print(info_list[:2])

# Methods for modifying a list

# Add an element onto the end of a list
info_list.append("Kamau")
print(info_list)

# Change a specified element within a list at the given index
info_list[3] = 85
print(info_list)

# Remove a specified object from a list
info_list.remove("Kamau")
print(info_list)

# Remove the object at the index specified
info_list.pop(0)
info_list.pop(0)
print(info_list)

# Functions for accessing information about a list
# Define a list named scores
scores = [92, 87, 68, 75, 96]

# Return the max (or highest value) item in a list
print(f"Max score: {max(scores)}")

# Return the min (or lowest) item in a list
print(f"Min score: {min(scores)}")

# Return the sum of the items in a list
print(f"Sum score: {sum(scores)}")

# Return the length of the list
print(f"Length of score list: {len(scores)}")

# Use sum and len to calculate average
average_score = sum(scores) / len(scores)
print(f"Average score: {average_score}")

# Create a tuple, a sequence of immutable Python objects that cannot be changed
info_tuple = ("Python", 100, 4.65, False)
print(info_tuple)

# Information functions also work on tuples, provided they contain valid data
# types
names_tuple = ("Melanie", "Jacinta", "Yindi", "Li")

print(len(names_tuple))
print(max(names_tuple))
print(min(names_tuple))

guests_tuple = (3, 5, 2, 4, 3)
print(sum(guests_tuple))
