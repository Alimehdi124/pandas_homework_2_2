from pathlib import Path
import pandas as pd

orders = pd.read_csv(Path(__file__).with_name('orders.csv'))
print(orders.head(10).to_string(index=False))
print('\nOrders per customer:\n', orders['Customer'].value_counts())
print('\nMaximum amount:', orders['Amount'].max())
print('Minimum amount:', orders['Amount'].min())
print('Total amount:', round(orders.Amount.sum(), 2))
