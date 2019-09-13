class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price

    def full_name(self):
        return f"{self.brand}   {self.model_name}"

    def make_a_call(self,number):
        return f"calling {number}"

class Smartphone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

phone = Phone('nokia','1020',10000)
smartphone = Smartphone('onePLus','7',80000,'6GB','64GB','48MP')
print(phone.full_name())
print(smartphone.full_name() + f"and price is{smartphone.price}")


         