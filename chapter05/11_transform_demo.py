def main():
    grades = [7, 5, 9, 10, 3]

    upscaled_grades = [grade + 1 if grade < 10 else grade for grade in grades]

    upscaled_grades2 = list(map(lambda grade: grade + 1 if grade < 10 else grade, grades))

    passed_grades = [grade for grade in grades if grade >= 5]

    passed_grades2 = list(filter(lambda grade: grade >= 5, grades))

if __name__ == '__main__':
    main()