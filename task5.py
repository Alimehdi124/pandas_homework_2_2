import pandas as pd

sales = pd.DataFrame([
    ['Avatar', 'Baku', 165],
    ['Dune', 'Baku', 120],
    ['Interstellar', 'Baku', 180],
    ['Avatar', 'Ganja', 95],
    ['Dune', 'Ganja', 125],
    ['Interstellar', 'Ganja', 130],
    ['Avatar', 'Sumgait', 140],
    ['Dune', 'Sumgait', 80],
    ['Interstellar', 'Sumgait', 100],
    ['Avatar', 'Shaki', 70],
    ['Dune', 'Shaki', 65],
    ['Interstellar', 'Shaki', 90]
], columns=['Movie', 'City', 'Tickets Sold'])

movie_totals = sales.groupby('Movie')['Tickets Sold'].sum().sort_values(ascending=False)
city_totals = sales.groupby('City')['Tickets Sold'].sum().sort_values(ascending=False)
print(sales.to_string(index=False))
print('\nTickets by movie:\n', movie_totals)
print('\nTickets by city:\n', city_totals)
print('\nTop movie:', movie_totals.idxmax(), movie_totals.max())
