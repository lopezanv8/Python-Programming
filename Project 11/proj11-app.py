################################
#    Project 11 Application Program
#    
#    This program will use both classes created to solve a problem.
#    Algorithm
#        opens two files
#        reads the two files
#        Continuously loops to add the data of each student into a master list
#        Determines the final score of each student
#        loops to take only the final score of the student and add it to a list
#        uses that list to determine the class average.
###############################

import classes

def open_file():
    '''program will open two files, if any file cannot open, proper error 
    message will be displayed.'''
    
    try:
        fp1 = open("students.txt", "r")
        fp2 = open("grades.txt", "r")
    except FileNotFoundError:
        print("Error. File cannot be displayed.") 
        #if file isn't found, error message will display
    
    return fp1, fp2 #returns file pointers of the both files opened.
    
def read_file():
    ''' Calls the files that were opened. Then reads each file line by line. 
    '''
    fp1,fp2 = open_file()
    weight_lst = fp2.readline().strip().split()
    proj_list = fp2.readline().strip().split()
    #makes the files into lists.
    allstu_lst = {} #create a dictionary for the student
    master_stu = [] #master list of all the students
    for line in fp2:
        line = line.strip().split()
        stugrade_lst = [] #list of the grades of the student
        for i in range(1,len(line)):
            stugrade_lst.append(classes.Grade(proj_list[i], float(line[i]), \
            float(weight_lst[i]))) 
            #adds the assignment, grade, and weight grade to the students list 
            # of grades
        allstu_lst[line[0]] = stugrade_lst

    for line in fp1:
        line = line.strip().split()
        stuid = line[0] #the id of the student
        firstname = line[1] #first name of the student
        lastname = line[2] #last name of the student
        student = classes.Student(stuid, firstname, lastname, allstu_lst[stuid])
        master_stu.append(student)
        #adds the data of each student to the master list of all students.
        
    total = 0
    count = 0
    for student in master_stu:
        print(student)
        print("Final Grade: "  + "{:>6.0f}%".format( student.calculate_grade()))
        print()
        #to get the final grade of the student, we call the calculate_grade function
        # inside the Class Student
        total += (student.calculate_grade())
        count += 1
        #add the final score of each student to the total which has a list of all
        # the students.
    avg = total / count
    #determines the class average

    print("The class average is {:.02f}%".format(avg))
            



L = read_file()






#Q1: 7
#Q2: 3
#Q3: 3
#Q4: 4