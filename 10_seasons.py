'''
Write a Python program that reads two integers representing a month and
day and prints the season for that month and day.
Expected Output:
Input the month (e.g. January, February etc.): july
Input the day: 31
Season is harmattan
'''

Rainy_season= {"march":range(1,32), "april": range(1,31), "may":range(1,32), "june":range(1,31), 
               "july":range(1,32), "august":range(1,32), "september":range(1,31), "october":range(1,32)}
dry_season= {"november":range(1,31), "december":range(1,32), "january":range(1,32), "february":range(1,29)}

month= str(input("please input month: \n"))
day= int(input("input day of the month:\n"))



try:
    for x, y in Rainy_season.items() and dry_season.item():
        if  Rainy_season.keys()== month and Rainy_season.values() == day:
            print("It is rainy season")
        elif dry_season.keys() and dry_season.values()==day:   
            print("it's a dry season!")
except:
    print("values are incorrect")
    