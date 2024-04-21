"""Returned Goods."""

# Define a new function called process_claims
def process_claims(claims):
    """
    Calculate the total insurance payout based on a list of claims.
    Args:
        claims (list): A list of claim amounts.
    Returns:
        float: The total insurance payout, which is 30% of the sum of all claims.
    """
    # Create a variable called `total_claims`, that is the sum of all claims
    total_claims = sum(claims)
    # Calculate a total payout, which is 30% of total_claims:
    total_payout = total_claims * 0.30
    # Return only the total_payout amount
    return total_payout

if __name__ == "__main__":
    # Add the weekly claims
    weekly_claims = [5000, 1000, 8000, 10000, 3000, 3500]
    # Create a variable that passes the weekly claims to the function.
    total_insurance_payout = process_claims(weekly_claims)
    # Print the total insurance payout to 2 decimal places.
    print(f"The total insurance payout is: ${total_insurance_payout: ,.2f}.")
