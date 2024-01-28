class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.user = {}
        self.user["username"] = self.username
        self.user["password"] = self.password
    
    def setPassword(self, newPassword):
        self.password = newPassword
        self.user["password"] = newPassword
    
    def setUsername(self, newUsername):
        self.username = newUsername
        self.user["username"] = newUsername

    def getUser(self):
        print(self.user)

class Food:
    def __init__(self, item, price, type, diet, cuisine, review):
        self.food = {}
        food["item"] = item
        food["food"] = price
        food["type"] = type
        food["food"] = diet
        food["cuisine"] = cuisine 
        food["review"] = review 
    
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
    def __init__(food):
        menu = {}
        menu[food.getFood()] = food.getFood()
    
    def getMenu(self):




x = User("hi", "bye")
x.getUser()
x.setUsername("ebebe")
x.getUser()