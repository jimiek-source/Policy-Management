def_init_(self, payment_id, amount, date,policyholder, product):
self.payment_id=payment_id
self.amount=amount
self.date=date
self.policyholder=policyholder
self.product=product
self.status='completed' #Default payment status is completed

def process_payment(self):
    self.policyholder.add_product(self.product)
    print(f"payment of ${self.amount}for product{self.product.name} processsed successfully.")

    def send_reminder(self):
        print(f"Reminder of ${self.amount} for product.name} is due for (self.policyholder.name}.")

        def impose_penalty(self)
            if self.status !='completed':
                print(f"Penalty of $30 imposed on {self.policyholder.name} for overdue payment on {self.product.name}.")
