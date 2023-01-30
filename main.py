def leap_year(year):
    # divided by 100 means century year (ending with 00)
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        print("{0} is a leap year".format(year))

    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 == 0) and (year % 100 != 0):
        print("{0} is a leap year".format(year))

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        print("{0} is not a leap year".format(year))
        return year


def even_or_odd_number(num):
    if (num % 2) == 0:
        print("{0} is Even".format(num))
    else:
        print("{0} is Odd".format(num))
    return num



def add_num(x, y):
    return x + y


def Square(X):
    # computes the Square of the given number
    # and return to the caller function
    return (X * X)


if __name__ == '__main__':
    leap_year(2020)
    even_or_odd_number(2000)
