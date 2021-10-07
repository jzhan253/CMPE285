import yfinance as yf
import datetime

def main():
    while(True):
        symbol = input("Input:\nPlease enter a symbol:\n")
        print("Output:")
        time = datetime.datetime.now()
        print(time.strftime('%a') + ' ' + 
            time.strftime('%b') + ' ' + 
            time.strftime('%d') + ' ' + 
            time.strftime('%X') + ' ' + 
            time.strftime('%Z') + 
            time.strftime('%Y'))
        try:
            company = yf.Ticker(symbol)
            info = company.info
        except:
            print('Connection with internal financial API has failed, check your internet connection.')
            break
        if info['regularMarketPrice'] == None:
            print('Invalid symbol! Please check for company stock symbol before enter!')
            continue
        today = company.history(period='1d')
        print(info['shortName'] + '(' + info['symbol'] + ')')
        close_price = today['Close'][0]
        open_price = today['Open'][0]
        diff = close_price - open_price
        if open_price == 0:
            print('Data have error, open price is 0')
        diff_per = (diff / open_price) * 100
        diff_str = '{:.2f}'.format(diff)
        diff_per_str = '{:.2f}'.format(diff_per) + '%'
        if diff > 0:
            diff_str = '+' + diff_str
            diff_per_str = '+' + diff_per_str
        elif diff < 0:
            diff_str = '-' + diff_str
            diff_per_str = '-' + diff_per_str
        print(str(info['currentPrice']) + ' ' + diff_str + ' (' + diff_per_str + ')')


if __name__ == '__main__':
    main()