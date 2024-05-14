#Ramirez, Marrol Faith F.
#Assignemnt 2 - Letter C

pwr=int(input("Enter the power of a number:"))
d=int(input("Enter the number of digits:"))

e=(2**pwr)
x=(e%100)//d

print("\nThe last that many digits of 2 raised to the power is:",round(x,2))