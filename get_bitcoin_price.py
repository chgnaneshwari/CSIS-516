
from forex_python.bitcoin import BtcConverter

def GetPriceInUSD():
    btc_converter = BtcConverter()
    PriceInUsd = btc_converter.get_latest_price("USD")
 
    return f"{PriceInUsd}"

print(f"The current bitcoin price in USD is ${BtcConverter().get_latest_price('USD'):.2f}"
)