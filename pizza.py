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
        print(self. pepperoniTopping)

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

if __name__ == "__main__":
    pz = DeluxePizza("large", 1, 2, 1)
    cost = pz.calcCost()
    print("pizza bill : ", cost)
    size, stuffedWithCheese, cheeseTopping, pepprtoniTopping, mushroomTopping, veggieTopping = pz.pizza_ordered()
    print(f"pizza #\n\tPizza size: {size}\n\tCheese filled dough: {stuffedWithCheese}\n\tNumber of cheese topping: {cheeseTopping}\n\tNumber of pepperoni topping: {pepprtoniTopping}\n\tNumber of mushroom topping: {mushroomTopping}\n\tNumber of vegetable topping: {veggieTopping}")
           