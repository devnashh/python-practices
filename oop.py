class Students:
    def __init__(pupil, name, age):
        pupil.name = name
        pupil.age = age
        pupil.grades = []

    def show_info(pupil):
        print(f"Student Name: {pupil.name}")
        print(f"Student Age: {pupil.age}")
        print(f"Student Grades: {pupil.grades}")
    
    def add_grade(pupil, grade):
        pupil.grades.append(grade)

    def compute_grade(pupil):
        total = sum(pupil.grades)
        count = len(pupil.grades)
        avg = total / count
        print(f"Total Average: {avg}")
    
pupil1 = Students("Dudong", 10)
pupil1.add_grade(80)
pupil1.add_grade(90)
pupil1.add_grade(95)
pupil1.show_info()
pupil1.compute_grade()
        
    
    
        



