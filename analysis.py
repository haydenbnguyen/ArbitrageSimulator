import matplotlib.pyplot as plt

def analyze_results(results):
    pnl = results["pnl"]
    spread = results["spread"]
    zscore = results["zscore"]
    
    fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
    axs[0].plot(spread.index, spread, label="Spread")
    axs[0].set_title("Spread")
    axs[1].plot(zscore.index, zscore, label="Z-Score")
    axs[1].axhline(1, color="r", linestyle="--")
    axs[1].axhline(-1, color="g", linestyle="--")
    axs[1].set_title("Z-Score")
    axs[2].plot(pnl.index, pnl, label="PnL")
    axs[2].set_title("Cumulative PnL")
    plt.tight_layout()
    plt.show()
