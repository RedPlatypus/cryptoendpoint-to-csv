# Bitfinex Converter

Take an endpoint like `https://api.bitfinex.com/v2/candles/trade:1m:tSTJBTC/hist` and convert it into a csv for easier analysis.

Process

1. go to the endpoint
2. copy txt into data.txt
3. run `python3 start.py`
    1. this script looks for `data.txt` and will convert it to `info.csv`
4. open `info.csv` in your favourite excel like program