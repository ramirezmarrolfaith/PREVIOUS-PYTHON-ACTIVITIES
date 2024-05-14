#Ramirez, Marrol Faith
#Assignemnt 2 (Item 1)

import random

a=round((random.uniform(1,100)),2)
b=round((random.uniform(1,100)),2)
c=round((random.uniform(1,100)),2)
d=round((random.uniform(1,100)),2)
e=round((random.uniform(1,100)),2)

ave=(a+b+c+d+e)/5
ave=round(ave,2)

print("The average of the five (5) random numbers is: " +str(ave))