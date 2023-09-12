#  Working with lists in python
#  A list is a structure which allows us to store and organize of larger quantities of data

friends = ["Tom", "Jenny", "Anna", "John", "Jim"]
#  You can store any piece of information into a list, strings, numbers and boolean
print(friends)
print(friends[1])  # Prints the desired index position in the list
print(friends[1:])  # Using the colon prints all the values from index 1 and after
print(friends[-1])  # Negative values prints from the back of the list. 1st position from
# the back is index -1
friends[1] = "Kevin"  # Updating/modifying values in within the list
print(friends)