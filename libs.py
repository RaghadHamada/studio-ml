import datawarehouse

fmp = datawarehouse.FMP()
ticker = 'AAPL'


start = '2023-01-01'
end = '2023-01-31'
df = fmp.recent_stock_info(tickers=[ticker],start=start,end=end)
print(df)
