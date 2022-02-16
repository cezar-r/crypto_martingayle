


import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter, StrMethodFormatter
import numpy as np


plt.style.use('ggplot')

plt.style.use("dark_background")


starting_leverage = [1.5, 2, 3, 4, 5, 6, 10]
COINPRICE = 100
BALANCE = 100_000


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
			balance -= 10000
			trades += 1

		fig, ax = plt.subplots()



		ax.set_title(f'{og_lev}x Leverage\n{round(100  - price, 2)}% Drop before Total Liquidation')
		ax.plot(x, liquidation_levels)
		ax.yaxis.set_major_formatter('{x:1.2f}%')
		ax.set_xlabel("Leveraged Position")
		ax.set_ylabel("Price")
		# ax.set_xticklabels([(2**(i))*og_lev for i in x])
		plt.tight_layout()
		# plt.savefig(f"imgs/{og_lev}_leverage_tot_liq.png")
		plt.show()



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
			balance -= 10000
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
				gain_pct.append(((((COINPRICE - price)/price) * leverage)  - ((BALANCE - balance) / 20000)) * 100) 
				balance -= 20000
				trades += 1

		fig, ax = plt.subplots()

		ax.set_title(f'{og_lev}x Leverage\n% Gains On Price Breakeven')
		ax.plot(x, gain_pct)
		ax.yaxis.set_major_formatter('{x:1.2f}%')
		ax.set_xlabel("# of Trades")
		ax.set_ylabel("Gains after price breakeven")
		plt.tight_layout()
		# plt.savefig(f"imgs/{og_lev}_profit_breakeven.png")
		plt.show()



# to_profit()
# total_liquidation()
profit_at_breakeven()


'''
Total Liquidation: when the price falls below total liquidation, the strategy will not work

Y-axis shows the price of the ticker since the first trade placed
X-axis shows number of trades placed

Think of the flat part of the graph as how much you can afford the stock to drop
(since you initally bought it) before the strategy will not work.

With this strategy, a good bet would be to do each order as 1/5th of your bankroll
as after 5 trades is when the line starts to plateau

'''