# function to calculate the final price after discount
def calculate_discount(price, discount_percent):
    if discount_percent > 20:
        discount_price = price * (discount_percent/100)
        final_price = price - discount_price
        print("The final price of the item is", final_price)
        # return final_price
    else:
        print("No discount awarded for this percent")
        # return price

price = int(input("What is the price of the item?"))
discount_price = int(input("What is the discount percent of the item?"))

calculate_discount(price, discount_price)

