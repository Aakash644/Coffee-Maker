logo='''
 _____          __   __             ___  ___        _               
/  __ \        / _| / _|            |  \/  |       | |              
| /  \/  ___  | |_ | |_  ___   ___  | .  . |  __ _ | | __ ___  _ __ 
| |     / _ \ |  _||  _|/ _ \ / _ \ | |\/| | / _` || |/ // _ \| '__|
| \__/\| (_) || |  | | |  __/|  __/ | |  | || (_| ||   <|  __/| |   
 \____/ \___/ |_|  |_|  \___| \___| \_|  |_/ \__,_||_|\_\\___||_|   
                                                                    
                                                                    
'''
coffeesold={"cappucino":0,"latte":0,"espresso":0,"caramel frappe":0,"vanilla frappe":0,"hazelnut frappe":0}
def transaction(item, cost, num):
    sum = 0
    sum += (int(input("Enter the number of Rs 1 coins: "))*1)
    sum += int(input("Enter the number of Rs 2 coins: "))*2
    sum += int(input("Enter the number of Rs 5 coins: "))*5
    sum += int(input("Enter the number of Rs 10 notes: "))*10
    sum += int(input("Enter the number of Rs 20 notes: "))*20
    sum += int(input("Enter the number of Rs 50 notes: "))*50
    sum += int(input("Enter the number of Rs 100 notes: "))*100
    sum += int(input("Enter the number of Rs 200 notes: "))*200

    if (sum >= (cost*num)):  
        count=1
        for item1 in reserve: 
            requir=(drink[item]["ingredients"][item1])*num
            if  requir > reserve[item1]:
                print(f"​Sorry there is not enough {item1}.") 
                count=0
        if(count==1):
            change = sum-cost*num 
            coffeesold[item]+=num;
            print(f"Here's, your {num}-{item}!\nHave a nice day!")
            for i in reserve:
                reserve[i] -= drink[item]["ingredients"][i]*num
            if (change > 0):
                print(f"Here's, your change of Rs.{change}") 
        else: 
            print("Transaction failed!Money refunded.\n")
    else:
        print("Transaction failed!Money refunded.\n")

def report(): 
    print("Total stock  remaining") 
    print(reserve)
    print("Total coffee sold") 
    print(coffeesold)
reserve = {"water": 3000, "milk": 3000, "coffee": 1000,
    "vanilla": 500, "hazelnut": 500, "caramel": 500}
drink = {"cappucino": {"ingredients": {"water": 20, "milk": 120, "coffee": 30, "vanilla": 0, "hazelnut": 0, "caramel": 0}, "cost": 99}, "latte": {"ingredients": {"water": 20, "milk": 140, "coffee": 30, "vanilla": 0, "hazelnut": 0, "caramel": 0}, "cost": 149}, "espresso": {"ingredients": {"water": 120, "milk": 0, "coffee": 60, "vanilla": 0, "hazelnut": 0, "caramel": 0},
    "cost": 179}, "caramel frappe": {"ingredients": {"water": 20, "milk": 120, "coffee": 60, "vanilla": 0, "hazelnut": 0, "caramel": 30}, "cost": 149}, "vanilla frappe": {"ingredients": {"water": 100, "milk": 120, "coffee": 30, "vanilla": 30,"hazelnut": 0, "caramel": 0}, "cost": 159}, "hazelnut frappe": {"ingredients": {"water": 120, "milk": 120, "coffee": 30, "vanilla": 0, "hazelnut": 30,"caramel": 0 }, "cost": 169}}

while(1):
    print(logo)  
   
    choice=int(input("Hello, what would you like to have ?\n1.Hot Coffee\n2.Cold Coffee\n3.Report\n4.exit\n")) 
    

    '''item      water     milk    coffee  vanilla  hazelnut  caramel
    cappucino     20      120      30        0         0        0
    latte         20      140      30        0         0        0
    espresso      120     0        60        0         0        0
    caramelfrappe 100     100      60        0         0       30
    vanillafrappe 100     100      30       30         0        0
    hazelnutfrappe100     100      30        0        30        0 '''
    if(choice == 1):
        choice1 = int(input("Item          Price\n1.Cappaucino  Rs.99\n2.Latte       Rs.149\n3.Espresso    Rs.179\nEnter your choice:\n"))
        if (choice1 == 1): 
            coffee="cappucino"
            num=int(input(f"Enter the number of {coffee}:"))
            transaction("cappucino", drink["cappucino"]["cost"],num)
        elif (choice1 == 2): 
            coffee="latte"
            num=int(input(f"Enter the number of {coffee}:"))
            transaction("latte", drink["latte"]["cost"],num)
        elif (choice1 == 3):
            coffee="espresso"
            num=int(input(f"Enter the number of {coffee}:"))
            transaction("espresso", drink["espresso"]["cost"],num) 
    elif(choice==2):
        choice1 = int(input("Item                Price\n1.Caramel frappe    Rs.149\n2.Vanilla frappe    Rs.159\n3.Hazelnut frappe   Rs.169\nEnter your choice:\n"))
        if (choice1 == 1): 
            coffee="caramel frappe"
            num=int(input(f"Enter the number of {coffee}:"))
            transaction("caramel frappe", drink["caramel frappe"]["cost"],num)
        elif (choice1 == 2): 
            coffee="vanilla frappe"
            num=int(input(f"Enter the number of {coffee}:"))
            transaction("vanilla frappe", drink["vanilla frappe"]["cost"],num)
        elif (choice1 == 3): 
            coffee="hazelnut frappe"
            num=int(input(f"Enter the number of {coffee}:"))
            transaction("hazelnut frappe", drink["hazelnut frappe"]["cost"],num)  
    elif(choice==3):
        report()
    elif(choice==4):
        exit(0) 
    else:
        print("invalid input\n")


