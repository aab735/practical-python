from porty.typedproperty import typedproperty,String,Integer,Float

class Stock:
    #__slots__ = ('name','_shares','price')

    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self,name,shares,price):
        self.name=name
        self.shares=shares
        self.price=price
    
    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'

    @property
    def cost(self):
        return self.shares*self.price
    
    def sell(self,sellShareCount):
        self.shares -= sellShareCount

    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self,value):
        if not isinstance(value,int):
            raise TypeError('Expected an integer')
        self._shares=value
