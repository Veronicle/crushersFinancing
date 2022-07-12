class item:
    
    def __init__(self, customer, style, color, logo, size, salePrice, retailPrice, customized, payDayWeek):
        self.customer = customer
        self.style = style
        self.color = color
        self.logo = logo
        self.size = size
        self.salePrice = salePrice
        self.retailPrice = retailPrice
        self.customized = customized
        self.payDayWeek = payDayWeek

    def getSalePrice(self):
        return self.salePrice
    
    def getRetailPrice(self):
        return self.retailPrice

class seller:

    pendingInventory = []
    soldInventory = []
    pendingInventoryTiming = []
    soldInventoryTiming = []

    def __init__(self, name, receivedMoney): 
        self.name = name
        self.receivedMoney = receivedMoney
    
    def getReceivedMoney(self):
        return self.receivedMoney

    def getName(self):
        return self.name

    def newOrder(self, Object, month, day, year):
        seller.pendingInventory.append(Object)
        date = "" + str(month) +"/" + str(day) + "/" + str(year) 
        seller.pendingInventoryTiming.append(date)

    def itemSold(self, Object, month, day, year):
        seller.soldInventory.append(Object)
        date = "" + str(month) +"/" + str(day) + "/" + str(year)
        seller.soldInventoryTiming.append(date)

    def getStatistics(self):
        salesCount = len(seller.soldInventory)
        salesValue = 0
        retailValue = 0
        for i in range(salesCount):
            salesValue += (seller.soldInventory[i]).getSalePrice()
            retailValue += (seller.soldInventory[i]).getRetailPrice()
        profit = salesValue - retailValue
        transferMoney = profit - seller.getReceivedMoney(self)
        return "Seller: " + seller.getName(self) + "\nSales Count: " + str(salesCount) + "\nProfit: $" + str(profit) + "\nMoney to be transferred: $" + str(transferMoney)
"""
# salesmen
Araash = seller("Araash", 240)
i1 = item("Chaitanya", "T-Shirt", "White", "Small", "Large", 20, 3.2, True, 1)
Araash.itemSold(i1, 6, 5, 2022)
i2 = item("Boris", "T-Shirt", "White", "Small", "Large", 20, 3.2, True, 1)
Araash.itemSold(i2, 1, 2, 3)
# print(dir(Araash)) => shows all possible emthods for Araash
print(Araash.getStatistics())

Henrik = seller("Henrik", 60)
Patrick = seller("Patrick", 30)
Kenny = seller("Kenny", 375)
Ronit = seller("Ronit", 140)
"""








    






