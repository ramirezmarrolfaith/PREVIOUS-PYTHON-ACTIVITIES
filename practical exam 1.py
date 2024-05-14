#Ramirez, Marrol Faith F.
#Practical Exam 1 (February 28, 2022)

print("                        Fei én Lyz Salon                             ")

print("-----------------------------------------------------------------")

print("           Code                Description           Price")
print("           [S1]                   Haircut               80")
print("           [S2]              Haircut W Blower          100")
print("           [R1]                    Rebond             3000")

prchs=eval(input("How many set of service would you like to avail? "))

code=input("Type the code of the service:")

q=eval(input("Type the number or quantity of service you would like to avail: "))

s1=("S1")
s2=("S2")
r1=("R1")

q1=(q*80)
q2=(q*100)
q3=(q*3000)

for i in range (prchs):
    if code==s1:
        print(q,"\t\tHaircut\t\t",q1)
    
    elif code==s2:
        print(q,"\t\tHaircut W Blower\t\t",q2)
        
    else:
         print(q,"\t\tRebond\t\t",q3)
 
print("Total Amount: ",ta)
ta=(q1+q2+q3)

pa=(eval(input("How much will you pay? "))

c=pa-ta
print("Your change is: ",c)