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
 
def predict(month, day):
    if month == 'January':
            month = 'September'
            day = day + 7
            if day <= 30:
                ed_day = day 
            else:
                month = 'October'
                ed_day = 30 - day  
    elif month == 'February':
       month = 'October' 
       day = day + 7
       if day < 31:
            ed_day = day 
       else :
            month = 'November'
            ed_day = 30 - day     
    elif month == 'March':
       month = 'November'
       day = day + 7
       if day <= 30:
            ed_day = day 
       else :
            month = 'December'
            day = day - 1
            ed_day = 31 - day    
    elif month == 'April':
       month = 'December' 
       day = day + 7
       if day <= 31:
            ed_day = day 
       else :
            month = 'January'
            ed_day = 31 - day
    elif month == 'May':
       month = 'February' 
       day = day + 7
       if day <= 28:
            ed_day = day 
       else :
            month = 'March'
            day = day - 1           
            ed_day = 31 - day 
    elif month == 'June':
       month = 'March' 
       day = day + 7
       if day <= 31:
            ed_day = day 
       else :
            month = 'April'
            day = day - 1
            ed_day = 30 - day 
    elif month == 'July':
       month = 'April'
       day = day + 7
       if day <= 30:
            ed_day = day 
       else :
            month = 'May'
            day = day - 1
            ed_day = 31 - day
    elif month == 'August':
       month = 'May'
       day = day + 7
       if day <= 31:
            ed_day = day 
       else :
            month = 'June'
            ed_day = 30 - day
    elif month == 'September':
       month = 'June'
       day = day + 7
       if day <= 30:
            ed_day = day 
       else :
            month = 'July'
            day = day - 1
            ed_day = 31 - day
    elif month == 'October':
       month = 'July' 
       day = day + 7
       if day <= 31:
            ed_day = day 
       else :
            month = 'August'
            ed_day = 30 - day
    elif month == 'November':
       month = 'August'
       day = day + 7
       if day <= 30:
            ed_day = day 
       else :
            month = 'September'
            day = day - 1
            ed_day = 31 - day
    elif month == 'December':
       month = 'September'
       day = day + 7
       if day <= 31:
            ed_day = day 
       else :
            month = 'October'
            ed_day = 31 - day

    print(f"The predicted expected date of your baby's delivery is {day} {month} :)")
     
print('Please write the month number of the month in which you had your last menstrual period (eg: 1 for January / 12 for December)')           
m = monthName(int(input('--> ')))
if(m == 'invalid'):
    print('Invalid date selection')
    _exit(1)
print("Please write the day of the month (e.g 14, 16, 22 etc)")
d = int(input())
predict(m, d)