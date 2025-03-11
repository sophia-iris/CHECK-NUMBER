def check_number(num):    
    if (num % 2) == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number")
        
def check(): 
    n = int(input("Enter any number to check if it is odd or even."))      
    check_number(n)
    
check() 

while True: 
    babye = input("Would you like to enter another number? (yes or no) ")
    if babye == "yes": 
        check() 
    else: 
        print("sigi, no sabi mo eh")    
        break