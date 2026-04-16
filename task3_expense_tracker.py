# Farm Expense and Profit Tracker

def calculate_total_expense(seed, fertilizer, labor, irrigation):
    """
    Calculate total farming expense
    """
    return seed + fertilizer + labor + irrigation


def calculate_profit_or_loss(total_expense, revenue):
    """
    Determine profit, loss, or break-even
    """
    net = revenue - total_expense

    if net > 0:
        return f"Profit of {net}"
    elif net == 0:
        return "Break-even"
    else:
        return f"Loss of {abs(net)}"


# Taking inputs
seed_cost = int(input("Enter Seed Cost: "))
fertilizer_cost = int(input("Enter Fertilizer Cost: "))
labor_cost = int(input("Enter Labor Cost: "))
irrigation_cost = int(input("Enter Irrigation Cost: "))
revenue = int(input("Enter Total Revenue: "))

# Calculations
total_expense = calculate_total_expense(
    seed_cost, fertilizer_cost, labor_cost, irrigation_cost
)

result = calculate_profit_or_loss(total_expense, revenue)

# Output
print("\nSeed Cost:", seed_cost)
print("Fertilizer Cost:", fertilizer_cost)
print("Labor Cost:", labor_cost)
print("Irrigation Cost:", irrigation_cost)
print("Total Expense:", total_expense)
print("Revenue:", revenue)
print("Net Result:", result)