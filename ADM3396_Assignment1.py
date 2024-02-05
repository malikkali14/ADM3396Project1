class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self, username, password):
        return self.username == username and self.password == password

    def getUser(self):
        return {"username": self.username, "password": self.password}

class Food:
    def __init__(self, item, price, food_type, diet, cuisine, review, available=True):
        self.food = {
            "item": item, 
            "price": price, 
            "type": food_type, 
            "diet": diet, 
            "cuisine": cuisine, 
            "review": review,
            "available": available
        }
    
    def setPrice(self, newPrice):
        self.food["price"] = newPrice
    
    def setReview(self, newReview):
        self.food["review"] = newReview

    def setAvailability(self, availability):
        self.food["available"] = availability

    def getFood(self):
        return self.food

class Menu:
    def __init__(self):
        self.menu = {}
    
    def addFood(self, food):
        self.menu[food.getFood()["item"]] = food.getFood()

    def removeFood(self, foodItem):
        if foodItem in self.menu:
            del self.menu[foodItem]

    def showMenu(self):
        print("Menu:")
        for item, details in self.menu.items():
            if details["available"]:
                print(f"{item}: {details}")

    def searchMenu(self, searchTerm):
        searchResults = {item: details for item, details in self.menu.items() if searchTerm.lower() in item.lower() and details["available"]}
        return searchResults

def main():
    # Create a user and attempt to login
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = User(username, password)
    
    if user.login(username, password):
        print(f"Welcome {username}!")
    else:
        print("Invalid username or password. Please try again.")
        return
    
    # Initialize menu and add food items
    menu = Menu()
    menu.addFood(Food("Pizza", 10, "Dinner", "Non-Vegetarian", "Italian", 5))
    menu.addFood(Food("Salad", 5, "Lunch", "Vegetarian", "Various", 4))
    
    # Show available menu items
    menu.showMenu()
    
    # Perform a search on the menu
    searchTerm = input("Enter a food item to search for: ")
    searchResults = menu.searchMenu(searchTerm)
    if searchResults:
        print("Search results:")
        for item, details in searchResults.items():
            print(f"{item}: {details}")
    else:
        print("No available items found with that name.")
        
    # Example of updating an item's availability
    food_to_update = input("Enter a food item to update availability: ")
    if food_to_update in menu.menu:
        new_availability = input(f"Is the {food_to_update} available? (yes/no): ").lower() == 'yes'
        menu.menu[food_to_update]["available"] = new_availability
        print(f"{food_to_update} availability updated to {new_availability}.")
    else:
        print(f"{food_to_update} not found in the menu.")

    # Show updated menu
    menu.showMenu()

if __name__ == "__main__":
    main()