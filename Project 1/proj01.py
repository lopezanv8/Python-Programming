# first program in python
# input two numbers, add them together, print them out
# wfp, 9/1/07; rje, 5/5/14
print()

temp_var = 15
speed_var = 10

WCT= 35.74 + 0.6215* temp_var - 35.75 * (speed_var **(0.16)) + 0.4275* temp_var *(speed_var **(0.16))

print('The air temperature(degrees F) is: ',temp_var)
print(' The Wind Speed(MPH) is: ', speed_var)
print('The Wind Chill Temperature is: ',WCT)
print()


temp_var = 0
speed_var = 20

WCT= 35.74 + 0.6215* temp_var - 35.75 * (speed_var **(0.16)) + 0.4275* temp_var *(speed_var **(0.16))

print('The air temperature(degrees F) is: ',temp_var)
print(' The Wind Speed(MPH) is: ', speed_var)
print('The Wind Chill Temperature is: ',WCT)
print()


temp_var = -15
speed_var = 30

WCT= 35.74 + 0.6215* temp_var - 35.75 * (speed_var **(0.16)) + 0.4275* temp_var *(speed_var **(0.16))

print('The air temperature(degrees F) is: ',temp_var)
print(' The Wind Speed(MPH) is: ', speed_var)
print('The Wind Chill Temperature is: ',WCT)
print()



T_str1 = input('Please enter air temperature: ')
V_str2 = input('Please enter Wind Speed: ')
print()

temp_var = float(T_str1)
speed_var = float(V_str2)

WCT= 35.74 + 0.6215* temp_var - 35.75 * (speed_var **(0.16)) + 0.4275* temp_var *(speed_var **(0.16))

print('The air temperature(degrees F) is: ',temp_var)
print(' The Wind Speed(MPH) is: ', speed_var)
print('The Wind Chill Temperature is: ',WCT)
