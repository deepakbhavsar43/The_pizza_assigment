class DeluxePizza:
    size, cheeseTopping, pepperoniTopping, mushroomTopping = 0, 0, 0, 0
    stuffedWithCheese = False
    veggieTopping = 0
    numberOfPizzas = 0
    
    def __init__(self, size, cheeseTopping, pepperoniTopping, mushroomTopping, stuffedWithCheese = 0, veggieTopping = 0):
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
            print(">> >> >>stuffedWithCheese", self.stuffedWithCheese)
            if self.stuffedWithCheese == 1:
                cost = cost + 2
            
        if self.size.lower() == "medium":
            cost = 12 + (2 * total_toppings) + (3 * self.veggieTopping)
            if self.stuffedWithCheese == True:
                cost = cost + 4
            
        if self.size.lower() == "large":
            cost = 14 + (2 * total_toppings) + (3 * self.veggieTopping)
            if self.stuffedWithCheese == True:
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
    \t2.	Cheese filled or not
    \t3.	Number of cheese toppings
    \t4.	Number of pepperoni toppings
    \t5.	Number of mushroom toppings
    \t6.	Number of vegetable toppings
    \t7.	Quit 
    """)

def displayPizza(pizza):
    print(f"""
        \nPizza  # 
        \tPizza size: {pizza.size}
        \tCheese filled dough: {pizza.stuffedWithCheese}
        \tNumber of cheese toppings: {pizza.cheeseTopping}
        \tNumber of pepperoni toppings: {pizza.pepperoniTopping}
        \tNumber of mushroom toppings: {pizza.mushroomTopping}
        \tNumber of vegetable toppings: {pizza.veggieTopping}
        \tPrice: ${pizza.calcCost()}
    """)

def pizzasOfSize(pizza, ofsize):
    if pizza.size == ofSize:
        displayPizza(pizza)
    else:
        print(f"No pizza ordered of size {ofSize}.")

def validatePassword(password):
    if password == "deluxepizza":
        return True
    else:
        return False


if __name__ == "__main__":
    # pz = DeluxePizza("large", 1, 2, 1)
    # cost = pz.calcCost()
    # print("pizza bill : ", cost)
    # size, stuffedWithCheese, cheeseTopping, pepprtoniTopping, mushroomTopping, veggieTopping = pz.pizza_ordered()
    # print(f"pizza #\n\tPizza size: {size}\n\tCheese filled dough: {stuffedWithCheese}\n\tNumber of cheese topping: {cheeseTopping}\n\tNumber of pepperoni topping: {pepprtoniTopping}\n\tNumber of mushroom topping: {mushroomTopping}\n\tNumber of vegetable topping: {veggieTopping}")
    print("Welcome to Papa Jhon Pizzeria")
    pizzaInStock = 5
    print(f"Number of maximum pizza can be prepared: {pizzaInStock}.")
    todaysPizzas = []
    # menu()
    Flag = True
    while Flag:
        menu()
        option = int(input("Please enter your choice > "))
        if option == 1:
            password = input("enter password: ")
            i = 2
            while i>0 and validatePassword(password) == False:
                password = input("enter valid password > ") 
                i = i - 1

            order = int(input("Number of pizza to make > "))
            if order <= pizzaInStock:
                for i in range(order):
                    temp = []
                    print(f"\nPizza {i+1}")
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
            password = input("enter password: ")
            i = 2
            while i>0 and validatePassword(password) == False:
                password = input("enter valid password > ") 
                i = i - 1

            pizzaToUpdate = int(input("Which pizza you want to update > "))
            if 0 <= pizzaToUpdate and pizzaToUpdate <= len(todaysPizzas):
                pizzaObject = todaysPizzas[pizzaToUpdate]
                displayPizza(pizzaObject)

                while True:
                    changeMenu()
                    chOption = int(input("Enter choice > "))

                    if chOption == 1:
                        size = input("Enter size of pizza small, medium or large > ")
                        pizzaObject.size = size
                    elif chOption == 2:
                        stuffedWithCheese = input("Pizza base with stuffed cheese > ")
                        pizzaObject.stuffedWithCheese = stuffedWithCheese
                    elif chOption == 3:
                        cheeseTopping = int(input("Number of cheese topping to add > "))
                        pizzaObject.cheeseTopping = cheeseTopping
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
                    displayPizza(pizzaObject)
            else:
                print("***Given pizza number not found***")
                print("Do you want to enter another pizza? Y or any to skip")
                choice = input()
                if choice.lower() == "n":
                    continue
        
        elif option == 3:
            ofSize = input("Enter the size of the pizza to search for > ")
            for obj in todaysPizzas:
                pizzasOfSize(obj, ofSize)
        elif option == 4:
            pass
        elif option == 5:
            break 
        else:
            print("Enter valid option.")  