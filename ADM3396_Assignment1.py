class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user = {"username": self.username, "password": self.password}
    
    def setPassword(self, newPassword):
        self.password = newPassword
        self.user["password"] = newPassword
    
    def setUsername(self, newUsername):
        self.username = newUsername
        self.user["username"] = newUsername

    def getUser(self):
        print(self.user)

class Food:
    def __init__(self, item, price, food_type, diet, cuisine, review):
        self.food = {
            "item": item, 
            "price": price, 
            "type": food_type, 
            "diet": diet, 
            "cuisine": cuisine, 
            "review": review
        }
    
    def setPrice(self, newPrice):
        price = newPrice
        self.food["price"] = newPrice
    
    def setReview(self, newReview):
        review = newReview
        self.food["review"] = newReview

    def getFood(self):
        return self.food

    def getFoodItem(self):
        return self.food["item"]

class Menu:
    def __init__(self):
        self.menu = {}
    
    def addFood(self, food):
        self.menu[food.getFoodItem()] = food.getFood()

    def removeFood(self, foodItem):
        if foodItem in self.menu:
            del self.menu[foodItem]

    def showMenu(self):
        for item, details in self.menu.items():
            print(f"{item}: {details}")
    
    def getMenu(self):
        print(self.menu)
   

x = User("hi", "bye")
x.getUser()
x.setUsername("ebebe")
x.getUser()

food1 = Food("Pizza", 10, "Dinner", "Non-Vegetarian", "Italian", 5)
food2 = Food("Salad", 5, "Lunch", "Vegetarian", "Various", 4)

menu = Menu()
menu.addFood(food1)
menu.addFood(food2)
menu.showMenu()
menu.getMenu()