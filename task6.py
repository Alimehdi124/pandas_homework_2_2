import pandas as pd

customers = pd.DataFrame([
    [1, 'Aysel', 'Baku'],
    [2, 'Murad', 'Ganja'],
    [3, 'Nigar', 'Sumgait'],
    [4, 'Elvin', 'Baku'],
    [5, 'Leyla', 'Lankaran']
], columns=['ID', 'Name', 'City'])

orders = pd.DataFrame([
    [1, 'Laptop', 1200],
    [2, 'Mouse', 35],
    [1, 'Keyboard', 80],
    [3, 'Monitor', 350],
    [4, 'Headphones', 90],
    [5, 'Tablet', 520],
    [2, 'Phone', 800]
], columns=['Customer ID', 'Order', 'Cost'])

merged = pd.merge(customers, orders, left_on='ID', right_on='Customer ID', how='inner')
totals = merged.groupby(['ID', 'Name', 'City'], as_index=False).agg({'Cost': 'sum'})
print('Customers:\n', customers.to_string(index=False))
print('\nOrders:\n', orders.to_string(index=False))
print('\nMerged:\n', merged.to_string(index=False))
print('\nTotal cost per customer:\n', totals.to_string(index=False))
