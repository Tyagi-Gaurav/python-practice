import random

names = ["Gaurav", "Shyam", "Ram", "Laxman", "Raavan", "Jack"]

student_scores = {name: random.randint(10, 100) for name in names}
print(student_scores)

passed_students = {key: value for (key, value) in student_scores.items() if value > 30}
print(passed_students)

student_dict = {
    "student": ["Gaurav", "Jack", "Shyam"],
    "score": [90, 91, 92]
}

for (key, value) in student_dict.items():
    print (key)
    print (value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print (student_data_frame)

#Loop through dataframe
# for (key, value) in student_data_frame.items():
#     print (value)

for (index, row) in student_data_frame.iterrows():
    print (index)
    print (row)
    print (row.student)
    print (row.score)