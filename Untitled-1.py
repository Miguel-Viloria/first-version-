# Checkout system for a retail store
def checkout_system():
    # Input and Output as mentioned in Lesson 2
    # Function to calculate total and apply discounts
    def calculate_total(item_prices):
        total = sum(item_prices)
        discount = 0
        if total > 100:
            discount = 0.10 * total
            print(f"You qualify for a 10% discount of ${discount:.2f}!")
        return total - discount, discount

    # Function to calculate loyalty points
    def calculate_loyalty_points(total):
        loyalty_points = total // 10  # 1 point for every $10 spent
        return loyalty_points

    # Function to handle payment
    def accept_payment(total):
        while True:
            payment = float(input(f"Your total is ${total:.2f}. Please enter your payment: "))
            if payment >= total:
                change = payment - total
                if change > 0:
                    print(f"Payment accepted. Your change is ${change:.2f}.")
                else:
                    print("Payment accepted. No change required.")
                break
            else:
                print("Payment is less than the total. Please enter a valid amount.")

    # Main logic of the program
    print("Welcome to the checkout system!\n")
    
    # Collect prices of three items
    item_prices = []
    for i in range(1, 4):
        price = float(input(f"Enter the price of item {i}: $"))
        item_prices.append(price)
    
    # Calculate total, discounts, and loyalty points
    final_total, discount = calculate_total(item_prices)
    loyalty_points = calculate_loyalty_points(final_total)
    
    # Display final total and loyalty points earned
    print(f"\nThe total after discount is: ${final_total:.2f}")
    print(f"You've earned {loyalty_points:.0f} loyalty points.\n")
    
    # Accept payment and handle change
    accept_payment(final_total)
    print("Thank you for shopping with us!\n")

# Run the checkout system
checkout_system()