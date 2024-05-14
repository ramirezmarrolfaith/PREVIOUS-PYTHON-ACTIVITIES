#Ramirez, Marrol Faith F.
#Exercise 1 (Feb 21)

grd=eval(input("Enter your average (grade): "))

#A - Outstanding
if grd>=90 and grd<100:
    print("A - Outstanding")

#B - Good
elif grd>=80 and grd<90:
    print("B - Good")
    
#C - Fair
elif grd>=70 and grd<80:
    print("C - Fair")

#D - Poor
elif grd>=60 and grd<70:
    print ("D - Poor")

#E - Failed
elif grd<60:
    print("E - Failed")

else:
    print("Invalid grade.")