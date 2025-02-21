# Import necessary classes

product_1 = Product(1)
product_2 = Product(2)


policyholder_1 = Policyholder(1)
policyholder_2 = Policyholder(2)


#Register policyholders

policyholder_1.register()
policyholder_2.register()

payment process

payment_1 = Payment( policyholder_1, product_1)
payment_1 =.process_payment(policyholder_2, product_2)

payment_2 = Payment()
payment_2.process_payment()


#Display account of policyholders.

policyholder_1.display_account_detail()
policyholder_2.display_account_details()




# suspend and reactivate policyholders

policyholder_1. suspend()
policyholder_1. display()
policyholder_1. display_account_details()

policyholder_1.reactivate()
policyholder_1.display_account_details()


# suspend and reactivate products

product_1.suspend()
product_1.reactivate().
 

