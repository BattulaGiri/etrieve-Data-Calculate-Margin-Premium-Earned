def calculate_margin_and_premium(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the margin required and premium earned for each option in the DataFrame.
    
    Args:
        data (pd.DataFrame): DataFrame with option chain data, including 'bid/ask' prices.

    Returns:
        pd.DataFrame: Modified DataFrame with added columns 'margin_required' and 'premium_earned'.
    """
    # Example lot size for calculation; this may vary by instrument
    lot_size = 100  # Adjust according to the instrument's lot size

    # Sample API endpoint for margin calculation (to be replaced with actual endpoint)
    margin_api_url = "https://api.yourbroker.com/calculate_margin"
    
    # Iterate through each row to calculate margin and premium for each option
    for idx, row in data.iterrows():
        # Calculate Premium Earned
        premium = row['bid/ask'] * lot_size
        data.at[idx, 'premium_earned'] = premium

        # Make an API request to get margin requirement for each option
        response = requests.get(margin_api_url, params={
            "instrument_name": row['instrument_name'],
            "strike_price": row['strike_price'],
            "side": row['side'],
            "transaction_type": "Sell"
        })
        
        # Error handling for the API response
        if response.status_code == 200:
            margin_data = response.json()
            data.at[idx, 'margin_required'] = margin_data.get('margin_required', 0)
        else:
            data.at[idx, 'margin_required'] = None  # Set as None if API call fails

    return data

# Example usage
enriched_data = calculate_margin_and_premium(option_data)
print(enriched_data)
