MENU={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
     "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
     "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    }
}
profit=0
resources={
    "water":300,
    "milk":200,
    "coffee":100,
    
}


#check resources sufficient
def is_resource_suff(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:   #if order in resource (curr item) cost is less than the required amount then return false
            print(f"Sorry there is not enough {item}.")
            return False
        return True

#process coin quaters=$0.25 ,nickles=$0.05,pennies=$0.01
def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total=int(input("how many quarters?:"))*0.25
    total+=int(input("how many dimes?:"))*0.1
    total+=int(input("how many nickles?:"))*0.05
    total+=int(input("how many pennies?:"))*0.01
    return total

#check transcation is successful
def is_trans_success(money_recieved,drink_cost):
    if money_recieved>=drink_cost:
        change=round(money_recieved-drink_cost)
        print(f"Here is ${change} in change.")
        global profit
        profit+=drink_cost
        return  True
    else:
        print("Sorry that's not enough money.Money refunded.")
        return False

#make coffee -> transcation success,enough resource then 
# the drink user selected need to be deducted from machine
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name}")


is_on=True
#the prompt shd show again to serve the nxt customer.
while is_on:
    #prompt user by asking what wuld you like?
    choice=input("what wuld you like?(espresso/latte/cappuccino):")
     
    #turn off the machine with prompt off
    if choice=="off":
        is_on=False
    #print report -> where it has current resource value
    elif choice=="report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money:${profit}")
    
    else:
        drink=MENU[choice]
        if is_resource_suff(drink["ingredients"]):
            payment=process_coins()
            if is_trans_success(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])

   




