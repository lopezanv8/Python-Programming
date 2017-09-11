# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:09:54 2016

@author: lopezan8
"""

# calcualate tuition for an MSU student during Fall Semester 2016
# Step 1: Resident or Non-Resident
# Step 2: Level (Freshmen, Sophomore, Junior, Senior, Graduate)
# Step 3: College
# Step 4: Credits
# Step 5: Total Cost


answer = "yes"
while answer == "yes":
    resident = input ("resident(yes/no):").lower()
    level = input("input level (freshman, sophomore, junior, senior, graduate):").lower()
    college = input("College (business, engineering, health, sciences, none):").lower()
    credits = int(input("credits taking this semester:"))
    #print(resident, college, level, credits)
    cost = 0
    if resident == "yes":
        if (level == "freshman" or level == "sophomore"):
            cost = credits * 468.75 + 18.00 + 3.00 + 5.00
        
        elif (level == "junior" or level == "senior"):
            cost = credits * 523.25 + 18.00 + 3.00
        
            if college == 'business' and credits <= 4:
                cost = credits * 523.25 + 109.00 + 18.00 + 3.00
            elif college == 'business' and credits > 4:
                cost = credits * 523.25 + 218.00 + 18.00 + 3.00 + 5.00
            elif college == 'engineering' and credits <= 4:
                cost = credits * 523.25 + 387.00 + 18.00 + 3.00
            elif college == 'engineering' and credits > 4:
                cost = credits * 523.25 + 645.00 + 18.00 + 3.00 + 5.00
            elif college == 'health' and credits <= 4:
                cost = credits * 523.25 + 50.00 + 18.00 + 3.00
            elif college == 'health' and credits > 4:
                cost = credits * 523.25 + 100.00 + 18.00 + 3.00 + 5.00
            elif college == 'sciences' and credits <= 4:
                cost = credits * 523.25 + 50.00 + 18.00 + 3.00
            elif college == 'sciences' and credits > 4:
                cost = credits * 523.25 + 100.00 + 18.00 + 3.00 + 5.00
            
        elif (level == "graduate"):
            cost = credits * 698.50 + 11.00 + 3.00
        
            if college == 'engineering' and credits <= 4:
                cost = credits * 698.50 + 37.50 + 387.00 + 11.00 + 3.00
            elif college == 'engineering' and credits > 4:
                cost = credits * 698.50 + 75.00 + 645.00 + 11.00 + 3.00
        
    else: #if resident == "no":
        if (level == "freshman" or level == "sophomore"):
            cost = credits * 1,263.00 + 18.00 + 3.00
        
        elif (level == "junior" or level == "senior"):
            cost = credits * 1,302.75 + 18.00 + 3.00
        
            if college == 'business' and credits <= 4:
                cost = credits * 1,302.75 + 109.00 + 18.00 + 3.00
            elif college == 'business' and credits > 4:
                cost = credits * 1,302.75 + 218.00 + 18.00 + 3.00 + 5.00
            elif college == 'engineering' and credits <= 4:
                cost = credits * 1,302.75 + 387.00 + 18.00 + 3.00
            elif college == 'engineering' and credits > 4:
                cost = credits * 1,302.75 + 645.00 + 18.00 + 3.00 + 5.00
            elif college == 'health' and credits <= 4:
                cost = credits * 1,302.75 + 50.00 + 18.00 + 3.00
            elif college == 'health' and credits > 4:
                cost = credits * 1,302.75 + 100.00 + 18.00 + 3.00 + 5.00
            elif college == 'sciences' and credits <= 4:
                cost = credits * 1,302.75 + 50.00 + 18.00 + 3.00
            elif college == 'sciences' and credits > 4:
                cost = credits * 1,302.75 + 100.00 + 18.00 + 3.00 + 5.00
        
        else: #if (level == "graduate"):
        
            if credits <= 4:
                if college == 'engineering':
                    cost = credits * 1,372.00 + 37.50 + 387.00 + 11.00 + 3.00
                elif college == 'business':
                    pass
                
            else:
                if college == 'engineering':
                    cost = credits * 1372.00 + 75.00 + 645.00 + 11.00 + 3.00 + 5.00
        yes
    
    
    
    print ("Total Cost: ${:,.2f}".format( cost))
    answer = input("would you like to calculate again(yes/no):").lower()
    
