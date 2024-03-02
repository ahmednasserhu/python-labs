from read_student_info import read_student_file
from process_student_info import process_student_data

file_path = "2.2/grades.txt"

student_data = read_student_file(file_path)
process_student_data(student_data)
