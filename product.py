def_init_(self,product_id,name, description, price)
self.product-id =product_id
self.name=Name
self.description =description
self.price =price
self.status ='Active' #Default status is active


def update_product(self, name=None, description=None, price=None);
    if name:
        self.name=name
        if description=description
if price: self.price=price
print(f"Product{self.name} update.")


def suspend(self):
    self.status='Suspended'
    print(f"Product{self.name.name}suspended.")


    def reactivate(self):
        self.status ='Active'
        print(f"Product {self.name} reactivated.")
        

