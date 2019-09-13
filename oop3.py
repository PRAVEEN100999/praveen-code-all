class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

    @property
    def complete_specification(self):
        return f"{self.brand} {self.model_name} {self._price}"
   
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)
        return self._price

phone1 = Phone('nokia','1100',1000)
# phone1._price = -500
print(phone1.complete_specification)            