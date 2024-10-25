import calendar

def display_months():

    months = calendar.month_name[1:]
    
    for month in months:
        print(month)


print("The 12 Months of the year are:")
display_months()