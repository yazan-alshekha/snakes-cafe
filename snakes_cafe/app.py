Appetizers=["Wings","Cookies","Spring Rolls"]
Entrees=["Salmon","Steak","Meat Tornado","A Literal Garden"]
Desserts=["Ice Cream","Cake","Pie"]
Drinks=["Coffee","Tea","Unicorn Tears"]

print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**")
print("** To quit at any time, type 'quit' **")
print("**************************************")

print("***********************************")
print("** What would you like to order? **")
print("***********************************")

def print_category(list,listName):
    print("--------")
    print(listName)
    print("--------")
    for item in list:
        print(item)


print_category(Appetizers,"Appetizers")
print_category(Entrees,"Entrees")
print_category(Desserts,"Desserts")
print_category(Drinks,"Drinks")

request=""
meal={}

while request!="quit":
    request= str(input())
    if request in meal:
     meal[request]+=1
    else:
        meal[request]=1
    if request!="quit":
        print(f"{meal[request]} order of {request} have been added to your meal")        




   






 


