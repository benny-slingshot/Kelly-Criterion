import numpy as np
import matplotlib.pyplot as plt

def kelly_criterion(win_rate, win_loss_ratio):
    """
    Calculate the Kelly Criterion fraction.
    
    :param win_rate: Probability of winning a trade (0 to 1)
    :param win_loss_ratio: Ratio of average win to average loss
    :return: Kelly fraction (optimal fraction of capital to risk)
    """
    return win_rate - (1 - win_rate) / win_loss_ratio

def calculate_position_size(kelly_fraction, account_balance, max_risk_percentage=0.05):
    """
    Calculate the position size based on the Kelly Criterion.
    
    :param kelly_fraction: Kelly Criterion fraction
    :param account_balance: Total account balance
    :param max_risk_percentage: Maximum risk percentage per trade (default 5%)
    :return: Recommended position size
    """
    # Limit the Kelly fraction to the maximum risk percentage
    risk_fraction = min(kelly_fraction, max_risk_percentage)
    return account_balance * risk_fraction

# Example usage
win_rate = 0.55  # 55% win rate
avg_win = 100  # Average win amount
avg_loss = 80  # Average loss amount
win_loss_ratio = avg_win / avg_loss
account_balance = 10000  # Total account balance

# Calculate Kelly Criterion fraction
kelly_fraction = kelly_criterion(win_rate, win_loss_ratio)

# Calculate recommended position size
position_size = calculate_position_size(kelly_fraction, account_balance)

print(f"Kelly Criterion fraction: {kelly_fraction:.4f}")
print(f"Recommended position size: ${position_size:.2f}")

# Simulate trades
num_trades = 1000
np.random.seed(42)  # For reproducibility

balance = account_balance
balances = [balance]

for _ in range(num_trades):
    position_size = calculate_position_size(kelly_fraction, balance)
    outcome = np.random.choice(["win", "loss"], p=[win_rate, 1 - win_rate])
    
    if outcome == "win":
        balance += position_size * (avg_win / avg_loss)
    else:
        balance -= position_size
    
    balances.append(balance)

# Plot results

plt.figure(figsize=(10, 6))
plt.plot(balances)
plt.title("Account Balance Over Time")
plt.xlabel("Number of Trades")
plt.ylabel("Account Balance ($)")
plt.show()
