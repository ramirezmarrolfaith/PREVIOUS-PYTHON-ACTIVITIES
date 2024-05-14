#Ramirez, Marrol Faith F.
#Assignment 5 (Item 2)

hr = eval(input("Enter hour: "))
tp = eval(input("\nAM (1) or PM (2)? "))
ha = eval(input("\nHow many hours ahead? "))


if tp == 2 and hr != 12:
    hr += 12;
elif tp == 1 and hr == 12:
    hr = 0;

nh = hr + ha;
nh = nh % 24;

if nh >= 0 and nh < 12:
    nh = nh % 12 ;
    if nh == 0:
        nh = 12;
    print("\nNew hour:",nh,"AM")
    
else:
    nh = nh % 12;
    if nh == 0:
        nh = 12 ;
    print("\nNew hour:",nh,"PM")