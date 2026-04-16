# Crop Yield Prediction System

def predict_yield(historical_yields, rainfall, fertilizer):
    """
    Predict crop yield using:
    - Average of historical yields
    - Weighted contribution of rainfall and fertilizer
    """

    # Step 1: Calculate average historical yield
    avg_yield = sum(historical_yields) / len(historical_yields)

    # Step 2: Normalize rainfall and fertilizer
    norm_rainfall = rainfall / 300      # Range: 0 to 1
    norm_fertilizer = fertilizer / 300  # Range: 0 to 1

    # Step 3: Apply weighted formula
    predicted = (0.6 * avg_yield) + (0.2 * avg_yield * norm_rainfall) + (0.2 * avg_yield * norm_fertilizer)

    return predicted


def categorize_yield(predicted):
    """
    Categorize yield into Low, Medium, High
    """

    if predicted < 2:
        return "Low"
    elif 2 <= predicted <= 3.5:
        return "Medium"
    else:
        return "High"


# Taking inputs
crop_name = input("Enter Crop Name: ")

n = int(input("Enter number of historical yield records (3 to 10): "))

historical_yields = []
for i in range(n):
    value = float(input(f"Enter yield for season {i+1} (tons/hectare): "))
    historical_yields.append(value)

rainfall = float(input("Enter average rainfall (mm): "))
fertilizer = float(input("Enter fertilizer usage (kg/hectare): "))

# Prediction
predicted_yield = predict_yield(historical_yields, rainfall, fertilizer)
category = categorize_yield(predicted_yield)

# Output
print("\nCrop:", crop_name)
print("Predicted Yield:", round(predicted_yield, 2), "tons/hectare")
print("Yield Category:", category)