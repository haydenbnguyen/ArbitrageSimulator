import pandas as pd
import numpy as np
from strategy import PairTradingStrategy
from data import load_price_data
from analysis import analyze_results

if __name__ == "__main__":
    # Example: Load sample data for two assets
    prices = load_price_data(["AAPL", "MSFT"], start_date="2020-01-01", end_date="2022-01-01")
    
    # Initialize and run the strategy
    strategy = PairTradingStrategy(prices)
    results = strategy.run()
    
    # Analyze and visualize results
    analyze_results(results)
