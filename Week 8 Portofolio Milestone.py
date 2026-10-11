#Week 4 Portofolio Milestone
#CSC500-1
#Michael Ferguson
#9/18/26

#Step 1 Build the ItemsToPurchase class:
class ItemsToPurchase:
    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0):
        self.item_name = str(item_name)
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

#Step 2: Main Program Implementation:
item1_name = input("Enter the item name: ")
item1_price = float(input("Enter the item price: "))
item1_quantity = int(input("Enter the item quantity: "))
total_cost1 = item1_price * item1_quantity
print(item1_name, item1_price, item1_quantity, total_cost1)
item2_name = input("Enter the item name: ")
item2_price = float(input("Enter the item price: "))
item2_quantity = int(input("Enter the item quantity: "))
total_cost2 = item2_price * item2_quantity
print(item2_name, item2_price, item2_quantity, total_cost2)

#Step 3: Output the total cost of the two items purchased.
total_cost = total_cost1 + total_cost2
print(item1_name, item1_quantity, "@", item1_price, "=", total_cost1)
print(item2_name, item2_quantity, "@", item2_price, "=", total_cost2)
print("Total Cost: $", total_cost)

#Week 6 Portfolio Milestone
#CSC500-1
#Michael Ferguson
#10/10/2026

#Step 4 Build Shopping Cart Class
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for index, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                del self.cart_items[index]
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_name, new_quantity):
        for item in self.cart_items:
            if item.item_name == item_name:
                item.item_quantity = new_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if not self.cart_items:
            print("SHOPPING CART EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
        print(f"\nTotal: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                description = getattr(item, "item_description", "No description")
                print(f"{item.item_name}: {description}")


#Step 5 Build The User Interface
def print_menu(shopping_cart):
    while True:
        menu_text = (
            "\nMENU\n"
            "a - Add item to cart\n"
            "r - Remove item from cart\n"
            "c - Change item quantity\n"
            "i - Output items' descriptions\n"
            "o - Output shopping cart\n"
            "q - Quit\n"
        )
        print(menu_text)
        user_choice = input("Choose an option:\n").strip().lower()

        if user_choice == 'a':
            print("Add item")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            item = ItemsToPurchase(name, price, quantity)
            item.item_description = description
            shopping_cart.add_item(item)
        elif user_choice == 'r':
            print("Remove item")
            name = input("Enter name of item to remove:\n")
            shopping_cart.remove_item(name)
            print("Returning to Menu")
        elif user_choice == 'c':
            print("Change item quantity")
            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            shopping_cart.modify_item(name, quantity)
        elif user_choice == 'i':
            print("Output items' Descriptions")
            shopping_cart.print_descriptions()
            print("Finished printing descriptions. Returning to menu.")
        elif user_choice == 'o':
            print("Output Shopping Cart")
            shopping_cart.print_total()
        elif user_choice == 'q':
            break
        else:
            print("Invalid option. Please try again")


if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")
    shopping_cart = ShoppingCart(customer_name, current_date)
    print_menu(shopping_cart)
