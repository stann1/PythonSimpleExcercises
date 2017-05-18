""" Prints the days from your birthday till now """

import datetime

def print_date_diff():
    birthdate_input = input("Enter your birth date: ")
    birthdate = datetime.datetime.strptime(birthdate_input, "%d-%m-%Y")
    daystoadd = datetime.timedelta(days=999)

    print("{:%d-%m-%Y}\r\n".format(birthdate + daystoadd))

print_date_diff()
