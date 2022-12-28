#This program calculated the age with month, week, day
# the user enters age and program calculated how the user live month, week, day 


age =input("Please, Enter your age: ").strip()
unit = input("Please choose Time unit: (months, weeks, days):  ")

months =int(age) * 12
weeks =months * 4
days = int(age) *365


if unit == 'months':
    print(f"you lived for {months: ,} Months")
elif unit == 'days':
    print(f"you lived for {days: ,} Days")
elif unit == 'weeks':
    print(f"you lived for {weeks: ,} weeks")
else: 
    print("wrong input")        
