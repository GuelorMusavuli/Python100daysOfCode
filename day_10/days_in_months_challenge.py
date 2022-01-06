def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """
    :param year: year from the user's input
    :param month: month from the user's input
    :return: the number of days in the passed in month
    """
    # Number of days in month from January to December for a non-leap year.
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]  # -1 bcz the months don't start from 0 as in the list


print(days_in_month(int(input("Enter a year: ")), int(input("Enter a month: "))))
