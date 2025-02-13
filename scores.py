def readSingleStudentScores(file_name):
    student_scores = {}
    with open(file_name, "r") as file:
        for line in file:
            data = line.strip().split(",")
            name = data[0]  
            scores = list(map(int, data[1:])) 
            student_scores[name] = scores
        return student_scores


def print_scores(subject,students_gpa):
    print("Gpa for subject "+subject)
    for name,scores in students_gpa.items():
        print(f"{name} : {scores}") 
    print("\n")

def write_scores(subject,students_gpa):
    with open("gpa.txt",'a') as file:
        file.writelines("Gpa for subject "f"{subject}\n")
        for name,scores in students_gpa.items():
            file.writelines(f"{name} : {scores}\n")
        file.writelines("\n") 

def computeGPAfromscores(file_name):
    students_gpa = {}
    student_scores = readSingleStudentScores(file_name)
    for name,scores in student_scores.items():
        students_gpa[name]=sum(scores)/len(scores)
    return students_gpa


file_dict = {"maths":"student-scores - math.csv","physics":"student-scores - Physics.csv","chemistry":"student-scores - Chemistry.csv"}
for subject,file in file_dict.items():
    gpa = computeGPAfromscores(file)
    write_scores(subject,gpa)