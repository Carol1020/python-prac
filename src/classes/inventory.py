"""
Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and methods like add_item, update_item, and check_item_details.
Use a dictionary to store the item details, where the key is the item_id and the value is a dictionary containing the item_name, stock_count, and price.
"""
class Inventory:
    def __init__(self):
        # self.item_id = item_id
        # self.item_name = item_name
        # self.stock_count = stock_count
        # self.price = price
        self.inventory_dict = {}
        
    def add_item(self, item_id, item_name, stock_count, price):
        self.inventory_dict[item_id] = {
            "item_name": item_name, 
            "stock_count": stock_count, 
            "price": price
        }
        print(f'item_id: {item_id}')
        print(f'item_name: {item_name}')
        print(f'stock_count: {stock_count}')
        print(f'price: {price}')
        
    def update_item(self, item_id, item_name, stock_count, price):
        if item_id in self.inventory_dict:
            self.inventory_dict[item_id]['item_name'] = item_name
            self.inventory_dict[item_id]['stock_count'] = stock_count
            self.inventory_dict[item_id]['price'] = price
            print(f'item_id: {item_id}')
            print(f'item_name: {item_name}')
            print(f'stock_count: {stock_count}')
            print(f'price: {price}')
        else:
            self.add_item(self, item_id, item_name, stock_count, price)
    
    def check_item_details(self, item_id):
        if item_id in self.inventory_dict:
            print(f'item_id: {item_id}')
            print(f'item_name: {self.inventory_dict[item_id]["item_name"]} ')
            print(f'item_name: {self.inventory_dict[item_id]["stock_count"]} ')
            print(f'item_name: {self.inventory_dict[item_id]["price"]} ')

        else:
            print('Item does not exist.')
            
            

if __name__ == "__main__": 
    
    inventory = Inventory()

    inventory.add_item("I001", "Laptop", 100, 500.00)
    inventory.add_item("I002", "Mobile", 110, 450.00)
    inventory.add_item("I003", "Desktop", 120, 500.00)
    inventory.add_item("I004", "Tablet", 90, 550.00)
    print("Item Details:")
    print(inventory.check_item_details("I001"))
    print(inventory.check_item_details("I002"))
    print(inventory.check_item_details("I003"))
    print(inventory.check_item_details("I004"))
    print("\nUpdate the price of item code - 'I001':")
    inventory.update_item("I001", "Laptop", 100, 505.00)
    print(inventory.check_item_details("I001"))
    print("\nUpdate the stock of item code - 'I003':")
    inventory.update_item("I003", "Microphone", 115, 500.00)
    print(inventory.check_item_details("I003"))
    
    