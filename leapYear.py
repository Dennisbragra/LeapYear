def LeapYear(year):
    """The function to check whether the year is a leap year"""
    
    #Prompt the user to input the year they would like checked
    
    #A leap year is divisible by 4 unless it's a century year
    #A century year has to be divivsible by 400

    if year % 4 == 0 and year % 100 != 0:
        print(str(year) + " is a leap year")
    elif year % 100 == 0:
        print(str(year) + " is not a leap year")
    elif year % 400 == 0:
        print(str(year) + " is a leap year")
    else:
        print(str(year) + " is not a leap year")        

LeapYear(int(input("Enter the year to be checked \n")))