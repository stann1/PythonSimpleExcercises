ratesDict = {"BGN": 1, "USD": 1.79549, "EUR": 1.95583, "GBP": 2.53405}

amountInput = input("Enter amount to convert: ")
currFromInput = input("From currency code: ")
currToInput = input("To currency code: ")

currFrom = ratesDict[currFromInput]
currTo = ratesDict[currToInput]

convAmount = float(amountInput) * (currFrom / currTo)

print("{0:.2f} {1}".format(convAmount, currToInput))
