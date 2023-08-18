import re
class Customer:
    def __init__(self, name, email, phone, street, city, state, country, company, type):
        self.name = name
        self.email=email
        self.phone=phone
        self.street=street
        self.city=city
        self.state=state
        self.country=country
        self.company=company
        self.type=type

        if type not in ["company","billing","contact","shipping"]:
            raise ValueError("Invalid customer type")
        
        if name.isdigit():
            raise ValueError("Name cannot contain numbers")

        if city.isdigit():
            raise ValueError("City cannot contain numbers")
        
        if state.isdigit():
            raise ValueError("state cannot contain numbers")
        
        if country.isdigit():
            raise ValueError("Country cannot contain numbers")

        if not isinstance(company,Customer):
            raise ValueError("company must be customer object")
        
        if not re.match("(0|91)?[6-9][0-9]{9}",phone):
            raise ValueError("invalid phone number")
        
        if not re.match("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}"):
            raise ValueError("invalid email")
    
    def Cust_info(self):
        print(f"Name:{self.name} Email:{self.email} Phone:{self.phone} Street:{self.street} City:{self.city} State:{self.state} Country:{self.country} Company:{self.company} Type:{self.type}")
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


# c1 = Customer("ria","ria@gmail.com","9800980098","powder gali","mumbai","maharashtra","india","billing")
































# •	Create a new class named "Customer" with below members. "name","email","phone","street","city","state","country","company","type".
# •	"type" must be from "company,contact,billing,shipping".
# •	"Company" must be a Customer object which is the parent object.
# •	Apply Multiple possible validation for phone number and email
# •	Does not allowed number in name,city,state and country


# •	Create a new class named "Order" with members "number","date", "company", "billing", "shipping", "total_amount","order_lines".
# •	"company", "billing", "shipping" are objects of Customer.
# •	"date" must be today or the future. Does not allow past date.
# •	"total_amount" auto calculated based on different products inside order.
# •	"order_lines" is list of objects of "OrderLine"


# •	create a new class named "OrderLine" with members "order", "product", "quantity", "price", "subtotal".
# •	"order" is the object of Order.
# •	"subtotal" is auto calculated based on quantity and price.


# •	Display Order and Customer Information
# •	Sort orders based on "date".
# •	User can filter the current month orders
# •	Search Orders from its number.
# •	List/Display all orders of a specific product.
