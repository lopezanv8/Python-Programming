####################
#Computer Project 06
#Program begins by importing csv
#prompt to open a file 
#   user should input Texas_death_row.csv
#program will then read the data file
#   in which we use the csv reader because some of the data in the file cannot be split
#then begin with an empty list
# the file will then be read line by line looking for the race, gender, and ("\")
#   info about the victim.
#   Creates a tuple of that information and appends it to the list
#then we start with having each race starting at zero
#   as we find a race on a line we add one to that race.
#   add all races total together
#   add all minority total together
#then we start with having each gender starting at zero
#   as we find a gender on a line we add one that gender
#   add both genders total together
#then we start with having the victim information on zero
#   as we find the information of the victim, whether its it gender and its race
#   we add one to its pertaining category.
#
####################

#1. Since the minorities consist of both Black and Hispanic, the executions ("\")
#   are higher for minorities than they are for whites.
#2. Executions for minorities killing whites are higher than whites killing ("\")
#   minorities because there was only 7 white-on-minority and there was 28 ("\")
#   minority-on-white.
#3. Execution are higher for men killing women because there was 65 male-on- ("\")
#   female and there was 0 female-on-male.
#4. There is a higher pecentage of men being executed because there was 118 ("\")
#   men executed and only 1 female executed.

import csv

def open_file():
    """
    open a file and display a proper message if incorrect file is inputted. 
    """
    the_file = input ("Enter a file name: ")
    while True:
        try: 
            fp = open (the_file, "r")
            return fp
        except FileNotFoundError:
            the_file = input ("Error. Enter a file name: ")

def read_file():
    """
    read the file with the csv
    look for the specific informatin of race, gender, and victim inforamtion
    add that information to a tupple and append it to our beginning empty list
    """
    fp = open_file() 
    csv_fp = csv.reader(fp) #Csv reader because splitting cannont be done on commas 
    L = []     
    for line in csv_fp:
        data_lst = line
        race = data_lst[15]
        gender = data_lst[16]
        victim_info = data_lst[27]
        T = (race, gender, victim_info)
        L.append(T) #add the information to our list that began as empty
    
    return (L[1:]) #this is so that victim info is off by one.

L = read_file()

#begin with all races set to zero, as we find a certain race on a line, one ("\")
#will be added to its pertaining race.
white = 0
black = 0
hispanic = 0
N = 0

for item in L:
    race = item[0].lower()
    if race == "white":
        white += 1
    if race == "black":
        black += 1
    if race == "hispanic":
        hispanic += 1
        
    N = white + black + hispanic #add them all together
    Minority = black + hispanic 
    #add the minorities together to differentiate with white.

print ("========================================")
print ("White vs. Minority")    
print ("N = ", N)    
print ("White: ", white)
print ("Black: ", black)
print ("Hispanic: ", hispanic)
print ("Minority = Black + Hispanic: ", Minority)
   

        
print ("========================================")   

#begin with each gender set to zero, as we find a certain gender on a line, ("\")
#one will be added to its pertaining gender.     
male = 0
female = 0

for item in L:
    gender = item[1].lower()
    if gender == "male":
        male += 1
    if gender == "female":
        female += 1
    
    N = male + female #add them all together

print ("Male vs. Female")    
print ("N = ", N)
print ("Male = ", male)
print ("Female: ", female)
        

print ("========================================")

#begin with the information of the victim set to zero. the line will display ("\")
# whether the victim's race and its gender. that will then be added to its ("\")
# peratining category.
minority_on_white = 0
male_on_female = 0
female_on_male = 0
white_on_minority = 0
N = 0

for item in L:
    victim_info = item[2].lower()
    gender_info = item[1].lower()
    race_info = item[0].lower() 
    if "white" in victim_info and (race_info == "black" or race_info == "hispanic"):
       minority_on_white += 1 
    if "black" in victim_info and (race_info == "white"):
        white_on_minority += 1
    if "hispanic" in victim_info and (race_info == "white"):
        white_on_minority += 1
    num_males = victim_info.count("male") - victim_info.count("female")
    if num_males > 0 and gender_info == "female":
        female_on_male+= 1
    if "female" in victim_info and gender_info == "male":
        male_on_female += 1
N=0
for item in L:
    if item[0].lower() == '' or item[1].lower() == '':
        continue
    if item[2].lower() != '' and (not 'not available' in item[2].lower()):
        N += 1
        


print ("Race difference between perpetrator and victim.")
print ("N = ", N)
print ("Minority-on-white: ", minority_on_white)
print ("Male-on-female: ", male_on_female)
print ("Female-on-male: ", female_on_male)
print ("White-on-minority: ", white_on_minority)    




#Q1: 6
#Q2: 4
#Q3: 4
#Q4: 4
