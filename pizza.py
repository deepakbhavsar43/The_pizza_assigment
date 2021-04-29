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
            if self.stuffedWithCheese == 1:
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
                    size = input("Enter size of pizza small, medium or large > "),
                    cheeseTop = int(input("Number of cheese topping to add > ")),
                    pepTop = int(input("Number of pepperoni topping to add > ")),
                    mushTop = int(input("Number of mushroom topping to add > ")),
                    stuffCheese = input("Pizza base with stuffed cheese > "),
                    veggieTop = int(input("Number of veggie topping to add > "))
                    pizza = DeluxePizza(
                        size,
                        cheeseTop,
                        pepTop,
                        mushTop,
                        stuffCheese,
                        veggieTop                      
                    )
                    cost = pizza.calcCost()
                    temp.extend([
                        size,
                        cheeseTop,
                        pepTop,
                        mushTop,
                        stuffCheese,
                        veggieTop,
                        Cost
                    ])
                    todaysPizzas.append(temp)
            else:
                print(f"Number of pizza we can make: {pizzaInStock}")

        if option == 2:
            password = input("enter password: ")
            i = 2
            while i>0 and validatePassword(password) == False:
                password = input("enter valid password > ") 
                i = i - 1

            pizzaToUpdate = int(input("Which pizza you want to update > "))
            if 0 <= pizzaToUpdate and pizzaToUpdate <= len(todaysPizzas):
                pizza = todaysPizzas[pizzaToUpdate]
                print(f"""
                    \nPizza  # 
                    \tPizza size: {pizza[0]}
                    \tCheese filled dough: {pizza[1]}
                    \tNumber of cheese toppings: {pizza[2]}
                    \tNumber of pepperoni toppings: {pizza[3]}
                    \tNumber of mushroom toppings: {pizza[4]}
                    \tNumber of vegetable toppings: {pizza[5]}
                    \tPrice: ${pizza[6]}
                """)
            else:
                print("***Given pizza number not found***")
                print("Do you want to enter another pizza? Y or any to skip")
                choice = input()
                if choice.lower() == "n":
                    continue

        if option == 5:
            break