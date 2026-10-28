import pandas as pd

books = pd.DataFrame([
    ['The Psychology of Money', 'Morgan Housel', 2020, 19.0],
    ['Clean Code', 'Robert Martin', 2008, 32.0],
    ['The Silent Patient', 'Alex Michaelides', 2019, 14.0],
    ['Digital Minimalism', 'Cal Newport', 2019, 22.0],
    ['The Alchemist', 'Paulo Coelho', 1988, 12.5],
    ['Project Hail Mary', 'Andy Weir', 2021, 25.0]
], columns=['Title', 'Author', 'Year Published', 'Price'])

print(books.to_string(index=False))
print('\nAverage price:', round(books.Price.mean(), 2))
print('\nPublished after 2015:\n', books[books['Year Published'] > 2015].to_string(index=False))
print('\nSorted by price:\n', books.sort_values(by='Price', ascending=True).to_string(index=False))
