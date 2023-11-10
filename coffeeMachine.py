

from pickle import TRUE


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}




def money_stuff():
    
    cost = MENU[choice]["cost"]    
    quarters = int(input("how many quaters"))
    dimes = int(input("how many dimes"))
    nickles = int(input("how many nickles"))
    pennys = int(input("how many pennys"))
    your_money = 0.25 * quarters + 0.1* dimes + 0.05 * dimes + 0.01 * pennys
    if cost > your_money:
        print(f"you are poor...here's your refund {your_money} dollars")
        return
    else:
        if resource_need():
            resource_need()
            refund = your_money - cost
            print(f"take you refund {refund} dollars")
        else:
            print(f"take you refund {your_money} dollars")
        return
    

def resource_need():
    if MENU[choice]["ingredients"]["milk"]<=resources["milk"] \
        and MENU[choice]["ingredients"]["water"]<=resources["water"] \
        and MENU[choice]["ingredients"]["coffee"]<=resources["coffee"]:
        resources["milk"]-= MENU[choice]["ingredients"]["milk"]
        resources["water"]-=MENU[choice]["ingredients"]["water"]
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
        print (resources["milk"],resources["water"],resources["coffee"])
        print("enjoy your coffer")
        return True
    else:
        print("no enough resources")
        

def coffee_Machine():
    money_stuff()
    #code like a joke...
        

while TRUE:
    choice = input("espresso/latte/cappuccino   ")
    buy = input("buy some? Y/N")
    if buy == "Y":
        coffee_Machine()
    else:
        break
    
    
    

