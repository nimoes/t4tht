#!/usr/bin/python3
"""
use free coingecko api subscription to fetch historical tht price.

"""

import argparse
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
print(cg)
print(dir(cg))
print(cg.get_price(ids='thought', vs_currencies='usd'))
#cg.get_coin_market_chart_range_by_id()

if __name__ == '__main__':
    # add args
    parser = argparse.ArgumentParser(description="Based on specified timezone,\
        input file, the program will generate new output with tht price at that time", \
            epilog="python ")
    parser.add_argument("-c", "--currency", required=True, type=str, \
         help="specify currency \(\'usd\', \'eur\'\)")
    parser.add_argument("-tz", "--timezone", required=True, type=str, \
         help="select the timezone, in utc, in which the transactions are based in\
             \(\'utc+/-12\'\)")
    parser.add_argument("-i", "--input", required=True, type=str, \
        help="specify the input filename with csv extension")
    parser.add_argument("-o", "--output", required=True, type=str, \
        help="name your output")
