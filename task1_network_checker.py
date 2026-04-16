# Mobile Network Signal Quality Checker

def check_network_quality(signal_strength, latency):
    """
    Function to classify network quality based on:
    - Signal Strength (in dBm)
    - Latency (in ms)
    """

    if signal_strength >= -70 and latency <= 50:
        return "Excellent"
    
    elif (signal_strength < -85) or (latency > 150):
        return "Poor"
    
    else:
        return "Average"


# Taking user input
signal_strength = float(input("Enter Signal Strength (dBm): "))
latency = float(input("Enter Network Latency (ms): "))

# Checking network quality
quality = check_network_quality(signal_strength, latency)

# Display result
print("Network Quality:", quality)