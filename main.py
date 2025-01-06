import json
from tabulate import tabulate

class InventoryManager:
    def __init__(self, data_file="inventory.json"):
        self.data_file = data_file
        try:
            with open(self.data_file, "r") as file:
                self.inventory = json.load(file)
        except FileNotFoundError:
            self.inventory = []

    def save_data(self):
        with open(self.data_file, "w") as file:
            json.dump(self.inventory, file, indent=4)

    def generate_id(self):
        return len(self.inventory) + 1

    def add_product(self):
        name = input("Enter product name: ")
        category = input("Enter product category: ")
        try:
            quantity = int(input("Enter quantity in stock: "))
            price = float(input("Enter product price: "))
        except ValueError:
            print("Invalid input. Quantity must be an integer and price must be a number.")
            return

        product = {
            "id": self.generate_id(),
            "name": name,
            "category": category,
            "quantity": quantity,
            "price": price
        }
        self.inventory.append(product)
        self.save_data()
        print("Product added successfully!")

    def list_products(self):
        if not self.inventory:
            print("No products in inventory.")
            return

        headers = ["ID", "Name", "Category", "Quantity", "Price"]
        table = [
            [product["id"], product["name"], product["category"], product["quantity"], product["price"]]
            for product in self.inventory
        ]
        print(tabulate(table, headers=headers, tablefmt="grid"))
    import json
from tabulate import tabulate

class InventoryManager:
    def __init__(self, data_file="inventory.json"):
        self.data_file = data_file
        try:
            with open(self.data_file, "r") as file:
                self.inventory = json.load(file)
        except FileNotFoundError:
            self.inventory = []

    def save_data(self):
        with open(self.data_file, "w") as file:
            json.dump(self.inventory, file, indent=4)

    def generate_id(self):
        return len(self.inventory) + 1

    def add_product(self):
        name = input("Enter product name: ")
        category = input("Enter product category: ")
        try:
            quantity = int(input("Enter quantity in stock: "))
            price = float(input("Enter product price: "))
        except ValueError:
            print("Invalid input. Quantity must be an integer and price must be a number.")
            return

        product = {
            "id": self.generate_id(),
            "name": name,
            "category": category,
            "quantity": quantity,
            "price": price
        }
        self.inventory.append(product)
        self.save_data()
        print("Product added successfully!")

    def list_products(self):
        if not self.inventory:
            print("No products in inventory.")
            return

        headers = ["ID", "Name", "Category", "Quantity", "Price"]
        table = [
            [product["id"], product["name"], product["category"], product["quantity"], product["price"]]
            for product in self.inventory
        ]
        print(tabulate(table, headers=headers, tablefmt="grid"))

    def update_product(self):
        while True:
            try:
                product_id = int(input("Enter the product ID to update: "))
            except ValueError:
                print("Invalid input. ID must be a number.")
                continue

            product = next((p for p in self.inventory if p["id"] == product_id), None)
            if not product:
                choice = input("Product not found. Try again? (yes/no): ").strip().lower()
                if choice == "no":
                    return
            else:
                break

        print("Leave the field blank to keep the current value.")
        name = input(f"Enter new name ({product['name']}): ") or product["name"]
        category = input(f"Enter new category ({product['category']}): ") or product["category"]
        try:
            quantity = input(f"Enter new quantity ({product['quantity']}): ")
            quantity = int(quantity) if quantity else product["quantity"]

            price = input(f"Enter new price ({product['price']}): ")
            price = float(price) if price else product["price"]
        except ValueError:
            print("Invalid input. Quantity must be an integer and price must be a number.")
            return

        product.update({"name": name, "category": category, "quantity": quantity, "price": price})
        self.save_data()
        print("Product updated successfully!")

    def delete_product(self):
        try:
            product_id = int(input("Enter the product ID to delete: "))
        except ValueError:
            print("Invalid input. ID must be a number.")
            return

        product = next((p for p in self.inventory if p["id"] == product_id), None)
        if not product:
            print("Product not found.")
            return

        confirm = input(f"Are you sure you want to delete {product['name']}? (yes/no): ").lower()
        if confirm == "yes":
            self.inventory.remove(product)
            self.save_data()
            print("Product deleted successfully!")
        else:
            print("Deletion canceled.")

    def search_product(self):
        search_term = input("Enter product ID or name to search: ").strip()
        try:
            search_id = int(search_term)
            products = [p for p in self.inventory if p["id"] == search_id]
        except ValueError:
            products = [p for p in self.inventory if search_term.lower() in p["name"].lower()]

        if not products:
            print("No products found.")
            return

        headers = ["ID", "Name", "Category", "Quantity", "Price"]
        table = [
            [product["id"], product["name"], product["category"], product["quantity"], product["price"]]
            for product in products
        ]
        print(tabulate(table, headers=headers, tablefmt="grid"))


def main():
    manager = InventoryManager()
    actions = {
        "1": manager.add_product,
        "2": manager.list_products,
        "3": manager.update_product,
        "4": manager.delete_product,
        "5": manager.search_product,
        "6": exit
    }

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. List Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Search Product")
        print("6. Exit")
        choice = input("Select an option: ")

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
