DISCOUNT_RATE = 0.1

numberOfItems = int(input("Number of Items: "))
while numberOfItems <= 0:
    print("Invalid number of items, try again.")
    numberOfItems = int(input("Number of Items: "))

itemPrices = []
totalPrice = 0.0

for i in range(numberOfItems):
    itemPrices.append(input("Item " +str(i + 1)+ " Price: $"))

# for i in range(len(itemPrices)):
#     totalPrice += itemPrices[i]

for price in itemPrices:
    totalPrice += price

if totalPrice > 100:
    totalPrice -= totalPrice * DISCOUNT_RATE

print("Total Price for "+str(numberOfItems)+ " items is $"+str(totalPrice))