"""
Write a  Python class Restaurant with attributes like menu_items, book_table, and customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
Perform the following tasks now:
Now add items to the menu.
Make table reservations.
Take customer orders.
Print the menu.
Print table reservations.
Print customer orders.
Note: Use dictionaries and lists to store the data.
"""

class Restaurant:
    def __init__(self) -> None:
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = {}
        
    def add_item_to_menu(self, new_menu_item, price):
        self.menu_items[new_menu_item] = price
        print(self.menu_items)

    
    def book_tables(self, table_number):
        self.book_table.append(table_number)
        # print('Table Reservations: ')
        print('Table: ', table_number)
                
    def customer_order(self, table_number, order:list):
        for dish in order:
            if dish not in self.menu_items:
                print(f'{dish} is not available for {table_number}.')
                order.remove(dish)
        self.customer_orders[f'Table {table_number}'] = order
        print(f'Table {table_number}: ', order)
    
    
restaurant = Restaurant()

print('Restaurant Menu:')
add_item_1 = 'chicken'
price_1 = 9.99
price_2 = 8
add_item_2 = 'beef'
restaurant.add_item_to_menu(add_item_1, price_1)
restaurant.add_item_to_menu(add_item_2, price_2)


print('Table Reservations: ')
restaurant.book_tables(1)
restaurant.book_tables(2)



print('Customer Orders: ')
restaurant.customer_order(1, ['chicken', 'beef'])
restaurant.customer_order(1, ['chicken', 'veggies'])
