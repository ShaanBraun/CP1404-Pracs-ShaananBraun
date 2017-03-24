
print("Welcome to the Electricity Bill Estimator")
print()


TARIFF_1 = 0.244618
TARIFF_2 = 0.136928

centsPerKWH = 0
dailyUseKWH = 0
numberOfBillingDays = 0
estimatedBill = 0

tariffChoice = int(input("Which Tariff, 1 or 2?: "))
if tariffChoice == 1:
    centsPerKWH = TARIFF_1
elif tariffChoice == 2:
    centsPerKWH = TARIFF_2
else:
    print("Invalid Tariff")


dailyUseKWH = float(input("Enter Daily Use in kWh: "))
numberOfBillingDays = int(input("Enter Number of Billing Days: "))

print()
estimatedBill = centsPerKWH*dailyUseKWH*numberOfBillingDays

print("Estimated Bill: $"+str(estimatedBill))