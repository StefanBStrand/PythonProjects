#  Using functions with lists in python

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
# Extend function: allows you to append a list to another list
friends.extend(lucky_numbers)  # lucky_numbers appended to friends
print(friends)

friends.append("Daniel")  # Append function adds element to the back of the list.
print(friends)

#  insert function is another function, takes 2 parameters,
#  the index position you want, and the value for that posisiton.
friends.insert(1, "Kelly")
print(friends)
#  Inserting new data into position 1 will be pushed off to the right (higher index positions)