#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # starting at the first position in array and compare to the next element to the right
  # defaul profit: second price (sell) - first price (buy)
  max_profit = prices[1] - prices[0]
  for i in range(len(prices)):  # looking at index
      for j in range(i + 1, len(prices)):  # looking at item to the right of index
          if prices[j] - prices[i] > max_profit:
              max_profit = prices[j] - prices[i]

  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))