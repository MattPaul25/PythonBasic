#running basic basic python program
import random



class classDocument(object):
    #this is a class (like .net all classes inherit from object)
    def __str__(self):
        #this is an auto-running method
        return "this is a document"

class ShoppingCart:
    def __init__(self):
        self.items = []

    def addItem(self, name, price):
        item = (name, price)
        self.items.append( item )

    def __iter__(self):
        return self.items.__iter__()

    @property #converts method into a setter property
    def getTotal(self):
        total = 0
        for item in self.items:
            total += item[1];
        return total

def runShopCartClass():
    cart = ShoppingCart()
    cart.addItem('car', 20000)
    cart.addItem('tv', 2000)
    for i in cart.items:
        print (i)
    myTotal = cart.getTotal
    print(format(myTotal))

#public IEnumerable<string> GetDays(){}
def get_days():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days

def get_random_weather_report():
    weather = ['sunny', 'rainy', 'hot', 'lovely']
    day = weather[random.randint(0, len(weather) - 1)]
    return day

def main():
    days = get_days()
    for d in days:
        r = get_random_weather_report()
        print("Weather on {0} is {1}. ".format(d, r))
    print("To show scope of R variable outside the loop: " + r)
    print("variables in loops are scoped to the method outside the loop...")
    
def runClass():
    doc = classDocument()
    print(doc)

if __name__ == "__main__":
    main()
    runClass()
    runShopCartClass()




