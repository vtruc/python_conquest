# string format symbol

bankName = "Asia Commercial Bank"
numOfEmployees = 10000
interestRate = 4.678

info_1 = " Name of Bank: " + bankName + "\n Number of employees: " + str(numOfEmployees)
print(info_1)
print("*" * 50)

info_2 = " Name of Bank: %s \n Number of employees: %i \n Interest Rate: %.2f" % (
    bankName,
    numOfEmployees,
    interestRate,
)
print(info_2)
print("*" * 50)

# f string
info_3 = f" Name of Bank: {bankName}\n Number of employees: {numOfEmployees}\n Interest rate: {interestRate}"
print(info_3)
print("*" * 50)

info_4 = f" Name of Bank: {bankName}\n Number of employees: {numOfEmployees:,}\n Interest rate: {interestRate:.2f}"
print(info_4)
print("*" * 50)

info_5 = f" Name of Bank: {bankName}\n Number of employees: {numOfEmployees:,.2f}\n Interest rate: {interestRate:.2f}"
print(info_5)
