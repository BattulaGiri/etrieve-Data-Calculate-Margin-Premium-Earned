# Options Trading Analysis

This project involves two primary coding tasks to retrieve and process options trading data for a specified instrument (e.g., NIFTY). The tasks include fetching option chain data, filtering for specific options, and calculating required margins and premiums earned.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Task Breakdown](#task-breakdown)
- [Usage](#usage)
- [Example Output](#example-output)
- [Assumptions and Notes](#assumptions-and-notes)

## Introduction

This project retrieves options data for a given instrument and processes it to calculate metrics essential for options trading analysis. It uses Python and requires access to a broker API to fetch live options data.

## Project Structure

The main components include:
- `get_option_chain_data()`: Fetches option chain data and structures it in a DataFrame.
- `calculate_margin_and_premium()`: Calculates the margin and premium earned for options trading based on the data from `get_option_chain_data()`.

## Setup Instructions

### Prerequisites
- Python 3.7+
- Packages: `pandas`, `requests`
- Access to an API key for options data

### Installation
1. Clone the repository.
2. Install required packages:
    ```bash
    pip install pandas requests
    ```

3. Set up API credentials in `config.py` or directly in the script.

## Task Breakdown

### Part 1: Retrieve Option Chain Data

#### Function: `get_option_chain_data`

**Objective**: Fetch option chain data for a specified instrument.

**Inputs**:
- `instrument_name` (str): Name of the instrument (e.g., "NIFTY").
- `expiry_date` (str): Expiration date for the option contract.
- `side` (str): Type of option ("PE" for put, "CE" for call).

**Logic**:
- Make a GET request to the API with the instrument name and expiry date.
- Filter for options based on `side`:
  - If "PE", find the highest bid price for put options.
  - If "CE", find the highest ask price for call options.
- Structure the data into a `pandas` DataFrame.

**Output**: A DataFrame with columns `instrument_name`, `strike_price`, `side`, and `bid/ask`.

### Part 2: Calculate Margin and Premium Earned

#### Function: `calculate_margin_and_premium`

**Objective**: Extend the DataFrame from Part 1 to include calculated columns `margin_required` and `premium_earned`.

**Inputs**: DataFrame from `get_option_chain_data`

**Logic**:
1. For each row in the DataFrame:
   - Calculate `margin_required` based on the transaction type ("Sell") by calling the API.
   - Calculate `premium_earned` by multiplying the bid/ask price by the lot size.
2. Add the calculated values to the DataFrame.

**Output**: The updated DataFrame with additional columns `margin_required` and `premium_earned`.

## Usage

Here is an example usage of the two main functions.

```python
import pandas as pd

# Example Part 1: Retrieve Option Chain Data
data = get_option_chain_data("NIFTY", "2024-12-15", "CE")
print("Option Chain Data:")
print(data)

# Example Part 2: Calculate Margin and Premium
enhanced_data = calculate_margin_and_premium(data)
print("Enhanced Data with Margin and Premium:")
print(enhanced_data)

