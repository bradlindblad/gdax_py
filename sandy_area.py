import gdax
import pandas as pd

my_client = gdax.PublicClient()

curr_eth_bid = my_client.get_product_ticker("ETH-USD")["bid"]
curr_eth_ask = my_client.get_product_ticker("ETH-USD")["ask"]
spread = pd.to_numeric(curr_eth_ask) - pd.to_numeric(curr_eth_bid)
print("hello darkness my old friend")

print("hi")