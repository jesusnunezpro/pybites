PENNY = "penny"  # use this to represent the penny
NICKEL = "nickel"  # use this to represent the nickel
DIME = "dime"  # use this to represent the dime
QUARTER = "quarter"  # use this to represent the quarter


def coins_on_the_table():
    """Return a sequence of all 1001 coins on the table."""
    coins = list()
    for i in range(1,1002):
        if i % 4 == 0:
            coins.append(QUARTER)
        elif i % 3 == 0:
            coins.append(DIME)
        elif i % 2 == 0:
            coins.append(NICKEL)
        else:
            coins.append(PENNY)
    return coins

if __name__ == "__main__":
    coin_list = coins_on_the_table()
    print(coin_list)
    print("Pennies: ", len([coin for coin in coin_list if coin == PENNY]))
    print("Nickels: ", len([coin for coin in coin_list if coin == NICKEL]))
    print("Dime: ", len([coin for coin in coin_list if coin == DIME]))
    print("Quarter: ", len([coin for coin in coin_list if coin == QUARTER]))