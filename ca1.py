
student_rollno = [112, 113, 112, 114,115,115,116,117,117]
new_data=set()
print("Data with Duplicate Roll Numbers:",student_rollno)
for rollno in student_rollno:
    new_data.add(rollno)
new_data_list = list(new_data)
print("New Data Without Duplicacy:",new_data_list)
