#!/usr/bin/env python
# coding: utf-8

# In[81]:


class Student:
    students = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.students += [self.grades]
        mean = 0
        
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        summ = 0
        quantity = 0
        for values in self.grades.values():
            summ += sum(values)
        for values in self.grades.values():            
            quantity += len(values)
        if quantity != 0:
            mean = round((summ / quantity),2)
            self.mean = mean
            info = f'имя: {self.name}\nфамилия: {self.surname}\nсредняя оценка за домашние задания: {mean}\nКурсы в процессе извучения: {self.courses_in_progress}\nЗавершённые курсы: {self.finished_courses}'
        else:
            info = f'имя: {self.name}\nфамилия: {self.surname}\nКурсы в процессе извучения: {self.courses_in_progress}\nЗавершённые курсы: {self.finished_courses}'
        return info
    
        
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    lecturers = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        Lecturer.lecturers += [self.grades]
        mean = 0
    
    def __str__(self):
        summ = 0
        quantity = 0
        for values in self.grades.values():
            summ += sum(values)
        for values in self.grades.values():            
            quantity += len(values)
        if quantity != 0:
            mean = round((summ / quantity),2)
            self.mean = mean 
            info = f'имя: {self.name}\nфамилия: {self.surname}\nсредняя оценка за лекции: {mean}'
        else:
            info = f'имя: {self.name}\nфамилия: {self.surname}'
        return info
        
        
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        rev_info = f'имя: {self.name}\nфамилия: {self.surname}'
        return rev_info

def mean_grade_hw(course):
    summ0 = []
    summ = 0
    for stu in Student.students:
        if course in stu:
            summ0 += [(sum(stu[course]))]
    summ = sum(summ0)
    t = []
    qua = 0
    for stu in Student.students:
        if course in stu:
            t += [len(stu[course])]
    qua += sum(t)
    mean = f'Средняя оценка домашнего задания по дисциплине {course} = {round((summ/qua),2)}'
    return mean

def mean_grade_lec(course):
    summ0 = []
    summ = 0
    for lec in Lecturer.lecturers:
        if course in lec:
            summ0 += [(sum(lec[course]))]
    summ = sum(summ0)
    t = []
    qua = 0
    for lec in Lecturer.lecturers:
        if course in lec:
            t += [len(lec[course])]
    qua += sum(t)
    mean = f'Средняя оценка лекций по дисциплине {course} = {round((summ/qua),2)}'
    return mean

#best_student = Student('Ruoy', 'Eman', 'your_gender')
#best_student.courses_in_progress += ['Python']
 
#cool_mentor = Mentor('Some', 'Buddy')
#cool_mentor.courses_attached += ['Python']
 
#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)
 
#print(best_student.grades)
reviewer1 = Reviewer('Vladimir', 'Levin')
reviewer1.courses_attached += ['Python', 'Git']

student1 = Student('Joseph', 'Stalinov', 'male')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']

lecturer1 = Lecturer('Nikita', 'Khruschin')
lecturer1.courses_attached += ['Python', 'Git']

reviewer2 = Reviewer('Leonid', 'Vrezhnev')
reviewer2.courses_attached += ['Python', 'Введение в программирование']

student2 = Student('Yuri', 'Andropenko', 'male')
student2.courses_in_progress += ['Python', 'Git', 'Введение в программирование']
student2.finished_courses += ['История партии']

lecturer2 = Lecturer('Konstantin', 'Chernenkov')
lecturer2.courses_attached += ['Python', 'Введение в программирование']

reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer1.rate_hw(student1, 'Git', 8)
reviewer2.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student2, 'Введение в программирование', 7)
reviewer1.rate_hw(student2, 'Git', 7)

student1.rate_lec(lecturer1, 'Python', 7)
student1.rate_lec(lecturer1, 'Git', 9)
student2.rate_lec(lecturer1, 'Python', 8)
student2.rate_lec(lecturer1, 'Git', 5)
student1.rate_lec(lecturer2, 'Python', 7)
student2.rate_lec(lecturer2, 'Python', 7)
student2.rate_lec(lecturer2, 'Введение в программирование', 7)

print(reviewer1)
print(reviewer2)
print(lecturer1)
print(lecturer2)
print(student1)
print(student2)

print(mean_grade_hw('Git'))
print(mean_grade_lec('Введение в программирование'))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




