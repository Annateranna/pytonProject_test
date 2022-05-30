def dic_students():
    student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012',
                   'S013']
    student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti',
                     'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman',
                     'Tom Hardy']
    student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]

    '''
    dict1 = dict(zip(student_ids, zip(student_names, student_grades)))
    result = [{i: {[*dict1[i]][0]: [*dict1[i]][1]}} for i in student_ids]
    '''
    result = [{x: {y: z}} for x, y, z in zip(student_ids, student_names, student_grades)]

    print(result)