def upscale_grades(grades):
    return [grade + 1 if grade < 10 else grade for grade in grades]

def filter_passed(grades):
    return [grade for grade in grades if grade >= 5]

def categorize_grades(grades):
    passed = [grade for grade in grades if 5 <= grade < 10]
    failed = [grade for grade in grades if grade < 5]
    honors = [grade for grade in grades if grade == 10]
    return failed, passed, honors

def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

def main():
    pass

if __name__ == '__main__':
    main()