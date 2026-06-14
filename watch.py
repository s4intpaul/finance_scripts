import yfinance as yf

watchlist ={}

def ticker_count(count, tickers):
    count = int(input(f"How many Tickers?: "))
    if count > 10:
        print("Exceeded Max Count(10). Try Again.")
    elif count > 0 and len(tickers) < count:
        for i in range(count):
            add_to_watchlist(watchlist)

def add_to_watchlist(watchlist):
    ticker: str = input(f"Enter ticker: ").upper()
    target = float(input(f"Enter target price for {ticker}: $"))
    watchlist[ticker] = {"target": target}
    print(f"Added {ticker} to watchlist at ${target:.2f}")

def get_price(ticker):
    stock = yf.Ticker(ticker)
    return stock.info["currentPrice"]


def main():
    ticker_count(0, watchlist)

    for ticker in watchlist:
        price = get_price(ticker)
        print(f"{ticker}: {price:.2f}")

    for ticker in watchlist:
        price = get_price(ticker)
        target = watchlist[ticker]["target"]

        if price >= target:
            print(f"{ticker}: ${price:.2f} TARGET ACQUIRED (target: {target:.2f})")
        else:
            diff = abs(target - price)
            print(f"{ticker:} ${price} | ${diff:.2f} away from target ${target:.2f}")

if __name__ == "__main__":
   main()



