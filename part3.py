# def grade_analyzer():          task 1
#     grades = [88, 80, 70, 60]
#     print(sum(grades) / (len(grades)))

# grade_analyzer()

# def grade_analyzer():              #task 2
#     grades = [88, 80, 70, 60]
#     print(max(grades))
#     print(min(grades))

# grade_analyzer()

def grade_analyzer():
    grades = [88, 80, 70, 60, 90]
    for grade in grades:
        if grade <= 60:
            print(grade, " D")
        elif grade <=79:
            print(grade, " C")
        elif grade <= 89:
            print(grade, " B")
        else:
            print(grade, " A")

grade_analyzer()