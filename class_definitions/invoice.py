# Zachary Hayes
class Invoice:
    '''Invoice Class'''

    def __init__(self, id, cust_id, lname, fname, phone, add, items={}):
        self.invoice_id = id
        self.customer_id = cust_id
        self.last_name = lname
        self.first_name = fname
        self.phone_number = phone
        self.address = add
        self.items_with_price = items

    def add_item(self, item_and_price):
        self.items_with_price.update(item_and_price)

    def create_invoice(self):
        running_total = 0
        for item in self.items_with_price:
            print(item + ".....$%.2f" % self.items_with_price.get(item))
            running_total += self.items_with_price.get(item)
        tax = running_total * .06
        print("Tax.....$%.2f" % tax)
        print("Total.....$%.2f" % (running_total + tax))


# Driver code
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()