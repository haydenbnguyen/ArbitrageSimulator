import numpy as np
import pandas as pd

class PairTradingStrategy:
    def __init__(self, prices: pd.DataFrame):
        self.prices = prices
        self.spread = None
        self.positions = None
        self.pnl = None

    def run(self):
        # Simple z-score mean reversion strategy
        s1, s2 = self.prices.columns[:2]
        spread = self.prices[s1] - self.prices[s2]
        zscore = (spread - spread.mean()) / spread.std()
        self.positions = pd.DataFrame(index=self.prices.index, columns=self.prices.columns)
        self.positions[s1] = -np.where(zscore > 1, 1, 0) + np.where(zscore < -1, 1, 0)
        self.positions[s2] = np.where(zscore > 1, 1, 0) - np.where(zscore < -1, 1, 0)
        self.pnl = (self.positions.shift().fillna(0) * self.prices.pct_change()).sum(axis=1).cumsum()
        return {"spread": spread, "zscore": zscore, "positions": self.positions, "pnl": self.pnl}
