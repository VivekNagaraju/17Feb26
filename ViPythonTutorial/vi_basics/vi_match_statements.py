'''
Created on 03-Mar-2026

@author: Vivek
'''
day_number = int(input("Enter the number to know the day:"))

match day_number:
    
    case 1:
        print("Sunday")
        
    case 2:
        print("Monday")
        
    case 3:
        print("Tuesday")
        
    case 4:
        print("Wednesday")
        
    case 5:
        print("Thursday")
        
    case 6:
        print("Friday")
        
    case 7:
        print("Saturday")
    
    case _:
        print("Please enter number in the range of 1-7")