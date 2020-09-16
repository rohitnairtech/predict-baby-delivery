from os import _exit


def monthName(i):
    months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    return months.get(i, 'invalid')


def predict(month, day, i):
    day += 7
    increment = 8
    if month == 'January':
        if day <= 30:
            ed_day = day
        else:
            increment += 1
            ed_day = 30 - day
        month = monthName(i+increment)
    elif month == 'February':
        if day < 31:
            ed_day = day
        else:
            increment += 1
            ed_day = 30 - day
        month = monthName(i+increment)
    elif month == 'March':
        if day <= 30:
            ed_day = day
        else:
            increment += 1
            day = day - 1
            ed_day = 31 - day
        month = monthName( i + increment )
    elif month == 'April':
        if day <= 31:
            ed_day = day 
        else :
            increment += 1
            ed_day = 31 - day
        month = monthName(i+increment)
    elif month == 'May':
        if day <= 28:
            ed_day = day 
        else :
            increment += 1
            day = day - 1           
            ed_day = 31 - day
        month = monthName(i+increment) 
    elif month == 'June':
        if day <= 31:
            ed_day = day 
        else :
            increment += 1
            day = day - 1
            ed_day = 30 - day 
        month = monthName(i+increment) 
    elif month == 'July':
        if day <= 30:
            ed_day = day 
        else :
            increment += 1
            day = day - 1
            ed_day = 31 - day
        month = monthName(i+increment) 
    elif month == 'August':
        if day <= 31:
            ed_day = day 
        else :
            increment += 1
            ed_day = 30 - day
        month = monthName(i+increment) 
    elif month == 'September':
        if day <= 30:
            ed_day = day 
        else :
            increment += 1
            day = day - 1
            ed_day = 31 - day
        month = monthName(i+increment) 
    elif month == 'October':
        if day <= 31:
            ed_day = day 
        else :
            increment += 1
            ed_day = 30 - day
        month = monthName(i+increment) 
    elif month == 'November':
        if day <= 30:
            ed_day = day 
        else :
            increment += 1
            day = day - 1
            ed_day = 31 - day
        month = monthName(i+increment) 
    elif month == 'December':
        if day <= 31:
            ed_day = day 
        else :
            increment += 1
            ed_day = 31 - day
        month = monthName(i+increment) 

    print(f"The predicted expected date of your baby's delivery is {day} {month} :)")
     
print('Please write the month number of the month in which you had your last menstrual period (eg: 1 for January / 12 for December)')           
i = int(input('--> '))
m = monthName(i)
if(m == 'invalid'):
    print('Invalid date selection')
    _exit(1)
print("Please write the day of the month (e.g 14, 16, 22 etc)")
d = int(input())
predict(m, d, i)
