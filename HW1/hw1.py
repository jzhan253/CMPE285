def proceed(allotment, final_share_price):
    return allotment * final_share_price

def cost(allotment, initial_share_price, commissions, capital_gain_tax):
    return allotment * initial_share_price + commissions + capital_gain_tax

def net_profit(proceeds, cost):
    return proceeds - cost

def capital_gain(allotment, final_share_price, initial_share_price, sell_commission, buy_commission):
    return allotment * (final_share_price - initial_share_price) - sell_commission - buy_commission

def capital_gain_tax(allotment, final_share_price, initial_share_price, sell_commission, buy_commission, tax_rate):
    return capital_gain(allotment, final_share_price, initial_share_price, sell_commission, buy_commission) * tax_rate

def break_even(allotment, initial_share_price, buy_commission, sell_commission):
    if allotment == 0:
        return 0
    return (allotment * initial_share_price + buy_commission + sell_commission) / allotment


def cost_detail(allotment, initial_share_price, buy_commission, sell_commission, capital_gain, tax_rate):
    print('\nCost details:\nTotal Purchase Price\n' + '{:,}'.format(int(allotment)) + ' × $' + '{:,}'.format(int(initial_share_price)) + ' = ' + '{:,.2f}'.format(allotment * initial_share_price))
    print('Buy Commission: = ' + '{:,.2f}'.format(buy_commission))
    print('Sell Commission: = ' + '{:,.2f}'.format(sell_commission))
    print('Tax on Capital Gain = ' + '{:,}'.format(int(tax_rate)) + '% of $' + '{:,.2f}'.format(capital_gain) + ' = ' + '{:,.2f}'.format(tax_rate * 0.01 * capital_gain))
    print()


def main():
    print('Compute Your Profit:\n')
    symbol = input('Ticket Symbol:\n')
    allotment = float(input('\nAllotment:\n'))
    final_share_price = float(input('\nFinal Share Price:\n'))
    sell_commission = float(input('\nSell Commission:\n'))
    initial_share_price = float(input('\nInitial Share Price:\n'))
    buy_commission = float(input('\nBuy Commission:\n'))
    tax_rate = float(input('\nCapital Gain Tax Rate(%):\n'))
    tax_rate_per = tax_rate * 0.01
    proceeds = proceed(allotment, final_share_price)
    print('\nPROFIT REPORT:\nProceeds\n$' + '{:,.2f}'.format(proceeds))
    tax = capital_gain_tax(allotment, final_share_price, initial_share_price, sell_commission, buy_commission, tax_rate_per)
    costs = cost(allotment, initial_share_price, sell_commission + buy_commission, tax)
    print('\nCost:\n$' + '{:,.2f}'.format(costs))
    cost_detail(allotment, initial_share_price, buy_commission, sell_commission, capital_gain(allotment, final_share_price, initial_share_price, sell_commission, buy_commission), tax_rate)
    print('Net Profit\n$' + '{:,.2f}'.format(proceeds - costs))
    print('\nReturn on Investment\n' + '{:,.2f}'.format(proceeds * 100 / costs - 100) + '%')
    print('\nTo break even, you should have a final share price of\n$' + '{:,.2f}'.format(break_even(allotment, initial_share_price, buy_commission, sell_commission)))

if __name__ == '__main__':
    main()