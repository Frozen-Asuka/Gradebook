#This file manipulates values for a sample gradebook using lists
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Create a list called subjects and fill it with classes
subjects = ["physics", "calculus", "poetry", "history"]

# Create a list for grades
grades = [98, 97, 85, 88]

# Create a 2D list
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# Print the gradebook list

print(gradebook)
# Create a variable to store a new class called computer science and a score of 100
new_grades = ["computer science", 100]

# Append the new list items to gradebook
gradebook.append(new_grades)
print(gradebook)

# Create a variable to hold values for another class and its score
next_grade = ["visual arts", 93]

# append next_grade to gradebook
gradebook.append(next_grade)
print(gradebook)

# Change the grade in visual arts and add five point to it
gradebook[5][1] = 98
print(gradebook)

# Remove the grade from you poetry class
gradebook[2].remove(gradebook[2][1])
print(gradebook)

# Add the value "pass" to the poetry class
gradebook[2] = ["poetry"]
gradebook[2].append("Pass")
print(gradebook)

# Create a new variable called full_gradebook that combines last_semester_gradebook anf gradebook

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)