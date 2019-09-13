class Laptop:
    def __init__(self,brand,model_name,price):
        #instance variavle 
        self.brand = brand
        self.model_name = model_name
        self.price = price
        self.Laptop_name = brand + '' +model_name

    def apply_discount(self,num):
        # self.price
        off_price = (num/100)*self.price
        return self.price -  off_price


laptop1 = Laptop('hp','bs179',87000)
print(laptop1.apply_discount(1))