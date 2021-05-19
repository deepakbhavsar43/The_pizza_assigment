class DeluxePizza:
    size, cheeseTopping, pepperoniTopping, mushroomTopping = 0, 0, 0, 0
    stuffedWithCheese = 0
    veggieTopping = 0
    numberOfPizzas = 0
    
    def __init__(self, size, cheeseTopping, pepperoniTopping, mushroomTopping, stuffedWithCheese, veggieTopping):
        self.size = size
        self.cheeseTopping = cheeseTopping
        self.pepperoniTopping = pepperoniTopping
        self.mushroomTopping = mushroomTopping
        self.numberOfPizzas += 1
        self.stuffedWithCheese = 0
        self.veggieTopping = 0

    def getSize(self):
        print(self.size)

    def getCheeseTopping(self):
        print(self.cheeseTopping)

    def getPepperoniTopping(self):
        print(self.pepperoniTopping)

    def getMushroomTopping(self):
        print(self.mushroomTopping)

    def getStuffedWithCheese(self):
        print(self.stuffedWithCheese)

    def getVeggieTopping(self):
        print(self.veggieTopping)

    def getNumberOfPizzas(self):
        print(self.numberOfPizzas)    
 
    def setSize(self, size):
        self.size = size

    def setCheeseTopping(self, cheeseTopping):
        self.cheeseTopping = cheeseTopping

    def setPepproniTopping(self, pepperoniTopping):
        self.pepperoniTopping = pepperoniTopping

    def setMushroomTopping(self, mushroomTopping):
        self.mushroomTopping = mushroomTopping

    def setStuffedWithCheese(self, stuffedWithCheese):
        self.stuffedWithCheese = stuffedWithCheese

    def setVeggieTopping(self, veggieTopping):
        self.veggieTopping = veggieTopping

    def calcCost(self):
        total_toppings = self.cheeseTopping + self.pepperoniTopping + self.mushroomTopping
        cost = 0
        if self.size.lower() == "small":
            cost = 10 + (2 * total_toppings) + (3 * self.veggieTopping)
            print("outside stuffed cheese", self.stuffedWithCheese)
            if self.stuffedWithCheese == 1:
                print("inside stuffed cheese", self.stuffedWithCheese)
                cost = cost + 2
            
        if self.size.lower() == "medium":
            cost = 12 + (2 * total_toppings) + (3 * self.veggieTopping)
            if self.stuffedWithCheese == 1:
                cost = cost + 4
            
        if self.size.lower() == "large":
            cost = 14 + (2 * total_toppings) + (3 * self.veggieTopping)
            if self.stuffedWithCheese == 1:
                cost = cost + 6
            
        return cost.__str__()

    def pizza_ordered(self):
        size = self.size.__str__()
        stuffedWithCheese = self.stuffedWithCheese.__str__()
        cheeseTopping = self.cheeseTopping.__str__()
        pepperoniTopping = self.pepperoniTopping.__str__()
        mushroomTopping = self.mushroomTopping.__str__()
        veggieTopping = self.veggieTopping.__str__()
        return size, stuffedWithCheese, cheeseTopping, pepperoniTopping, mushroomTopping, veggieTopping


def menu():
    print("""
    Papa Jhon, what do you want to do?
        1. Enter a new pizza order
        2. Change information of a specific order
        3. Display details for all pizzas of a specific size
        4. Statistics on today's pizzas
        5. Quit
    """)

def changeMenu():
    print("""
    Papa John, what would you like to change?
    \t1.	Size
    \t2.	Cheese filled or not (1 for True or 0 for False)
    \t3.	Number of cheese toppings
    \t4.	Number of pepperoni toppings
    \t5.	Number of mushroom toppings
    \t6.	Number of vegetable toppings
    \t7.	Quit 
    """)

def displayPizza(pizzaNumber, pizza):
    print(f"""Pizza  {pizzaNumber} 
    \tPizza size: {pizza.size}
    \tCheese filled dough: {pizza.stuffedWithCheese}
    \tNumber of cheese toppings: {pizza.cheeseTopping}
    \tNumber of pepperoni toppings: {pizza.pepperoniTopping}
    \tNumber of mushroom toppings: {pizza.mushroomTopping}
    \tNumber of vegetable toppings: {pizza.veggieTopping}
    \tPrice: ${pizza.calcCost()}
    """)

def pizzasOfSize(ofsize):
    count = 0
    for pizza in todaysPizzas:
        if pizza.size == ofSize:
            print(f"List of {ofSize} pizza sold today.")
            displayPizza(todaysPizzas.index(pizza), pizza)
            count += 1
    print(f"Our chef, made {count} {ofSize} pizza today!")

def validatePassword(password):
    if password == "deluxepizza":
        return True
    else:
        return False

def cheaperThan(priceThreshold):
    for pizza in todaysPizzas:
        price = pizza.calcCost()
        if price < priceThreshold:
            print(f"Pizza {todaysPizzas.index(pizza)} > price is {price}.")

def lowestPrice():
    pizzaCost = []
    for pizza in todaysPizzas:
        price = pizza.calcCost()
        pizzaCost.append(price)
    minCost = min(pizzaCost)
    minCostIndex = pizzaCost.index(minCost)
    displayPizza(pizzaCost.index(minCost), todaysPizzas[minCostIndex])

