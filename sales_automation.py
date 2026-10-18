total_sales = 0
max_sales = 0
sold_products = 0
average = 0
max_name = ""
max_product = ""


while True:
    name = input("Enter your name: ")
    if name == "exit":
        break
    product = input("Enter the product you want to purchase: ")
    price = int(input("Enter the price of the product: "))
    quantity = int(input("Enter the quantity you want to purchase: "))
    total = price * quantity
    print(f"Hello {name}, you have purchased {quantity} {product}(s) at ${price} each")
    print(f"Total cost for {quantity} {product}(s): ${total}")
    total_sales = total_sales + total
    sold_products = sold_products + quantity
    
    if total > max_sales:
        max_sales = total
        max_name = name
        max_product = product
        
        

if sold_products > 0:
    average = total_sales / sold_products
print(f"Total sales: {total_sales}")
print(f"Maximum sales: {max_sales}")
print(f"Total products sold: {sold_products}")
print(f"Average sales per product: {average}")
print(f"max sale details : costumer name {max_name} , product {max_product} ")