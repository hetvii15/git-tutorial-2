import re
import datetime as dt

class Customer:
    def __init__(self, name, email, phone, street, city, state, country,company, type):
        self.name = name
        self.email=email
        self.phone=phone
        self.street=street
        self.city=city
        self.state=state
        self.country=country
        self.company=company
        self.type=type
        self.validation()

    def validation(self):      
        if self.type not in ["Company","Billing","Contact","Shipping"]:
            raise ValueError("Invalid customer type")
        
        if self.name.isdigit():
            raise ValueError("Name cannot contain numbers")

        if self.city.isdigit():
            raise ValueError("City cannot contain numbers")
        
        if self.state.isdigit():
            raise ValueError("state cannot contain numbers")
        
        if self.country.isdigit():
            raise ValueError("Country cannot contain numbers")
        
        if not re.match("(0|91)?[6-9][0-9]{9}",self.phone):
            raise ValueError("invalid phone number")
        
        if not re.match("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}",self.email):
            raise ValueError("invalid email")
    
    def Cust_info(self):
        print(f"Name:{self.name} Email:{self.email} Phone:{self.phone} Street:{self.street} City:{self.city} State:{self.state} Country:{self.country} Company:{self.company} Type:{self.type}")

class Order:
    order_lines=[]
    def __init__(self,number,date,company,billing,shipping):
        self.number=number
        self.date=date
        self.company=company
        self.billing=billing
        self.shipping=shipping
        self.total_amount = 0

        date1 = self.date
        today = dt.date.today()
        today1 = dt.date.isoformat(today)
        if date1<today1:
            print("Date is invalid")

    def totalamount(self):
        for o in Order.order_lines:
            if o.order == self:
                self.total_amount += o.subtotal

    def order_info(self):
        print(f"Order number:{self.number} Date:{self.date} Company:{self.company} Billing:{self.billing} Shipping:{self.shipping} Total amount:{self.total_amount}")
   
    def filterOrder():
        print("Filter order based on current month")
        inputmonth = input("Enter current month(in number):")
        for o in orders:
            if o.date[-5:-3]==inputmonth :
                o.order_info()
        print("\n")

    def sortOrder():
        print("Sort orders based on date:")
        for i in range(len(orders)):
            for j in range(len(orders)):
                if orders[i].date < orders[j].date:
                    temp = orders[i]
                    orders[i]=orders[j]
                    orders[j]=temp
        print("sorted order list:")
        for o in orders:
            o.order_info()
        print("\n")

    def searchOrder():
        print("Search order")
        product_found = False
        inputnumber = input("Enter order number:")
        for o in orders:
            if o.number==inputnumber:
                product_found=True
                print("order is available")
                o.order_info()
        if not product_found:
            print("order not found")
        print("\n")

    def displayProduct():
        print("Display product orders")
        product = input("enter product name:")
        for o in orders:
            for o1 in Order.order_lines:
                if o1.product==product:
                    if o1.order==o:
                        o.order_info()
                
class OrderLine:
    def __init__(self,order,product,quantity,price):
        self.order=order
        self.product=product
        self.quantity=quantity
        self.price=price
        self.subtotal=self.quantity*self.price 


c1 = Customer("ria","ria@gmail.com","9800980098","powder gali","mumbai","maharashtra","india","abc","Billing")
c2 = Customer("Tarun","tarun@gmail.com","7659876598","tirupati nagar","Rajkot","Gujarat","India","afg","Shipping")
c3 = Customer("Jia","jia@gmail.com","8005480054","paldi","Ahmedabad","Gujarat","India","xyz","Company")
c4 = Customer("Sanket","sanket@gmail.com","9763397633","africa colony","Rajkot","Gujarat","India","jkl","Contact")

o1 = Order("O01","2023-08-23",c1.company,c1.type,None)
o2 = Order("O02","2023-09-06",c2.company,None,c2.type)
o3 = Order("O03","2023-08-25",c3.company,None,None)
o4 = Order("O04","2023-08-30",c4.company,None,None)

orders = [o1,o2,o3,o4]

ol1 = OrderLine(o1,"tshirt",10,200)
ol2 = OrderLine(o2,"Iphone 14",2,70000)
ol3 = OrderLine(o3,"Microwave",1,80000)
ol4 = OrderLine(o4,"Toys",5,300)


Order.order_lines = [ol1,ol2,ol3,ol4]

print("customer information:")
c1.Cust_info()
c2.Cust_info()
c3.Cust_info()
c4.Cust_info()
print("\n")

print("Order information:")
o1.totalamount()
o1.order_info()

o2.totalamount()
o2.order_info()

o3.totalamount()
o3.order_info()

o4.totalamount()
o4.order_info()
print("\n")

Order.filterOrder()
Order.sortOrder()
Order.searchOrder()
Order.displayProduct()

