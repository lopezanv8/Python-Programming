####################
#
#       Computer Project 11
#
#   Creates Class Grade
#   Creates Class Student
#   Within each class there are fuctions 
#   These classes will then be used for other programs.
#
#
####################

class Grade(object):
    
    def __init__(self, assignment = '', grade = 0.0, aweight = 0.0):
        ''' Constructs final scores by using the assignment, the grade, and the
        weight of the assignment'''
        self.assignment_str = assignment
        self.grade_float = grade
        self.aweight_float = aweight
        #the parameters must be assigned to a self with an attribute that is not\
        #private so that it can then be accessed. 
    def __str__( self ):
        '''Returns a string representing the grade of a student.'''
        out_str = "{:10} : {:6.0f}% {:6.02f}".format(self.assignment_str, self.grade_float, \
        self.aweight_float)
        #Displays the name of the project, the grade, and the weight of the grade
        return out_str
        
    def __repr__( self ):
        ''' Returns a formal representation of the students grade.'''
        
        return self.__str__()
        #just calls the __str__ to print the same thing
        
class Student (object):
    def __init__(self, stuid = 0, first = '', last = '', grades = None):
        ''' Constructs the data of the student'''
        
        self.first_name_str = first
        self.last_name_str = last
        self.id_int = stuid
        self.grades_lst = grades
        #the four parameters must be assigned to a self with an attribute that \
        #can then be accessed later on. 
        
    def update(self, first = '', last = '', stuid = 0, grades = None):
        if first:
            self.first_name_str = first
        if last:
            self.last_name_str = last
        if stuid:
            self.id_int = stuid
        if grades:
            self.grades_lst = grades
           
    def add_grade(self, grade = 0):
        ''' adds a grade to the list of grades'''
        if self.grades_lst == None:  
            self.grades_lst = [grade]
            #checks if the grades are in the list of grades
        else:
            self.grades_lst.append(grade)
            #if it is not in the list, it will add that grade onto the list
        
    def calculate_grade( self ):
        '''gets the weight of each assignment, to return final grade '''
        final_score = 0
        for g in self.grades_lst:
            grade_input = g.aweight_float * g.grade_float
            final_score += grade_input
            #multiplies the grade points by the weight to then sum up all the \
            # grades and return the final score of the student.
        return final_score
        
   
    def __gt__( self, other ):
        ''' student one final grades greater than student two's final grades'''
        student_one = self.calculate_grade()
        student_two = other.calculate_grade()
        
        return student_one > student_two
        
    def __lt__( self, other ):
        ''' student one final grades less than student two's final grades'''
        student_one = self.calculate_grade()
        student_two = other.calculate_grade()
       
        return student_one < student_two
        
    def __eq__( self, other ):
        ''' student one's final grades are equal to student two's final grades'''
        student_one = self.calculate_grade()
        student_two = other.calculate_grade()
       
        return abs(student_one - student_two) < 10 ** -6
        
    def __str__( self ):
        '''Returns a string representation of the name of the student, followed 
        by the students grades.'''
        #print method
        stustr = self.last_name_str + ', ' + self.first_name_str + "\n"
        for item in self.grades_lst:
            stustr += item.__str__()+ "\n"
        return stustr[:-1]
        
        #returns the string of the students last name, first name, followed by
        #grades of the student.
        #in order to get the students grades, in this function, we call the \
        #__str__ function from the class Grade.
    def __repr__( self ):
        '''Returns a string representation of the students name and grades'''
        return self.__str__()
       #just calls the __str__ function to return the same thing. 
        
        