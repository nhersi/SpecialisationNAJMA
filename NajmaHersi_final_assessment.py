# """
# TASK 1
#
#
class CFGStudent:

    def __init__(self, name, surname, age, email, student_id):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = student_id

    @staticmethod
    def generate_id():
        'create a random new id, which is any number between 1,000 and 10,000'
        'return id as a string'
        "Example '8754' "
        i = 1000
        for i in range(1001,10000):
            student_id = i
            i += 1
        return str(i)

    def get_id(self):
        return self.student_id
        'fetch student id'

    def get_fullname(self):
        "Expected outcome should be 'Name Surname' "
        print('{} {}'.format(self.name, self.surname))


class NanoStudent(CFGStudent):

    def __init__(self, specialization, course_grades):
        self.specialization = specialization
        self.course_grades = course_grades

    @staticmethod
    def generate_id():
        i = 1000
        for i in range(1001, 10000):
            student_id = i
            i += 1
        return print('this is your id: NANO{}'.format(student_id))
        'create a random new id, which is a word NANO followed by any number between 1,000 and 10,000'
        'return id as a string'
        "Example 'NANO1234' "

    def add_new_grade(self, task, grade):
        self.course_grades = []
        self.task = task
        self.grade = grade
        self.course_grades.append(self.task)
        self.course_grades.append(self.grade)

        print('[{} : {}]'.format(self.task,self.grade))

        'update course_grades container'
        "Example: pass in a task name and its grade, so that both are added to course_grades"

    def get_course_grades(self):
        return self.course_grades
        return self.grade
        'fetch course grades container and its values'



"""
TASK 2

"""
# setting up a general fibonacci function first

def fibonacci(i):
    if i == 0:
        return 0

    if i==1 or i==2:
        return 1

    else:
        return fibonacci(i-1) + fibonacci(i-2)

    return
#
# print(fibonacci(7))
# this works

# adding the requirement for summing up the fibonaccis
def sum_fibonacci(index_limit_number):
    for i in range(0,index_limit_number):
        if i == 0:
            return 0

        if i==1 or i==2:
            return 1

        else:
            return fibonacci(i-1) + fibonacci(i-2)
        i += 1
    return

def sum_fibonacci(index_limit_number):
    for i in range(0,index_limit_number):
        fibonacci(i)
        i += 1
    return

print(sum_fibonacci(0))

# adding the even summation requirement
def even_fibonacci_sum(index_limit_number):
    result = 0
    for i in range(0,index_limit_number):
        if fibonacci(i)/2 == 0:
            result += fibonacci(i)
        else:
            break
    return result

print(even_fibonacci_sum(10))

"""
TASK 3

"""
def is_valid_subsequence(array_1,array_2):
    for i in array_1:
        if i in array_2:
            array_2.remove(i)
    return array_2 == []

#### TESTS ####

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

print(is_valid_subsequence(array1, sequence1))  # FALSE


array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE

# they worked!yaay!



