import requests
import pandas as pd

def get_option_chain_data(instrument_name: str, expiry_date: str, side: str) -> pd.DataFrame:
    """
    Fetches the option chain data for a given instrument and expiry date.
    Retrieves the highest bid price for 'PE' (Put Option) or highest ask price for 'CE' (Call Option) for each strike price.
    
    Args:
        instrument_name (str): Name of the financial instrument (e.g., NIFTY, BANKNIFTY).
        expiry_date (str): Expiration date of the option in YYYY-MM-DD format.
        side (str): Option type; 'PE' for Put or 'CE' for Call.

    Returns:
        pd.DataFrame: A DataFrame containing columns instrument_name, strike_price, side, and bid/ask.
    """
    # Example API endpoint (replace with the actual endpoint from the API you choose)
    api_url = f"https://api.yourbroker.com/option_chain/{instrument_name}/{expiry_date}"

    # Headers and API key (update with your actual API authentication details)
    headers = {
        "Authorization": "Bearer YOUR_API_KEY"
    }
    
    response = requests.get(api_url, headers=headers)
    data = response.json()  # Parsing the JSON response
    
    # Extract the option data and filter by the specified option side ('PE' or 'CE')
    options = data['options']  # Adjust this based on the actual JSON structure from the API
    filtered_options = [option for option in options if option['side'] == side]
    
    # Prepare a list to hold processed data
    rows = []

    # Loop through each option to identify the highest bid or ask price
    for option in filtered_options:
        strike_price = option['strike_price']
        price = option['bid_price'] if side == 'PE' else option['ask_price']
        
        # Append data for each strike price
        rows.append({
            "instrument_name": instrument_name,
            "strike_price": strike_price,
            "side": side,
            "bid/ask": price
        })
    
    # Convert to DataFrame for structured data output
    df = pd.DataFrame(rows)
    return df

# Example usage
instrument = "NIFTY"
expiry = "2024-12-25"
option_side = "PE"  # Use "PE" for Put Option or "CE" for Call Option
option_data = get_option_chain_data(instrument, expiry, option_side)
print(option_data)
