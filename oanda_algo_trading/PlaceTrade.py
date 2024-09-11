import pandas as pd
import tpqoa

api = tpqoa.tpqoa("oanda.cfg")

dataframe = api.get_history(instrument = "EUR_USD", start = "2024-09-01", end = "2024-09-11",
                granularity = "D", price = "B")

print (dataframe)

#api.create_order(instrument = "EUR_USD", units = 1000, sl_distance= 0.1)

data = api.get_account_summary()
print (data["balance"])
