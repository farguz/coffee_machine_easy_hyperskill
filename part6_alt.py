class CoffeeMachine:
    # 'choosing an action', 'choosing a type of coffee', wait num of water/milk/beans/cups ?
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    # moved from body /
    def interprete_the_action(self, string):
        if string == 'buy':
            self.water, self.milk, self.beans, self.cups, self.money = \
                buy(self.water, self.milk, self.beans, self.cups, self.money)
        elif string == 'fill':
            self.water, self.milk, self.beans, self.cups = fill(self.water, self.milk, self.beans, self.cups)
        elif string == 'take':
            self.money = take(self.money)
        elif string == 'remaining':
            show_supplies(self.water, self.milk, self.beans, self.cups, self.money)
        else:
            exit()


def fill(water, milk, beans, cups):
    water += int(input('Write how many ml of water do you want to add: \n'))
    milk += int(input('Write how many ml of milk do you want to add: \n'))
    beans += int(input('Write how many grams of coffee beans do you want to add: \n'))
    cups += int(input('Write how many disposable cups of coffee do you want to add: \n'))
    return water, milk, beans, cups


def take(money):
    print('I gave you $' + str(money) + '\n')
    return 0


def buy(water, milk, beans, cups, money):
    coffee_type = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
    if coffee_type == '1':
        water, milk, beans, cups, money = espresso(water, milk, beans, cups, money)
    elif coffee_type == '2':
        water, milk, beans, cups, money = latte(water, milk, beans, cups, money)
    elif coffee_type == '3':
        water, milk, beans, cups, money = cappuccino(water, milk, beans, cups, money)
    return water, milk, beans, cups, money


def espresso(water, milk, beans, cups, money):
    if water >= 250 and beans >= 16 and cups >= 1:
        print('I have enough resources, making you a coffee!\n')
        water -= 250
        beans -= 16
        cups -= 1
        money += 4
    else:
        if water < 250:
            print_what_is_missing(1)
        elif beans < 16:
            print_what_is_missing(3)
        else:
            print_what_is_missing(4)
    return (water, milk, beans, cups, money)


def latte(water, milk, beans, cups, money):
    if water >= 350 and milk >= 75 and beans >= 20 and cups >= 1:
        print('I have enough resources, making you a coffee!\n')
        water -= 350
        milk -= 75
        beans -= 20
        cups -= 1
        money += 7
    else:
        if water < 350:
            print_what_is_missing(1)
        elif milk < 75:
            print_what_is_missing(2)
        elif beans < 20:
            print_what_is_missing(3)
        else:
            print_what_is_missing(4)
    return water, milk, beans, cups, money


def cappuccino(water, milk, beans, cups, money):
    if water >= 200 and milk >= 100 and beans >= 12 and cups >= 1:
        print('I have enough resources, making you a coffee!\n')
        water -= 200
        milk -= 100
        beans -= 12
        cups -= 1
        money += 6
    else:
        if water < 200:
            print_what_is_missing(1)
        elif milk < 100:
            print_what_is_missing(2)
        elif beans < 12:
            print_what_is_missing(3)
        else:
            print_what_is_missing(4)
    return water, milk, beans, cups, money


def show_supplies(water, milk, beans, cups, money):
    print(water, 'of water')
    print(milk, 'of milk')
    print(beans, 'of coffee beans')
    print(cups, 'of disposable cups')
    print(money, 'of money\n')


def print_what_is_missing(x):
    if x == 1:
        print('Sorry, not enough water!\n')
    if x == 2:
        print('Sorry, not enough milk!\n')
    if x == 3:
        print('Sorry, not enough coffee beans\n')
    if x == 4:
        print('Sorry, not enough disposable cups!\n')


water = 400
milk = 540
beans = 120
cups = 9
money = 550

my_test_class = CoffeeMachine(water, milk, beans, cups, money)
while True:
    my_test_class.interprete_the_action(input('Write action (buy, fill, take, remaining, exit):\n'))
