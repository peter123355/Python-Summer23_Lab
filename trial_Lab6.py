class Student:
    Scores = {}

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def getScores(self, file):
        answer_key = [line.strip() for line in open("answers.txt", 'r')]
        student_answers = [line.strip().split(',') for line in open(file, 'r')]
        total_score = 100

        for record in student_answers:
            if record[0].lower() == self.getName().lower():
                for i in range(1, len(record)):
                    if answer_key[i - 1] != record[i]:
                        total_score -= 10

        Student.Scores[self.getName()] = total_score

    def getName(self):
        return self.name

    def getGrade(self):
        return self.grade

    @staticmethod
    def sortDict():
        return sorted(Student.Scores.items())

    @staticmethod
    def getAverageGrade(student_list):
        total = sum(student.getGrade() for student in student_list)
        return round(total / len(student_list), 1)

    @staticmethod
    def getGradeRange(student_list):
        grades = [student.getGrade() for student in student_list]
        grade_range = max(grades) - min(grades) if len(grades) > 1 else 0
        return grade_range

student_objs = [
    Student('Sammy Student', 65),
    Student('Betty Sanchez', 90),
    Student('Alice Brown', 100),
    Student('Tom Schulz', 50),
    Student('Peter Alex', 80),
]

# Process data.txt
for student in student_objs:
    student.getScores("data.txt")

sortList = Student.sortDict()

for k, v in sortList:
    print(k.title(), "has Old score:", v)
    old_score = v

    # Calculate grade range for the student
    grade_range = Student.getGradeRange([student for student in student_objs if student.getName().lower() == k.lower()])

    # Process data1.txt
    for student in student_objs:
        if student.getName() == k:
            student.getScores("data1.txt")
            break

    sortList = Student.sortDict()

    # Print New score for the student
    new_score = None
    for k, v in sortList:
        if student.getName() == k:
            new_score = v
            break

    # Calculate average grade for the student
    average_grade = Student.getAverageGrade([student for student in student_objs if student.getName().lower() == k.lower()])

    print(k.title(), "has New score:", new_score)
    print("Average Grade:", average_grade)
    print("Grade Range:", grade_range, end="\n\n")

# Calculate overall average grade and grade range
all_student_grades = [student.getGrade() for student in student_objs]
overall_average_grade = Student.getAverageGrade(student_objs)
overall_grade_range = Student.getGradeRange(student_objs)

print("\nOverall Average Grade:", overall_average_grade)
print("Overall Grade Range:", overall_grade_range)
