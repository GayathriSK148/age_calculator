import time

##-------------------------------------------------inputs----------------------------------------------------------------##
birth_year = int(input("Enter your birth-year: "))
birth_month = int(input("Enter you birth-month(eg:01 for January): "))
if birth_month > 12:
    print("There are only twelve months")                                           ##There are only 12 months in a year
else:
    birth_date = int(input("Enter your birth-date: "))
         
    if (birth_month in [1, 3, 5, 7, 8, 10, 12]) and (birth_date > 31):
        print("Error!Such a day does not exist")                                ##January, March, May, July, August, October and December has only 31 days
    elif (birth_month in [4, 6, 9, 11]) and (birth_date > 30):
        print("Error!Such a day does not exist")                                ##April, June, September and November has only 30 days 
    elif birth_month == 2 and birth_year % 4 == 0 and birth_date > 29:
        print("Error!Such a day does not exist")                                ##February in a leap year has 29 days
    elif birth_month == 2 and birth_year % 4 != 0 and birth_date > 28:
        print("Error!Such a day does not exist"/n)                              ##February in all other years have 29 days
    else:
        today_year = int(input("Enter the year at which you want to calculate your age: "))
        if today_year < birth_year:
            print("Age can be calculated only after birth")
        else:
            today_month = int(input("Enter the month at which you want to calculate your age: "))
            if today_month > 12:
                print("There are only twelve months")                                ##There are only 12 months in a year
            elif today_year == birth_year and today_month < birth_month:
                print("Age can be calculated only after birth")                      ##Age can be calculated only after birth
            else:
                today_date = int(input("Enter the date at which you want to calculate your age: "))
                if (today_month in [1, 3, 5, 7, 8, 10, 12]) and today_date > 31:     ##January, March, May, July, August, October and December has only 31 days
                    print("Error!Such a day does not exist")
                elif (today_month in [4, 6, 9, 11]) and today_date > 30:             ##April, June, September and November has only 30 days
                    print("Error!Such a day does not exist")
                elif today_month == 2 and today_year % 4 == 0 and today_date > 29:   ##February in a leap year has 29 days
                    print("Error!Such a day does not exist")
                elif today_month == 2 and today_year % 4 != 0 and today_date > 28:   ##February in all other years have 29 days
                    print("Error!Such a day does not exist")
                elif today_year == birth_year and today_month == birth_month and today_date < birth_date:
                    print("Age can be calculated only after birth")
                else:
                    print("       ")
                    time.sleep(1)
                    
##--------------------------------------------calculations-------------------------------------------------## 
if (today_month >= birth_month) and (today_date >= birth_date):
    year = today_year - birth_year
    month = today_month - birth_month
    days = today_date - birth_date
    
elif today_month >= birth_month:
    year = today_year - birth_year
    month = today_month - birth_month - int(1)
    if today_month in [1, 2, 4, 6, 8, 9, 11]:
        days = int(31) + int(today_date) - birth_date 
    elif today_month in [5, 7, 10, 12]:
        days = int(30) + int(today_date) - birth_date
    elif today_month == 3 and int(today_year) % 4 == 0:
        days = int(29) + int(today_date) - birth_date
    else:
        days = int(28) + int(today_date) - birth_date
                                
elif int(today_month) < birth_month and int(today_date) >= birth_date:
    year = int(today_year) - birth_year - int(1)
    month = int(12) + int(today_month) - birth_month
    days = int(today_date) - birth_date
    
else:
    year = int(today_year) - birth_year - int(1)
    month = int(11) + int(today_month) - birth_month
    if today_month in [1, 2, 4, 6, 8, 9, 11]:
        days = int(31) + int(today_date) - birth_date 
    elif today_month in [5, 7, 10, 12]:
        days = int(30) + int(today_date) - birth_date
    elif today_month == 3 and int(today_year) % 4 == 0:
        days = int(29) + int(today_date) - birth_date
    else:
        days = int(28) + int(today_date) - int(birth_date)
            
print("Your age is ", year, "years", month, "months", days, "days on", today_date, "/", today_month, "/", today_year)

