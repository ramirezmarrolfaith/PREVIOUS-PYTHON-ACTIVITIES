num = int(input("Enter an integer: "))
l_num = num
s_num = num 

while num != 0:
    num = int(input("Enter an integer: "))
        
    if num > l_num:
        l_num = num
    
    if num != 0 and num < s_num:
        s_num = num
        
    else:
        s_num = s_num

print("Largest: ",l_num) 
print("Smallest: ",s_num)

d = (l_num-s_num)
print("Difference: ",d)