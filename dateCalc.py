import datetime

birthDateInput = input("Enter your birth date: ")
birthDate = datetime.datetime.strptime(birthDateInput, "%d-%m-%Y")
daystoadd = datetime.timedelta(days=999)

print("{:%d-%m-%Y}".format(birthDate + daystoadd))