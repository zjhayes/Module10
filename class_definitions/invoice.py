# Zachary Hayes
from class_definitions.customer import Customer


class Invoice:
    '''Invoice Class'''

    def __init__(self, id, cust, items={}):
        self.invoice_id = id
        self.customer = cust
        self.items_with_price = items

    def add_item(self, item_and_price):
        self.items_with_price.update(item_and_price)

    def create_invoice(self):
        running_total = 0
        print(self.customer.display())
        for item in self.items_with_price:
            print(item + ".....$%.2f" % self.items_with_price.get(item))
            running_total += self.items_with_price.get(item)
        tax = running_total * .06
        print("Tax.....$%.2f" % tax)
        print("Total.....$%.2f" % (running_total + tax))


# Driver
captain_mal = Customer(1, 'Reynolds', 'Mel', 'No phones', 'Firefly, somewhere in the verse')
invoice = Invoice(1, captain_mal)
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
del captain_mal