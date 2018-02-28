import csv

class processCSV:
    def __init__(self, inFileName ='None', outFileName='None'):
        self.inFileHandle = open(inFileName, 'rb')
        self.outFileHandle = open(outFileName, 'wb')
        self.exchanges=[]
    def processLines(self):
        reader = csv.reader(self.inFileHandle, delimiter=' ', quotechar='|')
        writer = csv.reader(self.outFileHandle, delimiter=' ', quotechar='|',  quoting=csv.QUOTE_NONE)

        for row in reader:
            exchangeName =
            coinName     =
            numCoins     =
            coinPrice    =
            index        = checkAndGetIndex(exchangeName)
            exchanges[index].parseLine()


    def checkAndGetIndex(self, exchangeName='None'):
        i = 0
        for a in self.exchanges:
            i= i + 1
            if a.name == exchangeName:
                return i

        self.exchanges.append(exchange(exchangeName))
        return i

####exchange Class####
class exchange:
    def __init__(self, exchangeName=''):
        self.name=exchangeName
        self.coins=[]

    def parseLine(self, inParameters):
        index = self.checkAndGetIndex(inParameters.coinName)

        if inParameters.action == 'BUY':
            self.coins[index].addBuy(inParameters.numCoins, inParameters.price, inParameters.time)
        elif inParameters.action == 'SELL':
            self.coins[index].addSell(inParameters.numCoins, inParameters.price, inParameters.time),
        elif inParameters.action == 'WITHDRAW':
            price = self.coins[index].withdraw(inParameters.numCoins)
        elif inParameters.action == 'DEPOSIT':
            self.coins[index].deposit(inParameters.numCoins, inParameters.price)

        return price

    def checkAndGetIndex(self, coinName='None'):
        i = 0
        for a in self.coins:
            i= i + 1
            if a.coin == coinName:
                return i

        self.coins.append(coinWallet(coinName))
        return i

####coinWallet Class####
class coinWallet:
    def __init__(self, coinName='None'):
        self.coin=coinName
        self.coin.holdings=[]

    def addBuy(self, numCoins=0, price=0, time=''):
        entry= {'num': numCoins, 'price': price, 'time': time}
        self.coin.holdings.append(entry)

    def addSell(self, numCoins=0, price=0, time=''):
        while(numCoins > 0):
            lastEntry = self.coin.holdings[-1]
            if lastEntry.get('num') < numCoins:
                proceeds = numCoins*price
                cost = lastEntry.get('num') * lastEntry.get('price')
                self.coin.holdings.pop()
                numCoins = numCoins- lastEntry.get('num')
            else:
                proceeds = numCoins*price
                cost = numCoins * lastEntry.get('price')
                self.coin.holdings[-1]['num'] = self.coin.holdings[-1]['num'] - numCoins
                numCoins = 0

    def deposit(self, numCoins=0, price=0, time=''):
        entry= {'num': numCoins, 'price': price, 'time': time}
        self.coin.holdings.append(entry)

    def withdraw(self, numCoins=0):
        totalCost=0
        numCoinsTemp=numCoins

        while(numCoinsTemp > 0):
            lastEntry = self.coin.holdings[-1]
            if lastEntry.get('num') < numCoinsTemp:
                totalCost = lastEntry.get('num')*lastEntry.get('price')
                self.coin.holdings.pop()
                numCoinsTemp = numCoinsTemp- lastEntry.get('num')
            else:
                totalCost = numCoinsTemp*lastEntry.get('price')
                self.coin.holdings[-1]['num'] = self.coin.holdings[-1]['num'] - numCoinsTemp
                numCoinsTemp = 0

        entry= {'num': numCoins, 'price': totalCost/numCoins, 'time': '0'}
        return entry
