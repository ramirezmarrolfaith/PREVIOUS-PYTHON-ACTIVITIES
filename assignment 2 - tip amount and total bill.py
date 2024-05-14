#Ramirez, Marrol Faith
#Assignment 2

prc=eval(input("Enter the price of your meal: "))
prcnt=eval(input("Enter the percent tip you want to leave: "))

ta=(prcnt*0.01)*prc
tb=prc+ta

print("\nYour tip amount would be",ta,"and your total bill with the tip is",tb)
