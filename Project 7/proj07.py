################
#Computer Project 7
#
#prompt to open multiple files
#   give error if input isn't correct
#
#read files inputed
#create a dictionary of data in files inputed
#
#find averages of city and highway mileages
#
#merge the data of multiple files together
#
#creates a master list 
#uses that list to plot
#plots multiple graphs
################

import csv
import pylab
import matplotlib.patches as patches

def open_files():
    ''' prompt to open multiple files. files will be read with csv. will return\
    a list of file pointers. proper message dispayed if error encountered.'''
    
    decade_files = input("Please enter the decades separated by comma: ")
    decades_split = decade_files.strip().split(',')  
    fps = []      
    while True:
        try:
            for decade in decades_split:
                fp  = open(decade + "s.csv") 
                csv_fp = csv.reader(fp)
                fps.append(csv_fp)
            return fps
            
        except FileNotFoundError:
            print ("Error. Incorrect decade")
            for fp in csv_fp:
                fp.close()

def read_file(input_file):
    '''Reads files of data, constructs and returns a dictionary. Assigned what \
    manuf is and what can be considered in manuf.'''
    
    dic1 = {} #start with empty dictionary. data will be appended on to it.
    city_fuel = []
    
    manuf = ["Ford", "GM", "Honda", "Toyota"]
    Ford = ["Ford", "Mercury", "Lincoln"]
    GM = ["Chevrolet", "Pontiac", "Buick", "GMC", "Cadillac", "Oldsmobile", "Saturn"]
    Honda = ["Honda", "Acura"]
    Toyota = ["Toyota", "Lexus", "Scion"]
    next(input_file)    #will return the next input file
    for line in input_file:
        manuf = line[46]
        year = int(line[63])
        if year == 2017:
            continue
        city_fuel = int(line[4])
        hwy_fuel = int(line[34])
        
        if manuf in GM:
            if 'GM' not in dic1:
                dic1["GM"] = {year: {'city': [city_fuel], 'highway': [hwy_fuel]}}               
            
            else:
                if year not in dic1["GM"]:
                    dic1["GM"][year]={'city': [city_fuel], 'highway': [hwy_fuel]}
                    #year is first encountered
            
                else:
                    dic1["GM"][year]['city'].append(city_fuel)
                    dic1["GM"][year]['highway'].append(hwy_fuel)
        
                    #appends new city mileage and new highway mileage
        
        if manuf in Honda:
            if 'Honda' not in dic1:
                dic1["Honda"]= {year: {'city': [city_fuel], 'highway': [hwy_fuel]}}
            
            else:
                if year not in dic1["Honda"]:                    
                    dic1["Honda"][year]={'city':[city_fuel], 'highway': [hwy_fuel]}
                    #year is first encountered
            
                else:
                    dic1["Honda"][year]['city'].append(city_fuel)
                    dic1["Honda"][year]['highway'].append(hwy_fuel)  

                    #appends new city mileage and new highway mileage

        if manuf in Ford:
            if 'Ford' not in dic1:
                dic1["Ford"] = {year: {'city': [city_fuel], 'highway': [hwy_fuel]}}
            
            else:
                if year not in dic1["Ford"]:
                    dic1["Ford"][year]={'city':[city_fuel], 'highway': [hwy_fuel]}
                    #year is fist encountered
                else:            
                    dic1["Ford"][year]['city'].append(city_fuel)
                    dic1["Ford"][year]['highway'].append(hwy_fuel)
                    
                    #appends new city mileage and new highway mileage
                
        if manuf in Toyota:
            if 'Toyota' not in dic1:
                dic1["Toyota"] = {year: {'city': [city_fuel], 'highway': [hwy_fuel]}}
            
            else:
                if year not in dic1 ["Toyota"]:
                    dic1["Toyota"][year]={'city': [city_fuel], 'highway': [hwy_fuel]} 
                    #year is first encountered
            
                else:
                    dic1["Toyota"][year]['city'].append(city_fuel)
                    dic1["Toyota"][year]['highway'].append(hwy_fuel)
                
                    #appends new city mileage and new highway mileage  
    
    return dic1
    

