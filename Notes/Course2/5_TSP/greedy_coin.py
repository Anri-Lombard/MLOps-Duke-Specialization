from typing import Dict

def greedy_coin(change: float) -> Dict[float, int]:
    """
    Calculate the minimum number of coins needed to make the given change.
    
    Parameters:
    change (float): The amount of change needed.
    
    Returns:
    dict: A dictionary with the coin type as the key and the number of coins as the value.
    """
    coins = [0.25, 0.1, 0.05, 0.01]
    coins.sort(reverse=True)
    coin_count = {}

    for coin in coins:
        count, change = divmod(change, coin)
        coin_count[coin] = int(count)

    print(f"Change can be given as:")
    for coin, count in coin_count.items():
        print(f"{count} coin(s) of {coin} dollar(s)")

    return coin_count


