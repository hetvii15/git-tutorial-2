class Category:
    def __init__(self,name,code):
        self.name=name
        self.code=code
        self.product=0
    

    def printCategory(self):
        print(f"Name: {self.name} Code: {self.code} Number of products: {self.product}")
    
class Product():
    def __init__(self,name,code,category,price):
        self.name=name
        self.code=code
        self.category=category
        self.price=price
        category.product += 1

    #sort the list in ascending order
    def sort_ascend():
        for i in range(len(prod_list)):
            for j in range(len(prod_list)):
                #swap elements
                if (prod_list[i].price < prod_list[j].price):
                    temp = prod_list[i]
                    prod_list[i]=prod_list[j]
                    prod_list[j]=temp

        print("Sorting the Products accroding to their price(low to high)")
        for i in prod_list:
            print(f"Name:{i.name} Code:{i.code} Category: {i.category.name} Price: {i.price}")
    
    #sort the list in descending order
    def sort_descend():

        for i in range(len(prod_list)):
            for j in range(len(prod_list)):
                #swap elements
                if (prod_list[i].price > prod_list[j].price):
                    temp = prod_list[i]
                    prod_list[i]=prod_list[j]
                    prod_list[j]=temp

        print("Sorting the Products accroding to their price(high to low):\n")
        for i in prod_list:
            print(f"Name:{i.name} Code:{i.code} Category: {i.category.name} Price: {i.price}")
    
    #search product using its code
    def search_prod():
        print("Search the product")
        product_found = False
        searchCode = input("Enter Code of the product to be searched:")
        for i in prod_list:
            if i.code == searchCode:
                print("product is available")
                print(f"Name: {i.name} Code: {i.code} Category: {i.category.name} Price: {i.price}")
                product_found = True
                break

        if not product_found:
            print("Sorry! Product Not Found.")

   
    
#creating category objects
c1=Category("Toys","AA1")
c2=Category("Clothes","AA2")
c3=Category("Footwear","AA3")
categories = [c1,c2,c3]

#creating product objects and appending into list
prod_list=[]
prod_list.append(Product("T-shirt","AA21",c2,250))
prod_list.append(Product("Car","AA11",c1,160))
prod_list.append(Product("Jeans","AA22",c2,280))
prod_list.append(Product("Shoes","AA31",c3,450))
prod_list.append(Product("Crocs","AA32",c3,500))
prod_list.append(Product("Truck","AA12",c1,190))
prod_list.append(Product("Piano","AA13",c1,350))
prod_list.append(Product("Shorts","AA23",c2,300))
prod_list.append(Product("Shirt","AA24",c2,320))
prod_list.append(Product("Crop top","AA25",c2,400))

#printing category information
print("Category information:\n")
print("Category 1:")
c1.printCategory()
print("Category 2:")
c2.printCategory()
print("Category 3:")
c3.printCategory()
print("\n")

#sort products in ascending order
Product.sort_ascend()
print("\n")

#sort products in descending order
Product.sort_descend()
print("\n")

#search product
Product.search_prod()
