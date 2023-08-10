class Category:
    def __init__(self,name,code,parent):
        self.name=name
        self.code=code
        self.parent=parent
        self.products=[]
        self.display_name=""

    def getdisplay_name(self):
        if self.parent is None:
            self.display_name = self.name
            return self.display_name
        else:
            self.display_name = self.parent.getdisplay_name() + ' > ' + self.name
            return self.display_name

    
    def addProducts(self,product):
        self.products.append(product)
    
    def getProducts(self):
        for i in range(len(self.products)):
            print(f"Product Name:{self.products[i].name}")
            print(f"Product Code:{self.products[i].code}")
            print(f"Product Category:{self.products[i].category.name}")
    
    def getCode(self):
        return self.code
    
    def groupProducts():
        print("Product list grouped by category:")
        for category in categories:
            print(category.name)
            for product in category.products:
                print(f"\t{product.name} {product.code}")
    
    def orderProducts():
        print("Product list ordered by category name:")
        for i in range(len(categories)):
            for j in range(len(categories)):
                if categories[i].name < categories[j].name:
                    tempCatName = categories[i]
                    categories[i]=categories[j]
                    categories[j]=tempCatName

        for category in categories:
            print(category.name)
            for product in category.products:
                print(f"\t{product.name} {product.code}")
    
class Product:
    def __init__(self,name,code,category):
        self.name=name
        self.code=code
        self.category=category

#create 5 category objects with parent and child relation
vehicle = Category("Vehicle", "V01",None)
car = Category("Car","C01",vehicle)
electric =Category ("Electric","E01",car)
petrol=Category("Petrol","P01",car)
diesel=Category("Diesel","D01",car)

categories = [vehicle,car,electric,petrol,diesel]

#create 3 objects of vehicle category
bike = Product("Bike","V011",vehicle)
car1 = Product("Car","V012",vehicle)
bus = Product("Bus","V013",vehicle)

#add vehicle products to the product list
vehicle.addProducts(bike)
vehicle.addProducts(car1)
vehicle.addProducts(bus)

#create 3 objects of car category
Ciaz = Product("Ciaz","C011",car)
Creta = Product("Creta","C012",car)
Brezza = Product("Brezza","C013",car)

#add car products to the product list
car.addProducts(Ciaz)
car.addProducts(Creta)
car.addProducts(Brezza)

#create 3 objects of petrol category
p1=Product("Ciaz","P011",petrol)
p2=Product("Creta","P012",petrol)
p3=Product("Brezza","P013",petrol)

#add petrol products to the product list
petrol.addProducts(p1)
petrol.addProducts(p2)
petrol.addProducts(p3)

#create 3 diesel objects
d1=Product("Ciaz","D011",diesel)
d2=Product("Creta","D012",diesel)
d3=Product("Brezza","D013",diesel)

#add diesel products in product list
diesel.addProducts(d1)
diesel.addProducts(d2)
diesel.addProducts(d3)

#create 3 electric objects
e1=Product("Ciaz","E011",electric)
e2=Product("Creta","E012",electric)
e3=Product("Brezza","E013",electric)

#add electric products in product list
electric.addProducts(e1)
electric.addProducts(e2)
electric.addProducts(e3)

#print category details
print(f"Category 1:{vehicle.name} Code: {vehicle.getCode()} Display name: {vehicle.getdisplay_name()}")
vehicle.getProducts()
print("\n")

print(f"Category 2:{car.name} Code: {car.getCode()} Display name: {car.getdisplay_name()}")
car.getProducts()
print("\n")

print(f"Category 3:{electric.name} Code: {electric.getCode()} Display name: {electric.getdisplay_name()}")
electric.getProducts()
print("\n")

print(f"Category 4:{petrol.name} Code: {petrol.getCode()} Display name: {petrol.getdisplay_name()}")
petrol.getProducts()
print("\n")

print(f"Category 5:{diesel.name} Code: {diesel.getCode()} Display name: {diesel.getdisplay_name()}")
diesel.getProducts()
print("\n")

#group by
Category.groupProducts()
print("\n")

#order by
Category.orderProducts()