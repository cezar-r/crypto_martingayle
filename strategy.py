#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np


plt.style.use('ggplot')
plt.style.use("dark_background")


starting_leverage = [1.5, 2, 3, 4, 5, 6, 10]
COINPRICE = 100
BALANCE = 100_000
TRADESIZE = 10_000

def total_liquidation():
	for leverage in starting_leverage:
		og_lev = leverage
		price = COINPRICE
		balance = BALANCE
		liquidation_levels = [price]
		x = [0]
		trades = 0

		while balance > 0:
			price = price * (1 - (1/leverage))
			liquidation_levels.append(price)
			x.append(trades + 1)
			print(leverage)
			leverage *= 2
			balance -= TRADESIZE
			trades += 1

		fig, ax = plt.subplots()
		ax.set_title(f'{og_lev}x Leverage\n{round(100  - price, 2)}% Drop before Total Liquidation')
		ax.plot(x, liquidation_levels)
		ax.yaxis.set_major_formatter('{x:1.2f}%')
		ax.set_xlabel("Leveraged Position")
		ax.set_ylabel("Price")
		plt.tight_layout()
		plt.savefig(f"imgs/{og_lev}_leverage_tot_liq.png")
		# plt.show()



def to_profit():
	for leverage in starting_leverage:
		og_lev = leverage
		price = COINPRICE
		balance = BALANCE
		x = []
		to_profit = []
		trades = 0

		while balance > 0:
			price = price * (1 - (1/leverage))
			x.append(trades + 1)
			leverage *= 2
			to_profit.append((COINPRICE - price)/(price*leverage) * 100)
			balance -= TRADESIZE
			trades += 1

		fig, ax = plt.subplots()
		ax.set_title(f'{og_lev}x Leverage\n% Move to Break Even')
		ax.plot(x, to_profit)
		ax.yaxis.set_major_formatter('{x:1.2f}%')
		ax.set_xlabel("# of Trades")
		ax.set_ylabel("% to break even")
		plt.tight_layout()
		plt.savefig(f"imgs/{og_lev}_leverage_to_profit.png")
		# plt.show()


def profit_at_breakeven():
	for leverage in starting_leverage:
		og_lev = leverage
		price = COINPRICE
		balance = BALANCE
		x = [0]
		gain_pct = [0]
		trades = 0

		while balance > 0:
				price = price * (1 - (1/leverage))
				x.append(trades + 1)
				leverage *= 2
				#  takes into account losses on previous trades.
				gain_pct.append(((((COINPRICE - price)/price) * leverage)  - ((BALANCE - balance) / (TRADESIZE*2))) * 100) 
				balance -= TRADESIZE*2
				trades += 1

		fig, ax = plt.subplots()
		ax.set_title(f'{og_lev}x Leverage\n% Gains On Price Breakeven')
		ax.plot(x, gain_pct)
		ax.yaxis.set_major_formatter('{x:1.2f}%')
		ax.set_xlabel("# of Trades")
		ax.set_ylabel("Gains after price breakeven")
		plt.tight_layout()
		plt.savefig(f"imgs/{og_lev}_profit_breakeven.png")
		# plt.show()


if __name__ == '__main__':
	# to_profit()
	# total_liquidation()
	# profit_at_breakeven()


