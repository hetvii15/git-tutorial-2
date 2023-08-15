class Customer:
    def __init__(self, name, emial, phone, street, city, state, country, company, type):
        self.name = name
        self.email=emial
        self.phone=phone
        self.street=street
        self.city=city
        self.state=state
        self.country=country
        self.company=company
        self.type=type

class Order:
    def __init__(self,number,date,company,billing,shipping,total_amount):
        self.number=number
        self.date=date
        self.company=company
        self.billing=billing
        self.shipping=shipping
        self.total_amount=total_amount
        self.order_lines=[]

class OrderLine:
    def __init__(self,order,product,quantity,price):
        self.order=order
        self.product=product
        self.quantity=quantity
        self.price=price
        self.subtotal=self.quantity*self.price
9
