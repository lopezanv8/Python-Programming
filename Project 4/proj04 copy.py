"""
Project 04
Prompt to open the file
It will repeatedly prompt to open a file until a file opens successfully
It will scan through the file and return the minimal percent value
    It will also indicate where the value is in the line
It will scan through the file and return the maximum percent value
    It will also indicate where the value is in the line
Since the index was found previously, it will return each GDP value associated with the minimal percent value and the maximum percent value
It will then display the minimum percent value, the year, and the GDP value
It will also display the maximum percent value, the year, and the GDP value
"""
def open_file():
    while True:   
        try:
            the_file = input("Enter a file name:")
            fp = open(the_file, "r")
            return fp
            
        except FileNotFoundError:
            print ("Error. Please try again")
    
    
def find_min_percent (line):
    min_value_index = 1
    min_value = 10000000 #set the beginning value high so as it goes through file the number will decrease
    
    for v in range(46):
       value = float(line[76+(v*12):88+(v*12)])
       if value < min_value:
            min_value = value #value has changed
            min_value_index = 76+(v*12)
    return min_value, min_value_index   

def find_max_percent (line):
    max_value_index = 1
    max_value = 0 #set the beginning value low so as it goes through file the number will increase
    
    for v in range (46):
        value = float(line[76+(v*12):88+(v*12)])
        if value > max_value:
            max_value = value #value has changed 
            max_value_index = 76+(v*12)
    return max_value, max_value_index
    
def find_gdp (line, index):
        return ( float(line[index:index+12].strip()))
        
def find_year (line,index):
        return ( float(line[index:index+12].strip()))


def display(min_percent, min_year, min_gdp, max_percent, max_year, max_gdp):
    print ("Gross Domestic Product")    
    print ("The minimum change in GDP was {:.1f} percent in {:4.0f} when the GDP was {:1.2f} trillion dollars.".format(min_percent, min_year, min_gdp/10**3))
            #the GDP is converted from billions to trillions
    print ("The minimum change in GDP was {:.1f} percent in {:4.0f} when the GDP was {:1.2f} trillion dollars.".format(max_percent, max_year, max_gdp/10**3))
            #the GDP is converted from billions to trillions
    
in_file = open_file()

count = 1
for line in in_file:
    if count == 9:
        line9 = line
    if count == 44:
        line44 = line
    if count == 8:
        line8 = line
    count += 1
        


min_percent, min_value_index = find_min_percent(line9)

max_percent, max_value_index = find_max_percent (line9)

min_gdp = find_gdp(line44, min_value_index)   
max_gdp = find_gdp(line44, max_value_index)

min_year = find_year(line8, min_value_index)
max_year = find_year(line8, max_value_index)

display_results = display (min_percent, min_year, min_gdp, max_percent, max_year, max_gdp)






#Questions
#Q1:6
#Q2:3
#Q3:3
#Q4:3



