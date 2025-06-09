from enum import Enum

class OrderType(Enum):
    GoodTillCancel = 0
    FillAndKill = 1

class Side(Enum):
    '''
    
    '''
    BUY = 0
    SELL = 1

class Order(object):
        '''
        The order should contain the information about the ordertype, whether it is buy
        or sell, the price, and the quantity that is initial quantity and what is the
        remaining quantity. 
        '''
        
        def __init__(self, orderType: OrderType, orderId, side: Side, price, initialQuantity, remainingQuantity):
            '''
            Initialize all the quantities 
            '''
            self._orderType = orderType
            self._orderId = orderId
            self._side = side
            self._price = price
            self._initialQuantity = initialQuantity
            self._remainingQuantity = remainingQuantity

        def getOrderId(self):
            return self._orderId
        
        def getSide(self):
            return self._side
        
        def getPrice(self):
            self._price

        def getOrderType(self):
            return self._orderType
        
        def getInitialQuantity(self):
            return self._initialQuantity
        
        def getRemainingQuantity(self):
            return self._remainingQuantity
        
        def getFilledQuantity(self):
            return self.getInitialQuantity() - self.getRemainingQuantity()

        def fill(self, quantity):
            assert(quantity <= self.getRemainingQuantity(), "the quantity to be filled must be less"
            " than or equal to the remaining quantity")
           
            self._remainingQuantity -= quantity


class OrderModify(object):
    '''
    Allows to modify your order
    '''

    def __init__(self, orderId, side: Side, price, quantity):
        self._orderId = orderId
        self._side = side
        self._price = price
        self._quantity = quantity

    def getOrderId(self):
        return self._orderId
    
    def getSide(self):
        return self._side
    
    def getPrice(self):
        return self._price
    
    def getQuantity(self):
        return self._quantity

class TradeInfo(object):
    def __init__(self, orderId, price, quantity):
        self._orderId = orderId 
        self._price = price
        self._quantity = quantity


class Trade(object):
    '''
    Information about the trade
    '''
    def __init__(self, bidTrade: TradeInfo, askTrade: TradeInfo):
        self._bidTrade = bidTrade
        self._askTrade = askTrade

    def getBidTrade(self):
        return self._bidTrade
    
    def getAskTrade(self):
        return self._askTrade


class LevelInfo(object):
        '''
        Contains the information where the orderbook is at right now. 
        '''

        def __init__(self, quantity, price, bids, asks):
            '''
            Write the documentation for the levelInfo
            '''
            # We need some sort of tracker to track all the bids, asks, so the orderbook can start empty
            self._bids = bids
            self._asks = asks
            self._quantity = quantity
            self._price = price  

        def orderBookLevelInfo(self, quantity, price, side: Side):
            self._quantity = quantity
            self._price = price
            self._side = side

        def getBids(self):
            return self._bids
        
        def getAsks(self):
            return self._asks
        
class OrderEntry(object):
    
    def __init__(self, order, time):
        self._order = order
        self._time = time
        

        