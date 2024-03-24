import random
# List Comprehension - it helps to copy a list to another object in only 1 line of code
# new_list = [new_item for item in list]
numbers = [1,2,3]
new_list = [n+1 for n in numbers]
print(new_list)

name = "Ben"
letters_list = [letter for letter in name]
print(letters_list)

range(1,5)
range_list = [num * 2 for num in range(1,5)]
print(range_list)

# Conditional List Comprehension - it helps to copy a list to another object in only 1 line of code
# new_list = [new_item for item in list if test]
names = ["Alex" , "Beth" , "Caroline" , "Dave" , "Elanor" , "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)


# Dictionary Comprehension - it helps to copy a dictionary to another object in only 1 line of code
#                            it's a way of creating a dictionary using this shortened syntax
# copy from list
# new_dict = {new_key:new_value for item in list}
# copy from another dictionary
# new_dict = {new_key:new_value for (key,value) in dict.items()}

names = ["Alex" , "Beth" , "Caroline" , "Dave" , "Elanor" , "Freddie"]

students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)

passed_students = {student:score for (student,score) in students_scores.items() if score >= 60}
print(passed_students)




student_dict = {
    "student":["Angela", "James","Lily"],
    "score":[56,76,98]
}
#looping through dictionaries
# for (key,value) in student_dict.items():
#     print(value)


#using pandas
import pandas 

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#loop through a data frame
# for (key,value) in student_data_frame.items():
#     print(value)

#loop through rows of data frame
for (index,row) in student_data_frame.iterrows():
    print(row)
    # print(row.student)
    # print(row.score)