def highestPrice():
    pizzaCost = []
    for pizza in todaysPizzas:
        price = pizza.calcCost()
        pizzaCost.append(price)
    maxCost = max(pizzaCost)
    maxCostIndex = pizzaCost.index(maxCost)
    displayPizza(pizzaCost.index(maxCost), todaysPizzas[maxCostIndex])

def numberOfPizzasOfSize(ofSize):
    count = 0
    for pizza in todaysPizzas:
        if pizza.size == ofSize:
            count += 1
    print(f"Number of pizza of {ofSize} is {count}.")



if __name__ == "__main__":
    print("Welcome to Papa Jhon Pizzeria")
    pizzaInStock = 5
    print(f"Number of maximum pizza can be prepared: {pizzaInStock}.")
    todaysPizzas = []
    Flag = True
    while Flag:
        menu()
        option = int(input("Please enter your choice > "))
        if option == 1:
            i = 1
            password = input("enter password: ")
            while i<=3 and validatePassword(password) == False:
                if i != 3:
                    i = i + 1
                    password = input("enter valid password > ") 
                else:
                    break
            if i == 3 and validatePassword(password) == False:
                continue

            order = int(input("Number of pizza to make > "))
            if order <= pizzaInStock and len(todaysPizzas) < pizzaInStock:
                for i in range(order):
                    temp = []
                    print(f"\nPizza {i}")
                    size = input("Enter size of pizza small, medium or large > ")
                    cheeseTop = int(input("Number of cheese topping to add > "))
                    pepTop = int(input("Number of pepperoni topping to add > "))
                    mushTop = int(input("Number of mushroom topping to add > "))
                    stuffCheese = input("Pizza base with stuffed cheese > ")
                    veggieTop = int(input("Number of veggie topping to add > "))
                    pizza = DeluxePizza(
                        size,
                        cheeseTop,
                        pepTop,
                        mushTop,
                        stuffCheese,
                        veggieTop                      
                    )
                    todaysPizzas.append(pizza)
            else:
                print(f"\nNumber of pizza we can make: {pizzaInStock}")
        elif option == 2:
            i = 1
            password = input("enter password: ")
            while i<=3 and validatePassword(password) == False:
                if i != 3:
                    i = i + 1
                    password = input("enter valid password > ") 
                else:
                    break
            if i == 3 and validatePassword(password) == False:
                continue

            pizzaToUpdate = int(input("Which pizza you want to update > "))
            if 0 <= pizzaToUpdate and pizzaToUpdate <= len(todaysPizzas):
                pizzaObject = todaysPizzas[pizzaToUpdate]
                displayPizza(pizzaToUpdate, pizzaObject)

                while True:
                    changeMenu()
                    chOption = int(input("Enter choice > "))

                    if chOption == 1:
                        size = input("Enter size of pizza small, medium or large > ")
                        pizzaObject.size = size
                    elif chOption == 2:
                        stuffedWithCheese = input("Pizza base with stuffed cheese > ")
                        pizzaObject.setStuffedWithCheese(stuffedWithCheese)
                    elif chOption == 3:
                        cheeseTopping = int(input("Number of cheese topping to add > "))
                        pizzaObject.setCheeseTopping(cheeseTopping)
                    elif chOption == 4:
                        pepperoniTopping = int(input("Number of pepperoni topping to add > "))
                        pizzaObject.pepperoniTopping = pepperoniTopping
                    elif chOption == 5:
                        mushroomTopping = int(input("Number of mushroom topping to add > "))
                        pizzaObject.mushroomTopping = mushroomTopping
                    elif chOption == 6:
                        veggieTopping = int(input("Number of veggie topping to add > "))
                        pizzaObject.veggieTopping = veggieTopping
                    elif chOption == 7:
                        break
                    else:
                        print("\nEnter valid choice.\n")
                        continue
                    displayPizza(pizzaToUpdate, pizzaObject)
            else:
                print("***Given pizza number not found***")
                print("Do you want to enter another pizza? Y or any to skip")
                choice = input()
                if choice.lower() == "n":
                    continue
        
        elif option == 3:
            ofSize = input("Enter the size of the pizza to search for > ")
            pizzasOfSize(ofSize)
        elif option == 4:
            while True:
                print("""
                Papa John, what information would you like?
                1.	Cost and details of cheapest pizza
                2.	Cost and details of most costly pizza
                3.	Number of pizzas sold today
                4.	Number of pizzas of a specific size
                5.	Average cost of pizzas
                6.	Quit
                """)
                infoChoice = int(input("Enter choice > "))
                if infoChoice  == 1:
                    lowestPrice()
                elif infoChoice == 2:
                    highestPrice()
                elif infoChoice == 3:
                    print(f"Total {len(todaysPizzas)} pizza sold today.")
                elif infoChoice == 4:
                    pizzaSizeToSearch = input("Enter size of the pizza > ")
                    count = 0
                    for obj in todaysPizzas:
                        if obj.size == pizzaSizeToSearch:
                            count += 1
                    print(f"Total count of {pizzaSizeToSearch} pizza is {count}.")
                elif infoChoice == 5:
                    sum , length = 0, len(todaysPizzas)
                    for obj in todaysPizzas:
                        sum = sum + int(obj.calcCost())
                    averageCost = sum/length
                    print(f"Average cost of pizza is {averageCost}")
                elif infoChoice == 6:
                    break
                else:
                    print("Enter a valid choice > ")
        elif option == 5:
            print("***shuting down***")
            break 
        else:
            print("Enter valid option.")  