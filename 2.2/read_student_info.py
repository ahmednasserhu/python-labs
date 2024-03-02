def read_student_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return [line.strip().split() for line in lines]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
