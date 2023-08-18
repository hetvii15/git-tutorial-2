class Location:
    def __init__(self,name,code):
        self.name=name
        self.code=code

class Movement:
    def __init__(self,from_location, to_location,product,quantity):
        self.from_location=from_location
        self.to_location=to_location
        self.product=product
        self.quantity=quantity

    @staticmethod
    def movement_by_product(product):
        for m in movements:
            if m.product==product:
                if m.quantity > product.stock_at_location[m.from_location]:
                    raise Exception("Not enough stock")
                product.stock_at_location[m.from_location] -= m.quantity
                product.stock_at_location[m.to_location] += m.quantity
                print("\n")
                print(f"{product.name} moved from {m.from_location} to {m.to_location} with quantity {m.quantity}",file=f)
                print("\n")
                # return product.name , "moved from", m.from_location ,"to", m.to_location ,"with quantity", m.quantity
            
class Product:
    def __init__(self,name,code):
        self.name = name
        self.code = code
        self.stock_at_location = {}

    def printProduct():
        for product in products:
            print(product.name, product.stock_at_location)

    def GroupBy():
        for location in locations:
            print(location.name)
            for p in products:
                if p.stock_at_location[location.name]:
                    print(f"{p.name}:{p.stock_at_location[location.name]}")   
               

#create 4 location objects
locations = []
locations.append(Location("Warehouse A","A01"))
locations.append(Location("Warehouse B","B01"))
locations.append(Location("Warehouse C","C01"))
locations.append(Location("Warehouse D","D01"))

#create 5 product objects and add stock at different locations
p1 = Product("Toys", "001")
p1.stock_at_location = {
    "Warehouse A":15,
    "Warehouse B":30,
    "Warehouse C":0,    
    "Warehouse D":0
}
p2 = Product("sports","002")
p2.stock_at_location = {
    "Warehouse A":0,
    "Warehouse B":20,
    "Warehouse C":0,
    "Warehouse D":0
}
p3 = Product("Clothes","003")
p3.stock_at_location = {
    "Warehouse A":0,
    "Warehouse B":0,
    "Warehouse C":30,
    "Warehouse D":0
}
p4 = Product("Footwear","004")
p4.stock_at_location = {
    "Warehouse A":0,
    "Warehouse B":0,
    "Warehouse C":0,
    "Warehouse D":50
}
p5 = Product("Electronics","005")
p5.stock_at_location ={
    "Warehouse A":30,
    "Warehouse B":0,
    "Warehouse C":0,
    "Warehouse D":0
}

products = [p1,p2,p3,p4,p5]

#create movement objects
m1 = Movement("Warehouse A","Warehouse B", p1,6 )
m2 = Movement("Warehouse B","Warehouse C", p2,8 )
m3 = Movement("Warehouse C","Warehouse D", p3,9 )
m4 = Movement("Warehouse D","Warehouse A", p4,7 )
m5 = Movement("Warehouse A","Warehouse C", p5,10 )
m6 = Movement("Warehouse B","Warehouse D", p1,12)

movements =[m1,m2,m3,m4,m5,m6]

# file creation
f = open("output.txt","w")

print("Movement of Toys:")
Movement.movement_by_product(p1)
print("Movement of Sports:")
Movement.movement_by_product(p2)
print("Movement of Clothes:")
Movement.movement_by_product(p3)
print("Movement of Footwear:")
Movement.movement_by_product(p4)
print("Movement of Electronics:")
Movement.movement_by_product(p5)
print("\n")

Product.printProduct()
print("\n")

Product.GroupBy()

