import numpy as np
from scipy.stats import linregress 
import os





if __name__ == '__main__':
    first_line = input().split()
    holdings, num_stocks, days_remaining = float(first_line[0]), int(first_line[1]), int(first_line[2])

    buy_transactions = []
    final_transactions = []


    # Need to do time series forcasting instead of +/- for determining buy or sell
    # if os.path.isfile("historical_prices.txt"):
    #     f = open("historical_prices.txt", "r")
    #     lines = f.readlines()
    #     info = []
    #     for line in lines:
    #         line = line.strip("\n").split()
    #         line = [line[0]] + [line[1]] + list(map(float, line[2:])) + [float(input().split()[-1])]
    #         info.append(line)
    #     f.close()

        
    # else:
    #     info = [input().split() for _ in range(num_stocks)]
    
    # with open('historical_prices.txt', 'w') as f:
    #         for frame in info:
    #             f.write(' '.join(str(num) for num in frame))
    #             f.write('\n')
    

    info = [input().split() for _ in range(num_stocks)]

    for stock_info_line in info:
    
        stock = stock_info_line[0]
        num_stocks_owned = int(stock_info_line[1])
        stock_prices = list(map(float, stock_info_line[2:]))
        historical_prices_slope = linregress(list(range(len(stock_prices))), stock_prices).slope
        
        if historical_prices_slope < 0:
            buy_transactions.append({
                'stock': stock,
                "curr_stock_price": stock_prices[-1]
            })
        else:
            if num_stocks_owned > 0:
                final_transactions.append({
                    'stock': stock,
                    "num_stocks": num_stocks_owned,
                    "transaction": "SELL",
                    "curr_stock_price": stock_prices[-1]
                })  

    sorted_buy_transactions = sorted(buy_transactions, key=lambda k: k['curr_stock_price'], reverse=True)

    for i in range(len(sorted_buy_transactions)):

        num_shares_can_buy = int(holdings // sorted_buy_transactions[i]['curr_stock_price'])

        if num_shares_can_buy == 0:
            continue

        holdings -= (num_shares_can_buy * sorted_buy_transactions[i]['curr_stock_price'])
        final_transactions.append({
                'stock': sorted_buy_transactions[i]['stock'],
                "num_stocks": num_shares_can_buy,
                "transaction": "BUY",
                "curr_stock_price": sorted_buy_transactions[i]['curr_stock_price']
            })

    print(len(final_transactions))
    for tran in final_transactions:
        print(f"{tran['stock']} {tran['transaction']} {tran['num_stocks']}")
        