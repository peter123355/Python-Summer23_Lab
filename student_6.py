class Student:

    Scores = {}

    # initializing the constructor method

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def getScores(self):

        answer_key = []
        # read into answer_key list, the answer key from file
        answer_key = [line.strip() for line in open("answers.txt", 'r')]

        student_answers = []
        # read into student_answers list, student answers from file
        student_answers = [line.strip().split(',') 
                           for line in open("data.txt", 'r')]
        
        total_score = 100

        # additional code statements here for the above function
         #---started the loop processing logic here---#
        for student in student_answers:
            if student[0]==self.getName():
                for i in range(len(answer_key)):
                    if answer_key[i]!=student[i+1]:
                        total_score -=10
        #---ended the loop processing logic here---#



        #---continue the class definition#

        Student.Scores[self.getName()] = total_score

    def getName(self):
        return self.name

    @staticmethod
    def sortDict():
        return sorted(Student.Scores.items())

    #---end the class definition#

student_objs = [

    Student('Sammy Student', 65),
    Student('Betty sanchez', 45),
    Student('Alice brown', 100),
    Student('tom Schulz', 50),
    Student('Peter Alex',50)
]

for index in range(len(student_objs)):
    student_objs[index].getScores()

sortList = Student.sortDict()

for k, v in sortList:
    print(k, "has old score:", v)
  
