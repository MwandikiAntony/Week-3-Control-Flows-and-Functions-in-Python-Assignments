# Step 1: Define the calculate_discount function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Step 2: Prompt the user for the original price and discount percentage
price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Step 3: Call the calculate_discount function and display the result
final_price = calculate_discount(price, discount_percent)

# Output the final price, each on a new line
print("The final price after applying the discount is:")
print(f"${final_price:.2f}")
