products = [
    {
        "name": "phone cover",
        "price": 500,
        "quantity": 18
    },
    {
        "name": "teddy",
        "price": 300,
        "quantity": 9
    },
    {
        "name": "kitty bag",
        "price": 999,
        "quantity": 0
    }
]
print("===> Product Management system <===")
print("here you can add new product / search product / view products / show total product / delete product / product analysis / stock analysis! ")
print("want to leave type (exit)!")
user  = input("type as you want: ")
while user != "exit": 
    
    if user != "exit" and user != "add new product" and user != "search product" and user != "product analysis" and user != "stock analysis" and user != "view products" and user != "show total product" and user != "delete product":
        print("invalid type 😥😭")
        print("chosses valid option.")

    if user == "add new product":
        name = input("enter product name:")
        price = int(input("enter product price:"))
        quantity = int(input("enter product quantity:"))
        for k in products:
            if k["name"] == name:
                print("Product already exists.")
                break
        else:
            new_product = {
                "name": name,
                "price": price,
                "quantity": quantity
            }
            products.append(new_product)
            print("Product added successfully.")
        
    if user == "search product":
        name = input("enter product name:")
        for j in products:
            if j["name"] == name:
                print(j)
                break
        else:
            print("Product not found.")
    
    if user == "show total product":
        print("total products =",len(products))

    if user == "view products":
        if products == []:
            print("No products avialable.")
        for j in products:
            print(j)

    if user == "delete product":
        name = input("enter product name:")
        for j in products:
            if j["name"] == name:
                products.remove(j)
                break
        else:
            print("Product not found.")

    if user == "product analysis":
        e_count = 0
        a_count = 0
        for j in products:
            if j["price"] >= 500:
                print(j["name"],"is expencive product.")
                e_count += 1

            else:
                print(j["name"],"is avrage product")
                a_count += 1
        print("total expencive product =",e_count)
        print("total avrage product =",a_count)

    if user == "stock analysis":
        for k in products:
            if k["quantity"] >= 10:
                print(k["name"],"--> in stock")
            elif k["quantity"]  > 0:
                print(k["name"],"--> low stock")
            else:
                print(k["name"],"--> out of stock")
        
    
    print("-----------------------------------------------------------------------------------------------------")
    print("select another options.")
    print("-----------------------------------------------------------------------------------------------------")
    print("here you can add new product / search product / view products / show total product / delete product / product analysis / stock analysis! ")
    print("want to leave type (exit)!")
    user  = input("type as you want: ")
