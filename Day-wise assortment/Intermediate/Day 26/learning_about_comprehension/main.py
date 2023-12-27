import pandas


# # List Comprehension
# # Filtering out even numbers
# numbers = [1, 4, 2, 9, 6, 3]
# even_numbers = [num for num in numbers if num % 2 == 0]  # Filter, even numbers
# print(even_numbers)
# # Output: [4, 2, 6]


# Dictionary Comprehension
# new_dict = {key_expression : value_expression for element in iterable if condition}
# But if you wish to iterate through both key as well as values at the same time
# new_dict = {key_expression: value_expression for key, value in original_dict.items() if condition}


# Iterating through Dataframe
# First let's create a dataframe
students_data = {
    "students": ["Rahul", "Keshav", "Priya"],
    "scores": [76, 53, 52],
}
students_data = pandas.DataFrame(students_data)
print(students_data)

# Working with a Dataframe is similar to working with dictionaries in python
# Column names act as key and column data acts as values

# Like if you want to loop through keys or say column names what you can do is
print("\nGetting just the column names")
for column_name in students_data:
    print(column_name)

# Now if you want to get each of the column printed
print("\nGetting each column printed")
for (key, value) in students_data.items():
    print(value)

# If you want to get hold of each row
# Pandas has an inbuilt method i.e., .iterrows()
print("\nGetting hold of rows")
for (index, row) in students_data.iterrows():  # index gets hold of the row in which we are present
    print(row)
    # Now if we only wish to print only a certain column data row-wise
    # print(row.students)
    # Is it possible to get only the columns we wanted to be printed?
    # The Answer is yes!!
