import datetime

def get_dates(starting_date,ending_date ,search_day):
    current_date = starting_date
    datelist = []
    while current_date <= ending_date:
        if datetime.datetime.strftime(current_date,"%A") == search_day:
            datelist.append(current_date.date())
        current_date = current_date + datetime.timedelta(days=1)
    return datelist

starting_date = datetime.datetime.strptime(input("Enter starting date(dd-mm-yyyy) : "),"%d-%m-%Y")
ending_date = datetime.datetime.strptime(input("Enter starting date(dd-mm-yyyy) : "),"%d-%m-%Y")
search_day = input("Enter the day : ").capitalize()

date_list = get_dates(starting_date, ending_date, search_day)

for i in date_list:
    print(i)
