# Дан файл, содержащий различные даты.
# Каждая дата - это число, месяц и год.
# Найти самую раннюю дату. [02-8.1-ML-29]

def is_first_date_earlier(date1, date2):
    day1, month1, year1 = map(int, date1.split('-'))
    day2, month2, year2 = map(int, date2.split('-'))
    if year1 < year2:
        return True
    elif year1 > year2:
        return False
    elif month1 < month2:
        return True
    elif month1 > month2:
        return False
    elif day1 < day2:
        return True
    elif day1 > day2:
        return False
    else:
        return False



def main():
    with open('files/dates.txt') as dates_file:
        dates = dates_file.readlines()
        erliest_date = dates[0]
        for date in dates:
            if is_first_date_earlier(date, erliest_date):
                erliest_date = date
    print(erliest_date)

if __name__ == "__main__":
    main()
