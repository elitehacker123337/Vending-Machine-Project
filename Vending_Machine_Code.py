vending_machine = [
    {'Code': 'A1', 'Product': 'Maltesers', 'Price': 4.25},
    {'Code': 'A2', 'Product': 'Bounty', 'Price': 3.90},
    {'Code': 'A3', 'Product': 'Kinder Bueno', 'Price': 4.75},
    {'Code': 'A4', 'Product': 'Galaxy Flutes', 'Price': 4.75},
    {'Code': 'A5', 'Product': 'Snickers', 'Price': 3.90},
    {'Code': 'A6', 'Product': 'Peanuts', 'Price': 2.00},
    {'Code': 'A7', 'Product': 'Twix', 'Price': 3.90},
    {'Code': 'A8', 'Product': 'Sponge Cake', 'Price': 3.50},
    {'Code': 'A9', 'Product': 'Lays Ketchup', 'Price': 2.00},
    {'Code': 'A10', 'Product': 'Lays Spicy', 'Price': 2.00},
    {'Code': 'B1', 'Product': 'Lays Vinegar', 'Price': 2.00},
    {'Code': 'B2', 'Product': 'Forno Salt Chips', 'Price': 3.90},
    {'Code': 'B3', 'Product': 'Barbican Pomegranate', 'Price': 4.75},
    {'Code': 'B4', 'Product': 'Barbican Orange', 'Price': 3.00},
    {'Code': 'B5', 'Product': 'Energy Drink', 'Price': 6.00},
    {'Code': 'B6', 'Product': 'Kinder Bueno', 'Price': 4.75},
    {'Code': 'B7', 'Product': 'RedBull White', 'Price': 3.45},
    {'Code': 'B8', 'Product': 'RedBull Normal', 'Price': 3.75},
    {'Code': 'B9', 'Product': 'Coca Cola', 'Price': 3.00},
    {'Code': 'B10', 'Product': 'Water', 'Price': 1.00},
]

#print the welcome message
print("Welcome to my vending machine!")
print() #gives space for the text below

#display the menu/all the items in the vending machine in a specific format, allowing for spaced between code, product and price 
# to make it look like a table
print(f"{'Code':<6} {'Product':<25} {'Price'}")
print("-" * 40)
for item in vending_machine:
    print(f"{item['Code']:<6} {item['Product']:<25} SAR{item['Price']:.2f}")
print()

#ask a product code from the user
name = input("Hello! Please enter your name to start your vending machine experience, or else type 'EXIT' to exit): \n").capitalize()
welcome = True 

while welcome: 
    if name == 'Exit': #allows the user to exit the program without selecting an item
            print('Goodbye..')
            welcome = False #'welcome' turns False in order to stop the while loop
            break #exit the loop and stop the program, withou this it would still print goodbye and exit the loop, but it would continue 
                  # onto the next lines of code
     
#find the product fom the user input
    shopping = True
    selected_items = []  #list to store all selected items (used to display the user's cart later in the code)
    total_price = 0  #running total
    
    while shopping:
        product_code = input(f"Greetings {name}! please enter product code: ").upper()
        
        #find the product from the dictionary list
        selected_product = None
        for item in vending_machine:
            if item['Code'] == product_code:
                selected_product = item
                
        
        #check if product exists in the list of dictionaries
        if selected_product:
            print(f"You selected: {selected_product['Product']} - ${selected_product['Price']:.2f}")
            selected_items.append(selected_product)
            total_price += selected_product['Price']
            print(f"Current total: ${total_price:.2f}")
        else:
            print("Invalid product code. Please try again.")
        
        #ask if user wants more items
        print("\nWould you like to add another item? (y/n): ")
        more_items = input().strip().lower()
        
        if more_items != 'y': 
            shopping = False #if user does not enter 'y' shopping becomes false to close the loop and move on to the enxt block of code
    
    #display cart summary (what the empty 'selected_items' list is used for, the selected items were stored in the list and then displayed here)
    print("\n--- Your Cart ---")
    for item in selected_items:
        print(f"{item['Product']}: ${item['Price']:.2f}") #using a for loop to display specific items from the 'selected_items' list
    print(f"\nTotal: ${total_price:.2f}")
    
    #get payment from the user
    #a payment loop keeps asking until sufficient payment is received
    balance = 0  #track total money inserted
    paying = True
    
    while paying: #making a while loop allows for the user to input multiple amounts of money in case of insufficient payment
        try: #Try Except in python is useful for loops and avoiding value errors
            payment = float(input(f"Please insert payment (Remaining: SAR{total_price - balance:.2f}): ")) #main payment input
            balance += payment  #allows checking if the payment is sufficient by meeting the required balance
            
            if balance < total_price: #if user input does not match the total price
                remaining = total_price - balance #track the remaining balance by subtracting the total price by the user payment
                print(f"Insufficient payment. You need SAR{remaining:.2f} more. \n")
            elif balance >= total_price: #if user enters more than total price
                change = balance - total_price #track the change of the user
                if change > 0: #print change, if present
                    print(f"\nChange: SAR{change:.2f}")
                
                print("\nDispensing products...")
                for item in selected_items: #dispense selected products from the cart list
                    print(f"  - {item['Product']}")

                #print goodbye message when all other conditions have been met, and all previous lines of code have been completed
                print("\nThank you for your purchase! Have a great day!") 
                paying = False  #exit payment loop
                welcome = False  #exit main loop
                
        except ValueError: #print in case user enters an invalid input
            print("Invalid amount. Please enter a valid number.\n")
            
  
