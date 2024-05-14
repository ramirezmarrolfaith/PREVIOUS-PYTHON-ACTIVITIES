pw = ("hakdog")
tries = 3

while tries > 0:
    x = input("Password: ")
    
    if x == pw:
        print("You are now logged in to the system.")
        
        break
        
    else:
         tries +=1
         if tries ==0:
             print("You have been kicked off of the system.")
         else:
              print("Incorrect password. You only have",tries,"tries left.")