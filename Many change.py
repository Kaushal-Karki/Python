# Function to convert Rupees to Dollars
def rupees_to_dollars(rupees, rate):
    """
    rupees : amount in INR
    rate : conversion rate (1 USD = ? INR)
    returns : equivalent amount in USD
    """
    dollars = rupees / rate
    return dollars

# Input from user
rupees = float(input("Enter amount in Rupees (Rs): "))
rate = float(input("Enter conversion rate (1 USD = ? Rs): "))

# Call function and display result
usd = rupees_to_dollars(rupees, rate)
print(f"{rupees} Rs = {usd:.2f} $")
