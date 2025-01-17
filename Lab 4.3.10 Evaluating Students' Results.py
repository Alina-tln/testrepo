class StudentsDataException (Exception):
    pass

class BadLine (StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string

class FileEmpty (StudentsDataException):
    def __init__(self):
        super().__init__(self)

from os import strerror

dictinary = {}
txt = input('Enter the file: ')
try:
    file = open('C:\\Users\\Random\\Desktop\\Python_files\\' + txt, 'rt')
    lines = file.readlines()
    file.close()
    if len(lines) == 0:
        raise FileEmpty
    for i in range(len(lines)):
        line = lines[i]
        columns = line.split()
        # if columns != 3:
        #     raise BadLine (i + 1, line)
        student = columns[0] + ' ' + columns[1]
        points = float(columns[2])

        try:
            dictinary[student] += points
        except KeyError:
            dictinary[student] = points
    for student in sorted(dictinary.keys()):
        print(student, ' ', dictinary[student])


except IOError as e:
    print('I/O error occurred:', strerror(e.errno))
except BadLine as e:
    print('Wrong line#' + str(e.line_number) + ' in sourse file: ' + e.line_string)
except FileEmpty:
    print('Source file empty')