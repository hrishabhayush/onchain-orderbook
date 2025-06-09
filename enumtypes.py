from enum import Enum

class OrderType(Enum):
    GoodTillCancel = 0
    FillAndKill = 1

class Side(Enum):
    Buy = 0
    Sell = 1

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
    


    


    




