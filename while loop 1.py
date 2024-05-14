temp=0

while temp != -1000:
    temp = eval(input("\nEnter a temperature (-1000 to quit):"))
    
    if temp!= -1000:
        print("In fahrenheit that is",9/5*temp+32)
        
    else:
        print("\nGood bye.")