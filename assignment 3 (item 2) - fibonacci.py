#Ramirez, Marrol Faith F.
#Assignment 3 (Item 2)

reps=int(input("Enter how many Fibonnaci numbers would you like to present: "))

f1=0
f2=1

for seq in range(0, reps):
           if(seq<=1):
               n2=seq          
               
           else:               
                      n2=f1+f2
                      f1=f2
                      f2=n2
                      
           print(n2)