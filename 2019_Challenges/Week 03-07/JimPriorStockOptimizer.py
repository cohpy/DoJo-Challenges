#!/usr/bin/env python3

"""
Jim Prior's solution to the following problem:

Given a array of numbers representing the stock prices of a company in
chronological order, write a function that calculates the maximum profit you
could have made from buying and selling that stock once. You must buy
before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you
could buy the stock at 5 dollars and sell it at 10 dollars.

This solution accepts the array on th command line.
"""

import sys


def get_prices_from_arguments(args):
    return list(map(int, args[1:]))


def calculate_maximum_profit(prices):
    maximum_profit = 0
    maximum_price = None

    for price in reversed(prices):
        if maximum_price is None or price > maximum_price:
            maximum_price = price
        profit = maximum_price - price
        if profit > maximum_profit:
            maximum_profit = profit

    return maximum_profit


def main(args):
    prices = get_prices_from_arguments(args)
    maximum_profit = calculate_maximum_profit(prices)
    print(maximum_profit)


if __name__ == '__main__':
    main(sys.argv)
