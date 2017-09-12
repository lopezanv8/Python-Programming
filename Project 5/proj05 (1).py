
##########################
#Computer Project #5
#First import the pylab which will be used to plot the graphs 
#Prompt to open a file
#    user will input the RedCedarRiver.txt
#
#It will then read the data file 
#    Beginning with an empty list
#    Create a tuple of the year, month, and flow
#    Then append the L with the tuple
#The annual average will take a list 
#    then find the average for every year
#    create a tuple of the year and the average
#    then append the year flows with the tuple
#The month flow will read through the file
#    determine the flow for each month of every year
#Then draw a plot of the annual average
#As well as display each year and its flow average
#Then determine which month the user inputed to obtain data for
#it will loop through and determine whether the input is true or not.
#The program will draw a plot of the flow of a certain month for every year.
#As wel as display the month and the flow of every year. 
################################################
import pylab

def draw_plot( x, y, plt_title, x_label, y_label):
    ''' Draw x vs. y (lists should have the same length)
    Sets the title of plot and the labels of x and y axis '''
    
    pylab.title(plt_title)
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    
    pylab.plot( x, y )
    pylab.show()    



def open_file():
    """
    prompt for a file to open 
    program will display an error message if incorrect file is inputed
    then prompt again until file opens successfully
    """    
    the_file = input ("Enter a file name: ")
    while True:
        try: 
            fp = open (the_file)
            return fp
        except FileNotFoundError:
            the_file = input ("Error. Enter a file name: ")
           
def read_file ():   #This will call the open_file() function
    """
    calls to the open_file it then reads the data file
    starts as an empty list
    then returns the data list in a tuple with the year, month, and flow
    """
    fp = open_file()
    L = []
    for line in fp:
        line_lst = line.strip().split()
        year = line_lst[4]
        month = line_lst[5]
        flow = float(line_lst [6])
        T = (year, month, flow)
        L.append(T)     #This will include everything in what was an empty L
    return L       
        

def annual_average(L):
    """
    take the flows of every month for each year
    program adds on to the count until adds up to 12 to represent the months
    then appends the flow
    determine the avg_flow by dividing the sum of the months by the length of 
        the year
    a tuple is then created and appended to the year_flows
    the count has to be reset to 0 after its reached 12
    then returns the year_flows which includes the year and its average
    """    
    year_flows = []
    temp_flows = []
    count = 0
    for item in L: #where item is something like ('2015', '6', 77.5)    
        count += 1         
        flow = item [2]
        temp_flows.append(flow)      
        if count == 12: #there is only 12 months so count cannot be greater
            year = item [0]
            avg_flow = sum(temp_flows)/ len(temp_flows)
            T = (year, avg_flow)
            year_flows.append(T)
            temp_flows = []
            count = 0   #Reset the count to 0; there is only 12 months
    return year_flows
    
    
def month_average (L,M):
    """
    takes the flows of a certain month for every year
    month_flow starts of as an empty list
    its then appended with the year and the flow
    the count is then reseted back to 0 since there is only 12 months.
    """    
    month_flow = []
    count = 0
    for item in L:
        count += 1
        year = item [0] 
        flow = item [2]
        if count == M:
            month_flow.append((year,flow)) 
            #Append the month_flow so that year and flow are included 
        if count == 12:
            count = 0
    return month_flow
            

            
L = read_file()
year_flow = annual_average(L)

x = []
y = []
for item in year_flow:
    x.append(int(item[0]))
    y.append(item[1])
draw_plot (x, y, "Annual Average Flow 1932 - 2015", "Year", "Flow")    
    
print("Annual Average Flow")    
print ("{:<7}{:>9}".format('Year', 'Flow'))
for item in year_flow:
    print("{:<7}{:>9.2f}".format(item[0],item[1]))

while True:
    M = (input("Enter a Month(1-12):"))
    if M.isdigit(): #month has to be a digit as it is the number of the month
        M = (int(M))
        if M > 12 or M < 1: #has to be in the range of 1-12
            print ("Error. Integer out of range." )
        else:
            break
    else:
        print ("Error. Not an integer.")
            
month_flow =  month_average(L,M)

x = []
y = []
for item in month_flow:
    x.append(int(item[0]))
    y.append(item[1])
month_str = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", \
"Oct", "Nov", "Dec"]    
draw_plot (x, y, "Average Flow for " + month_str[M-1], "Year", "Flow")   
#subtract 1 from M because the index begins counting at 0 instead of 1

print ("Average Flow for " + month_str [M-1])
print ("{:<7}{:>9}".format('Year', 'Flow'))
for item in month_flow:
    print("{:<7}{:>9.2f}".format(item[0],item[1]))



   




#Q1:6
#Q2:4
#Q3:4
#Q4:4
