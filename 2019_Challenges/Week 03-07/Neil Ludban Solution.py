#!/usr/bin/env python3.7
"""
Given a array of numbers representing the stock prices of a company in
chronological order, write a function that calculates the maximum profit you
could have made from buying and selling that stock once. You must buy before
you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you
could buy the stock at 5 dollars and sell it at 10 dollars.

"""

def delta(x):
    a = next(x)
    for b in x:
        yield b - a
        a = b


def positive_sums(x):
    s = 0
    for c in x:
        s += c
        if s > 0:
            yield s
        else:
            s = 0


prices = [9, 11, 8, 5, 7, 10]
print(max(positive_sums(delta(iter(prices)))))
