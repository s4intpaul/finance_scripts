
watchlist ={}

def add_to_watchlist(watchlist):
    ticker = input(f"Enter ticker: ").upper()
    target = float(input(f"Enter target price for {ticker}: $"))
    watchlist[ticker] = {"target": target}
    print(f"Added {ticker} to watchlist at ${target:.2f}")

def main():
    add_to_watchlist(watchlist)
    add_to_watchlist(watchlist)
    add_to_watchlist(watchlist)
    print(watchlist)

if __name__ == "__main__":
   main()
