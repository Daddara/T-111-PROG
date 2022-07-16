
BUDGET_DAY_PRICE = 40
DAILY_DAY_PRICE = 60
MILE_PRICE = 0.25
DAILY_MILE_MARK = 100

choice = input("Welcome to car rentals! \nWould you like to continue (y/n)? ")

while choice == "y":
    
    '''Input section'''
    cust_code = input("Customer code (b or d): ")
    num_of_days = int(input("Number of days: "))
    odo_start = int(input("Odometer reading at the start: ")) 
    odo_end = int(input("Odometer reading at the end: ")) 
    total_drive = (odo_end - odo_start) 
    
    '''Calculates total amount based on selected choice'''
    if cust_code == "b":
        total_amount = (num_of_days*BUDGET_DAY_PRICE)+(total_drive*MILE_PRICE)
    else: 
        total_day_price = (num_of_days*DAILY_DAY_PRICE)
        avg_drive_per_day = total_drive/num_of_days
        '''calculates if more than 100km are driven per day'''
        if avg_drive_per_day > DAILY_MILE_MARK:
            price_above_hundred_miles = (MILE_PRICE*(total_drive-(DAILY_MILE_MARK*num_of_days)))
            total_amount = total_day_price+price_above_hundred_miles
        else:
            total_amount = total_day_price
  
    print ("Miles driven:", total_drive)
    print ("Amount due:", round(total_amount, 1))
    choice = input("Would you like to continue (y/n)? ")
