# change_from_dollar.py

"""
Write a program that, given a price in cents that is less than a dollar (i.e., 100 cents),
determines the method of giving change that uses the fewest coins. The program will not
take input from the user, but rather it will begin with a hard-coded value for the price, i.e.:

    price = 67

"""

coins = {
    "quarter": 25,
    "dime": 10,
    "nickle": 5,
    "penny": 1
    }

def change_from_dollar(price):
    remaining_amt = price

    for coin in coins:
        coins_needed = remaining_amt//coins[coin]
        print("{}:{}".format(coin, coins_needed))

        remaining_amt =  remaining_amt - (coins_needed * coins[coin])

if __name__ == "__main__":
    try:
        price = int(input("Input Price Integer Less than 100: "))
        change_from_dollar(price)
    except:
        print("Wrong Input")