def enroll_student(*students, min_grade=50, department='Computer Science', **kwargs):
    print(f'Min grade: {min_grade}')
    print(f'Department: {department}')
    print('\nEnrolled Students:')
    for student in students:
        print(f' - {student}')
    print('\nAdditional information:')
    for k, v in kwargs.items():
        print(f'{k} : {v}')
    print('End of enrollment.')

def main():
    enroll_student('Christos', 'Marinos', min_grade=70, academic_year=2025, semester='Fall')

if __name__ == '__main__':
    main()