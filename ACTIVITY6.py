class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: ₱{self.price:.2f}"

class ItemManager:
    def __init__(self):
        self.items = {}
        self.sanrio_characters = ["Hello Kitty", "My Melody", "Cinnamoroll", "Kuromi", "Pompompurin", "Little Twin Stars", "Badtz-Maru"]
    
    def add_item(self):
        try:
            item_id = input("Enter item ID: ")
            if item_id in self.items:
                raise ValueError("Item ID already exists!")
            print("Choose a Sanrio character:")
            for i, char in enumerate(self.sanrio_characters, 1):
                print(f"{i}. {char}")
            choice = int(input("Enter choice: "))
            if choice < 1 or choice > len(self.sanrio_characters):
                raise ValueError("Invalid choice!")
            name = self.sanrio_characters[choice - 1]
            description = input("Enter description: ")
            price = float(input("Enter price: "))
            if price < 0:
                raise ValueError("Price cannot be negative!")
            
            self.items[item_id] = Item(item_id, name, description, price)
            print("Item added successfully!\n")
        except ValueError as e:
            print(f"Error: {e}\n")
    
    def view_items(self):
        if not self.items:
            print("No items available.\n")
        else:
            for item in self.items.values():
                print(item)
            print()
    
    def update_item(self):
        try:
            item_id = input("Enter item ID to update: ")
            if item_id not in self.items:
                raise ValueError("Item not found!")
            description = input("Enter new description: ")
            price = float(input("Enter new price: "))
            if price < 0:
                raise ValueError("Price cannot be negative!")
            
            self.items[item_id].description = description
            self.items[item_id].price = price
            print("Item updated successfully!\n")
        except ValueError as e:
            print(f"Error: {e}\n")
    
    def delete_item(self):
        try:
            item_id = input("Enter item ID to delete: ")
            if item_id not in self.items:
                raise ValueError("Item not found!")
            
            del self.items[item_id]
            print("Item deleted successfully!\n")
        except ValueError as e:
            print(f"Error: {e}\n")

    def run(self):
        while True:
            print("==SANRIO MERCHANTS ONLINE STORE==")
            print("1. Add Sanrio character\n2. View Sanrio merch\n3. Update Sanrio merch\n4. Delete Sanrio merch\n5. Exit")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.add_item()
                elif choice == 2:
                    self.view_items()
                elif choice == 3:
                    self.update_item()
                elif choice == 4:
                    self.delete_item()
                elif choice == 5:
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice!\n")
            except ValueError:
                print("Please enter a valid number!\n")

if __name__ == "__main__":
    manager = ItemManager()
    manager.run()
