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

class seller:

    inventory = []
    inventoryTiming = []

    def __init__(self, name, receivedMoney): 
        self.name = name
        self.receivedMoney = receivedMoney

    def newItemSold(object, month, day, year):
        seller.inventory.append(item.object)
        date = "" + month +"/" + date + "/" + year
        seller.inventoryTiming.append(date)

    def getStatistics():
        salesCount = seller.inventory.len()
        salesValue = 0
        retailValue = 0
        for i in range(salesCount):
            salesValue += seller.inventory.index(i).salePrice
            retailValue += seller.inventory.index(i).retailPrice
        profit = salesValue - retailValue
        transferMoney = profit - seller.receivedMoney
        return "Seller: " + seller.name + "\nSales Count: " + str(salesCount) + "\nProfit: $" + str(profit) + "\nMoney to be transferred: $" + str(transferMoney)

# salesmen
Araash = seller("Araash", 240)
i1 = item("Chaitanya", "T-Shirt", "White", "Small", "Large", 20, 3.2, True, 1)
Araash.newItemSold(i1, 6, 5, 2022)
Araash.getStatistics()

Henrik = seller("Henrik", 60)
Patrick = seller("Patrick", 30)
Kenny = seller("Kenny", 375)
Ronit = seller("Ronit", 140)







    






