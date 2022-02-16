# Crypto Martingale Leverage Strategy

## Background
The Martingale Strategy is one of the most popular strategies when it comes to gambling. The main idea behind this strategy is to double your bet every time you lose in a game.
For example, say you're playing roulette. You bet $5 on red, and it hits black. The next bet will be $10, then $20, etc. 
This strategy will work a majority of the time in recouping losses, however it will not work forever as you need to have an infinite bankroll.
Be wary though, as the size of your bets increase exponentially with this strategy. If you start with $2 bets, your 10th bet will be $1,024 (and that's only to make $2 back).
[Read More Here](https://en.wikipedia.org/wiki/Martingale_(betting_system))

## Leverage Trading
Leverage trading is one of the riskiest ways to trade, especially in a market as volatile as crypto. This is when you borrow money from the exhange for your trade.
For example, say you want to invest $1,000 into Bitcoin on 5x leverage. The exhange will lend you another $4,000. When you close your trade, the $4,000 goes back to the exhange and you keep the profits.

### Liquidations
The riskiest part of the leverage trading is quite obvious; you are using someone else's money and the size of your trades are relatively large to what they usually are.
Another risk that you need to take into consideration before leverage trading is getting liquidated. Liquidation happens when the asset moves 1 / leverage in the opposite direction.
Let's go back to our example earlier, where we did a 5x leverage trade on Bitcoin. Let's also assume this was a short trade (we want Bitcoin to go down in price). You will be liquitaed of your $1,000 if Bitcoin goes up 20% (1 / 5). 

## Strategy
Leverage provides a unique opportunity to use the Martigale strategy, but without its major pitfalls of exponentially increasing bets. In this strategy, we will be placing leveraged trades. Once we get liquidated, rather than doubling our bet, we will just double our leverage position.
Going back to that example again, if Bitcoin rises 20%, we would then open a 10x leverage short with $1,000. The next position will be 20x, 40x, etc.

### Pros 
One of the major advantages of this strategy is that your bets remain constant (you are never risking more than $1,000 per trade), therefore your losses are linear. The classic Martingale strategy requires an exponential increase in bets (you are risking 2x your previous bet per trade). 

This strategy also doesn't require you to time the market that well (obviously the higher your opening leverage position is the better you will need to time the market).

## Explanation
You may be thinking "40x leverage position, are you crazy?". But let's check out the math.

 - If you start this strategy off with a 1.5x leverage long position, you will need to see the asset fall 84% from the price you initally traded at to lose all of your bankroll. If this is the case, we are most likely in a Black Swan event and there are other priorities we would probably be worried about.
 <img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/1.5_leverage_tot_liq.png' height = 300 width = 400>

 - What about something riskier like 3x? To see "Total Liquidation" (when the asset price falls below the graph's plateau), the asset will need to fall 53.17%, which is still a pretty safe bet to make. If the asset falls 33%, we will then open a 6x leveraged position at that price. If the asset falls 40% from the original price, we open a 12x leveraged position. 
 
 <img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/3_leverage_tot_liq.png' height = 300 width = 400>
 - Now imagine, you placed these trades towards the bottom of a bear market. You would be holding a heavily leverage position from the very bottom. This is what I meant earlier by this strategy not needing "perfect timing" but "rough timing".


### Profit Taking
You may also be thinking, "how much would the asset have to rise for me to profit". Each trade that is made, requires a smaller move by the asset for us to break even.
- Let's continue with our 3x leveraged position example. The asset has fallen 42% since we started trading and we now have a very large 12x leveraged position. We only need to asset to go up 4% to break back even. And as you can see, this line also begins to plateau the more leveraged positions we take.
<img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/3_leverage_to_profit.png' height = 300 width = 400>

- What if the asset were to breakeven? According to the chart below, we would be up about 900% (10x) on our trade.
<img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/3_profit_breakeven.png' height = 300 width = 400>

- If we look at the 5x Leverage chart, on our 4th trade, when the asset is down 33%, we will have a 80x leveraged position and only need a .6% move in the market to break even. 

<img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/5_leverage_to_profit.png' height = 300 width = 400> <img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/5_leverage_tot_liq.png' height = 300 width = 400>

- Better yet, if the asset breaks even to where we orignally starting trading, we are up an astounding 4,000% (41x).
<img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/5_profit_breakeven.png' height = 300 width = 400>

## Downsides
One of the downsides of this strategy is you need to be certain that a bottom (or top) is coming sometime soon in the market, as well as how far the bottom (or top) is in terms of price (think previous highs or lows).
Another potential downside (although rare) is the asset price does not move from one liquidation level to another, meaning we can't make bigger trades.

## Closing Notes
- This readme mainly talked about this strategy being used in crypto as crypto exhanges are more open to large leveraged positions, however this can just as easily work with stocks and other assets.
 - As mentioned eariler, the downside is relatively small to the size of our trades. Worst comes to worst, we lost the investment in very unique market conditions (the market would have to move 40%+). The upside however, is unlimited. In the 5x leveraged example, if the asset bottoms out at 33% and fully recovers, we are looking at about a 2640% increase in our investment.

## Risk Management
This is not financial advice, simply it is exploring the math behind leveraged trading
To implore this strategy, you must be sure the asset will not hit the Total Liquidation Price
Based on the charts, it is recommended you split your trade into no more than 6 trades, as after your 6th trade you will be getting liquidated very quickly.

## Example
- Below is an example of this strategy in play:
<img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/BTCUSD_2022-02-15_18-35-28.png' height = 380 width = 800>

## Charts
- Below are charts that examine each starting leverage position for this strategy.
- In the following charts, you can identify the leveraged position at each x-value by computing (2^x) * leverage
### 1.5x 
<img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/1.5_leverage_to_profit.png' height = 300 width = 400> <img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/1.5_leverage_tot_liq.png' height = 300 width = 400> <img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/1.5_profit_breakeven.png' height = 300 width = 400>
### 2x 
<img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/2_leverage_to_profit.png' height = 300 width = 400> <img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/2_leverage_tot_liq.png' height = 300 width = 400> <img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/2_profit_breakeven.png' height = 300 width = 400>
### 3x 
<img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/3_leverage_to_profit.png' height = 300 width = 400> <img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/3_leverage_tot_liq.png' height = 300 width = 400> <img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/3_profit_breakeven.png' height = 300 width = 400>
### 4x 
<img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/4_leverage_to_profit.png' height = 300 width = 400> <img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/4_leverage_tot_liq.png' height = 300 width = 400> <img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/4_profit_breakeven.png' height = 300 width = 400>
### 5x 
<img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/5_leverage_to_profit.png' height = 300 width = 400> <img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/5_leverage_tot_liq.png' height = 300 width = 400> <img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/5_profit_breakeven.png' height = 300 width = 400>
### 6x 
<img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/6_leverage_to_profit.png' height = 300 width = 400> <img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/6_leverage_tot_liq.png' height = 300 width = 400> <img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/6_profit_breakeven.png' height = 300 width = 400>
### 10x 
<img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/10_leverage_to_profit.png' height = 300 width = 400> <img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/10_leverage_tot_liq.png' height = 300 width = 400> <img src = 'https://github.com/cezar-r/crypto_martingayle/blob/master/imgs/10_profit_breakeven.png' height = 300 width = 400>

## Code
- All code can be found in strategy.py

### Total Liquidation Graph
[Here](https://github.com/cezar-r/crypto_martingayle/blob/0724c9e8cb9300b8f18ddc85f5f76e625579ac84/strategy.py#L17)

### Asset % Increase to Break Even on Bankroll
[Here](https://github.com/cezar-r/crypto_martingayle/blob/0724c9e8cb9300b8f18ddc85f5f76e625579ac84/strategy.py#L47)

### Gains % When Asset Breaks Even
[Here](https://github.com/cezar-r/crypto_martingayle/blob/0724c9e8cb9300b8f18ddc85f5f76e625579ac84/strategy.py#L75)
