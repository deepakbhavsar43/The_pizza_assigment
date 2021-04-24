class pizza:
    size, cheeseTopping, pepperoniTopping, mushroomTopping = 0, 0, 0, 0
    def __init__(self, size, cheeseTopping, pepperoniTopping, mushroomTopping):
        self.size = size
        self.cheeseTopping = cheeseTopping
        self.pepperoniTopping = pepperoniTopping
        self.mushroomTopping = mushroomTopping

    def getSize(self):
        print(self.size)

    def getCheeseTopping(self):
        print(self.cheeseTopping)

    def getPepperoniTopping(self):
        print(self. pepperoniTopping)

    def getMushroomTopping(self):
        print(self.mushroomTopping)

    def setSize(self, size):
        self.size = size

    def setCheeseTopping(self, cheeseTopping):
        self.cheeseTopping = cheeseTopping

    def setPepproniTopping(self, pepperoniTopping):
        self.pepperoniTopping = pepperoniTopping

    def setMushroomTopping(self, mushroomTopping):
        self.mushroomTopping = mushroomTopping

    def calcCost(self):
        total_toppings = self.cheeseTopping + self.pepperoniTopping + self.mushroomTopping
        cost = 0
        if self.size.lower() == "small":
            cost = 10 + (2 * total_toppings)

        if self.size.lower() == "medium":
            cost = 12 + (2 * total_toppings)

        if self.size.lower() == "large":
            cost = 14 + (2 * total_toppings)
        
        return cost.__str__()

    def pizza_ordered(self):
        size = self.size.__str__()
        cheeseTopping = self.cheeseTopping.__str__()
        pepperoniTopping = self.pepperoniTopping.__str__()
        mushroomTopping = self.mushroomTopping.__str__()
        return size, cheeseTopping, pepperoniTopping, mushroomTopping

if __name__ == "__main__":
    pz = pizza("large", 1, 2, 1)
    cost = pz.calcCost()
    print("pizza bill : ", cost)
    size, cheeseTopping, pepprtoniTopping, mushroomTopping = pz.pizza_ordered()
    print(f"pizza ordered :\n\tSize: {size}\n\tcheeseTopping: {cheeseTopping}\n\tpepprtoniTopping: {pepprtoniTopping}\n\tmushroomTopping: {mushroomTopping}")
           