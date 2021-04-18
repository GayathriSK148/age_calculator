import time
birth_year = int(input("Enter your birth-year: "))
if birth_year < 1900:
    print("Enter an acceptable year")
else:   
    birth_month = int(input("Enter you birth-month(eg:01 for January): "))
    if birth_month > 12:
        print("There are only twelve months")
    else:
        birth_date = int(input("Enter your birth-date: "))
        if (birth_month == 1 or birth_month == 3 or birth_month == 5 or birth_month == 7 or birth_month == 8 or birth_month == 10 or birth_month == 12) and birth_date > 31:
            print("Error!Such a day does not exist")
        elif (birth_month == 4 or birth_month == 6 or birth_month == 9 or birth_month == 11) and birth_date > 30:
            print("Error!Such a day does not exist")
        elif birth_month == 2 and birth_year % 4 == 0 and birth_date > 29:
            print("Error!Such a day does not exist")
        elif birth_month == 2 and birth_year % 4 != 0 and birth_date > 28:
            print("Error!Such a day does not exist")
        else:
            print("         ")
            today_year = int(input("Enter the year at which you want to calculate your age: "))
            if today_year < birth_year:
                print("Age can be calculated only after birth")
            else:
                today_month = int(input("Enter the month at which you want to calculate your age: "))
                if today_month > 12:
                    print("There are only twelve months")
                elif today_year == birth_year and today_month < birth_month:
                    print("Age can be calculated only after birth")
                else:
                    today_date = int(input("Enter the date at which you want to calculate your age: "))
                    if (today_month == 1 or today_month == 3 or today_month == 5 or today_month == 7 or today_month == 8 or today_month == 10 or today_month == 12) and today_date > 31:
                        print("Error!Such a day does not exist")
                    elif (today_month == 4 or today_month == 6 or today_month == 9 or today_month == 11) and today_date > 30:
                        print("Error!Such a day does not exist")
                    elif today_month == 2 and today_year % 4 == 0 and today_date > 29:
                        print("Error!Such a day does not exist")
                    elif today_month == 2 and today_year % 4 != 0 and today_date > 28:
                        print("Error!Such a day does not exist")
                    elif today_year == birth_year and today_month == birth_month and today_date < birth_date:
                        print("Age can be calculated only after birth")
                    else:
                        print("       ")
                        time.sleep(1)
                    
                        if int(today_month) >= birth_month and int(today_date) >= birth_date:
                            year = int(today_year) - birth_year
                            month = int(today_month) - birth_month
                            days = int(today_date) - birth_date
                        elif int(today_month) >= birth_month:
                            year = int(today_year) - birth_year
                            month = int(today_month) - birth_month - int(1)
                            if today_month == 2 or today_month == 4 or today_month == 6 or today_month == 8 or today_month == 9 or today_month == 11:
                                days = int(31) + int(today_date) - birth_date 
                            elif today_month == 5 or today_month == 7 or today_month == 10 or today_month == 12:
                                days = int(30) + int(today_date) - birth_date
                            elif today_month == 3 and int(today_year) % 4 == 0:
                                days = int(29) + int(today_date) - birth_date
                            elif today_month == 3 and int(today_year) % 4 != 0:
                                days = int(28) + int(today_date) - birth_date   
                        elif int(today_month) < birth_month and int(today_date) >= birth_date:
                            year = int(today_year) - birth_year - int(1)
                            month = int(12) + int(today_month) - birth_month
                            days = int(today_date) - birth_date
    
                        elif int(today_month) < birth_month and int(today_date) < birth_date:
                            year = int(today_year) - birth_year - int(1)
                            month = int(11) + int(today_month) - birth_month
                            if today_month == 2 or today_month == 4 or today_month == 6 or today_month == 8 or today_month == 9 or today_month == 11:
                                days = int(31) + int(today_date) - birth_date 
                            elif today_month == 5 or today_month == 7 or today_month == 10 or today_month == 12:
                                days = int(30) + int(today_date) - birth_date
                            elif today_month == 3 and int(today_year) % 4 == 0:
                                days = int(29) + int(today_date) - birth_date
                            elif today_month == 3 and int(today_year) % 4 != 0:
                                days = int(28) + int(today_date) - int(birth_date)
            
                        print("Your age is ", year, "years", month, "months", days, "days on", today_date, "/", today_month, "/", today_year)