def average(dic1):
    ''' finds average of city mileage and highway mileage'''
    city_lst = []
    hwy_lst = []
    for manuf in dic1:
       year_manuf = dic1[manuf]
       for year in year_manuf:
           city_lst = year_manuf[year]['city']
           hwy_lst = year_manuf[year]['highway']
           city_avg= sum(city_lst)/len(city_lst)
           hwy_avg = sum(hwy_lst)/len(hwy_lst)
           year_manuf[year]['city']=city_avg
           year_manuf[year]['highway']=hwy_avg
           
    return dic1, city_avg, hwy_avg
  
def merge_dict (target,source):
    ''' merges multiple files to get a dictionary with all the information.'''
    for manuf in source:
        if manuf in target:
            target[manuf].update(source[manuf])
        else:
            target[manuf]=source[manuf]
            #target is to get a master dictionary and the source is from the \
            #previous data
 
def prepare_plot(Master_dict):
    '''Creates the master dictionary. Grabs averages from city mileage and hwy\
    mileage creating a new average. it will then sort the years in order. '''
    city = {}
    hwy = {}
    years = []
    #start with empty dictionaries for city and hwy
    #empty list for years
    for manuf, years_data in Master_dict.items():
        for year, mpg_data in years_data.items():
            if manuf in city:
#                T=(year, mpg_data[city])
                city[manuf].append((year, mpg_data['city']))
            else:
                city[manuf] = [(year, mpg_data['city'])]
            if year not in years:
                years.append(int(year))
            if manuf in hwy:
                hwy[manuf].append((year,mpg_data['highway']))
            else:
                hwy[manuf] = [(year, mpg_data['highway'])]
            if year not in years:
                years.append(int(year))
    print(city)
    print (hwy)
    for manuf, years_mpg in city.items():
        years_mpg.sort()
    for manuf, years_mpg in hwy.items():
        years_mpg.sort()
        #sort by years
    print(city)
    print(hwy)
    years.sort()
    print(years)

    return years, city, hwy
    
           
           
def plot_mileage (years, city, highway):
    '''Plot the city and highway mileage data.
       Input: years, a list of years;
              city, a dictionary with manufacturer as key and list of annual mileage as value;
             highway, a similar dictionary with a list of highway mileage as values.
       Requirement: all lists must be the same length.'''
    pylab.figure(1)
    pylab.plot(years, city['Ford'], 'r-', years, city['GM'], 'b-', years,
             city['Honda'], 'g-', years, city['Toyota'], 'y-')
    red_patch = patches.Patch(color='red', label='Ford')
    blue_patch = patches.Patch(color='blue', label='GM')
    green_patch = patches.Patch(color='green', label='Honda')
    yellow_patch = patches.Patch(color='yellow', label='Toyota')
    pylab.legend(handles=[red_patch, blue_patch, green_patch, yellow_patch])
    pylab.xlabel('Years')
    pylab.ylabel('City Fuel Economy (MPG)')
    pylab.show()
    
    #Plot the highway mileage data.
    pylab.figure(2)
    pylab.plot(years, highway['Ford'], 'r-', years, highway['GM'], 'b-', years,
             highway['Honda'], 'g-', years, highway['Toyota'], 'y-')
    pylab.legend(handles=[red_patch, blue_patch, green_patch, yellow_patch])
    pylab.xlabel('Years')
    pylab.ylabel('Highway Fuel Economy (MPG)')
    pylab.show()
            
#have tupple sort it to years once tuple sorted extract just averages create a dictionary (similar to avg dictionary)


Master_dict = dict()
fp = open_files()
print (fp)
for file in fp:
     data = read_file(file)
     merge_dict (Master_dict,data)
     print()     
     print(data)
     


print ()
print(Master_dict)
print ()
dic1 = average(data)
print(data)

years, city, highway = prepare_plot (dic1)
print (prepare_plot)
graph = plot_mileage 

print ("Manufactures' average for decades {}".format)
print ("City")
print ("Company: Mileage")
print ("GM: {}".format(city[GM]))
print ("Honda: {}".format(city[Honda]))
print ("Ford: {}".format(city[Ford]))
print ("Toyota: {}".format(city[Toyota]))

print ("Highway")
print ("Company: Mileage")
print ("GM: {}.".format(highway[GM]))
print ("Honda: {}".format(highway[Honda]))
print ("Ford: {}".format(highway[Ford]))
print ("Toyota: {}".format(highway(Toyota)))



#Q1: 1
#Q2: 7
#Q3: 7
#Q4: 1